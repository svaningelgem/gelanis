import tempfile

from memory_profiler import profile

import gelanis


@profile
def main():
    tempFile = tempfile.NamedTemporaryFile(delete=True)
    tempFile.close()

    sc = gelanis.Context()
    sc.parallelize(range(1000000)).saveAsTextFile(tempFile.name + '.gz')
    rdd = sc.textFile(tempFile.name + '.gz')
    rdd.collect()


if __name__ == '__main__':
    main()
