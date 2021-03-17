import importlib
from importlib.abc import Loader, MetaPathFinder
import sys
import time
import warnings


class _TransparentImporter(MetaPathFinder, Loader):
    __from__ = None
    __to__ = None

    @classmethod
    def find_spec(cls, name, path, target=None):
        splitted = name.split('.')
        if splitted[0] != cls.__from__:
            return None  # Nope. We're not providing this..

        splitted[0] = cls.__to__
        new_name = '.'.join(splitted)
        return importlib.util.spec_from_loader(name, cls(new_name, name))

    def __init__(self, new_name: str, old_name: str):
        self.new_name = new_name
        self.old_name = old_name

    def create_module(self, spec):
        module = importlib.import_module(self.new_name)
        return module

    def exec_module(self, module):
        sys.modules[self.old_name] = module
        return None

    @classmethod
    def is_enabled(cls):
        return cls in sys.meta_path

    @classmethod
    def setup(cls):
        sys.meta_path.insert(0, cls)

        # Find any already loaded 'pyspark' modules:
        modules_to_set = [
            (source_name, cls.__to__ + source_name[len(cls.__from__):])
            for source_name in sys.modules
            if source_name.startswith(cls.__from__) and not source_name.startswith(cls.__to__)
        ]

        if not modules_to_set:
            return

        warnings.warn(
            f"{cls.__from__} was already loaded."
            f" Please setup {cls.__to__} first to ensure no nasty side-effects take place."
        )

        for old_name, new_name in modules_to_set:
            try:
                # Gelanis was already loaded?
                new_module = sys.modules[new_name]
            except KeyError:
                # Load it
                new_module = importlib.import_module(new_name)

            # And override it in the pyspark one
            sys.modules[old_name] = new_module


class Pyspark2Gelanis(_TransparentImporter):
    __from__ = 'pyspark'
    __to__ = 'gelanis'


class Gelanis2Pyspark(_TransparentImporter):
    __from__ = 'gelanis'
    __to__ = 'pyspark'


def _test(pyspark2gelanis: bool = True):
    # Comment or un-comment the next line to make the magic work...
    if pyspark2gelanis:
        Pyspark2Gelanis.setup()
        # pylint: disable=import-outside-toplevel
        from pyspark.sql import SparkSession
    else:
        Gelanis2Pyspark.setup()
        # pylint: disable=import-outside-toplevel
        from gelanis.sql import SparkSession

    start = time.time()

    spark = (
        SparkSession.builder
        .master("local")
        .appName("SparkByExamples.com")
        .getOrCreate()
    )
    data_list = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]
    rdd = spark.sparkContext.parallelize(data_list)
    print(rdd.collect())

    data = [
        ('James', '', 'Smith', '1991-04-01', 'M', 3000),
        ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
        ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
        ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
        ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1),
    ]

    columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]
    df = spark.createDataFrame(data=data, schema=columns)
    df.show()

    print(f"Finished this run in : {time.time() - start:.3f}s (Injector was on: {Pyspark2Gelanis.is_enabled()})")


if __name__ == '__main__':
    _test()
