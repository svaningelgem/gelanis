import pytest

from pysparkling.sql import SparkSession
from pysparkling.sql.functions import array, col, map_from_arrays


def _strip_line(line: str) -> str:
    return (
        '\n'.join(
            x.rstrip() for x in line.split('\n')
        )
        .strip()
    )


@pytest.fixture(name='spark')
def fixture_spark():
    return (
        SparkSession.builder
        .master("local")
        .appName("SparkByExamples.com")
        .getOrCreate()
    )


@pytest.fixture(name='df')
def fixture_df(spark):
    data = [
        ('James', '', 'Smith', '1991-04-01', 'M', 3000),
        ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
        ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
        ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
        ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1),
    ]

    columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]
    return spark.createDataFrame(data=data, schema=columns)


def test_df_show(df, capsys):
    df.show()
    captured = capsys.readouterr()

    expected = ("""
+---------+----------+--------+----------+------+------+
|firstname|middlename|lastname|       dob|gender|salary|
+---------+----------+--------+----------+------+------+
|    James|          |   Smith|1991-04-01|     M|  3000|
|  Michael|      Rose|        |2000-05-19|     M|  4000|
|   Robert|          |Williams|1978-09-05|     M|  4000|
|    Maria|      Anne|   Jones|1967-12-01|     F|  4000|
|      Jen|      Mary|   Brown|1980-02-17|     F|    -1|
+---------+----------+--------+----------+------+------+
""").lstrip()

    assert captured.out == expected


def test_df_show_array(spark, capsys):
    df = spark.range(3)
    df.select(array(df.id, df.id * 2)).show()

    actual = capsys.readouterr().out
    expected = """
+-------------------+
|array(id, (id * 2))|
+-------------------+
|             [0, 0]|
|             [1, 2]|
|             [2, 4]|
+-------------------+
""".lstrip()

    assert actual == expected


def test_df_show_map_from_arrays(spark, capsys):
    df = spark.range(3)
    df.select(map_from_arrays(array(df.id), array(df.id))).show()

    actual = capsys.readouterr().out
    expected = """
+-------------------------------------+
|map_from_arrays(array(id), array(id))|
+-------------------------------------+
|                             [0 -> 0]|
|                             [1 -> 1]|
|                             [2 -> 2]|
+-------------------------------------+
""".lstrip()

    assert actual == expected


def test_df_show_map_from_arrays_array(spark, capsys):
    df = spark.range(3)
    df.select(map_from_arrays(array(df.id, df.id * 2), array(df.id, df.id * 2))).show()

    actual = capsys.readouterr().out
    expected = """
+---------------------------------------------------------+
|map_from_arrays(array(id, (id * 2)), array(id, (id * 2)))|
+---------------------------------------------------------+
|                                                 [0 -> 0]|
|                                         [1 -> 1, 2 -> 2]|
|                                         [2 -> 2, 4 -> 4]|
+---------------------------------------------------------+
""".lstrip()

    assert actual == expected


def test_df_show_vertical(spark, capsys):
    c = col("id")
    (
        spark
        .range(9, 11)
        .select(c, c * 2, c ** 2)
        .show(vertical=True)
    )

    actual = capsys.readouterr().out
    expected = """
-RECORD 0-------------
 id           | 9
 (id * 2)     | 18
 POWER(id, 2) | 81.0
-RECORD 1-------------
 id           | 10
 (id * 2)     | 20
 POWER(id, 2) | 100.0
"""

    assert _strip_line(actual) == _strip_line(expected)


def test_df_cube_1(spark, capsys):
    df = spark.createDataFrame([(2, 'Alice'), (5, 'Bob'), (5, 'Carl')], ["age", "name"])
    df.cube("name", df.age).count().orderBy("name", "age", "count").show()
    actual = capsys.readouterr().out
    expected = """
+-----+----+-----+
| name| age|count|
+-----+----+-----+
| null|null|    3|
| null|   2|    1|
| null|   5|    2|
|Alice|null|    1|
|Alice|   2|    1|
|  Bob|null|    1|
|  Bob|   5|    1|
| Carl|null|    1|
| Carl|   5|    1|
+-----+----+-----+
"""

    assert _strip_line(actual) == _strip_line(expected)


def test_df_cube_2(spark, capsys):
    df = spark.createDataFrame([(2, 'Alice'), (5, 'Bob'), (5, None)], ["age", "name"])
    df.cube("name", df.age).count().orderBy("name", "age", "count").show()
    actual = capsys.readouterr().out
    expected = """
+-----+----+-----+
| name| age|count|
+-----+----+-----+
| null|null|    1|
| null|null|    3|
| null|   2|    1|
| null|   5|    1|
| null|   5|    2|
|Alice|null|    1|
|Alice|   2|    1|
|  Bob|null|    1|
|  Bob|   5|    1|
+-----+----+-----+
"""

    assert _strip_line(actual) == _strip_line(expected)
