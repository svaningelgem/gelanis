![image](https://raw.githubusercontent.com/kbc-opensource/gelanis/master/logo/banner_black-w1500.png%0A%20:target:%20https://github.com/kbc-opensource/gelanis)

[![pypi-badge](https://badge.fury.io/py/gelanis.svg)](https://pypi.python.org/pypi/gelanis/), [![test-badge](https://github.com/kbc-opensource/gelanis/workflows/Tests/badge.svg)](https://github.com/kbc-opensource/gelanis/actions?query=workflow%3ATests), [![Documentation Status](https://readthedocs.org/projects/gelanis/badge/?version=latest)](https://pysparkling.readthedocs.io/en/latest/?badge=latest)

**Gelanis** is an enhanced version of [pysparkling](https://github.com/svenkreiss/pysparkling).

List of improvements:

-   Data types of the resulting dataframes are equal to pyspark

List of todos:

-   Implemented since/until + be able to target a certain pyspark version
-   Get a drop-in API compatibility with pyspark (auto-injector is written, but more tests are needed here).
-   Test the tests against both pyspark & pysparkling & compare the outputs so we're 100% certain both libraries are API equal.
-   Achieve API equality between pyspark & pysparkling (meaning that any public symbol should exist in both libraries).
-   Increase tests to ensure 100% compatibility with pyspark.

Some performance metrics I observed (5 simple union-tests):

| | gelanis | pyspark | speedup (times slower than gelanis) |
| --- | --- | --- | --- |
| startup | 0.542 | 47.112 | 87.0 |
| test 1 | 0.009 | 2.610 | 274.7 |
| test 2 | 0.008 | 2.721 | 340.1 | 
| test 3 | 0.008 | 2.761 | 345.1 | 
| test 4 | 0.009 | 2.471 | 274.6 | 
| test 5 | 0.013 | 2.486 | 191.2 | 

```python
import gelanis
gelanis.setup(spark_version='2.3.2')
```


Original pysparkling documentation:
============================================

**Pysparkling** provides a faster, more responsive way to develop programs for PySpark. It enables code intended for Spark applications to execute entirely in Python, without incurring the overhead of initializing and passing data through the JVM and Hadoop. The focus is on having a lightweight and fast implementation for small datasets at the expense of some data resilience features and some parallel processing features.

**How does it work?** To switch execution of a script from PySpark to pysparkling, have the code initialize a pysparkling Context instead of a SparkContext, and use the pysparkling Context to set up your RDDs. The beauty is you don't have to change a single line of code after the Context initialization, because pysparkling's API is (almost) exactly the same as PySpark's. Since it's so easy to switch between PySpark and pysparkling, you can choose the right tool for your use case.

**When would I use it?** Say you are writing a Spark application because you need robust computation on huge datasets, but you also want the same application to provide fast answers on a small dataset. You're finding Spark is not responsive enough for your needs, but you don't want to rewrite an entire separate application for the *small-answers-fast* problem. You'd rather reuse your Spark code but somehow get it to run fast. Pysparkling bypasses the stuff that causes Spark's long startup times and less responsive feel.

Here are a few areas where pysparkling excels:

-   Small to medium-scale exploratory data analysis
-   Application prototyping
-   Low-latency web deployments
-   Unit tests

Install
=======

``` {.sourceCode .bash}
pip install pysparkling[s3,hdfs,streaming]
```

[Documentation](https://pysparkling.trivial.io):

[![image](https://raw.githubusercontent.com/svenkreiss/pysparkling/master/docs/readthedocs.png)](https://pysparkling.trivial.io)

Other links: [Github](https://github.com/svenkreiss/pysparkling), [![pypi-badge](https://badge.fury.io/py/pysparkling.svg)](https://pypi.python.org/pypi/pysparkling/), [![test-badge](https://github.com/svenkreiss/pysparkling/workflows/Tests/badge.svg)](https://github.com/svenkreiss/pysparkling/actions?query=workflow%3ATests), [![Documentation Status](https://readthedocs.org/projects/pysparkling/badge/?version=latest)](https://pysparkling.readthedocs.io/en/latest/?badge=latest)

Features
========

-   Supports URI schemes `s3://`, `hdfs://`, `gs://`, `http://` and `file://` for Amazon S3, HDFS, Google Storage, web and local file access. Specify multiple files separated by comma. Resolves `*` and `?` wildcards.
-   Handles `.gz`, `.zip`, `.lzma`, `.xz`, `.bz2`, `.tar`, `.tar.gz` and `.tar.bz2` compressed files. Supports reading of `.7z` files.
-   Parallelization via `multiprocessing.Pool`, `concurrent.futures.ThreadPoolExecutor` or any other Pool-like objects that have a `map(func, iterable)` method.
-   Plain pysparkling does not have any dependencies (use `pip install pysparkling`). Some file access methods have optional dependencies: `boto` for AWS S3, `requests` for http, `hdfs` for hdfs

Examples
========

Some demos are in the notebooks [docs/demo.ipynb](https://github.com/svenkreiss/pysparkling/blob/master/docs/demo.ipynb) and [docs/iris.ipynb](https://github.com/svenkreiss/pysparkling/blob/master/docs/iris.ipynb) .

**Word Count**

``` {.sourceCode .python}
from pysparkling import Context

counts = (
    Context()
    .textFile('README.rst')
    .map(lambda line: ''.join(ch if ch.isalnum() else ' ' for ch in line))
    .flatMap(lambda line: line.split(' '))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)
print(counts.collect())
```

which prints a long list of pairs of words and their counts.
