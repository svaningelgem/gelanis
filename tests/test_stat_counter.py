import gelanis
from gelanis.sql._statcounter import ColumnStatHelper
from gelanis.sql.functions import col
from gelanis.sql.types import IntegerType, Row, StructField, StructType


def test_mean():
    d = [1, 4, 9, 160]
    s = gelanis.StatCounter(d)
    assert sum(d) / len(d) == s.mean()


def test_column_stat_helper():
    """
    Expected quantile values come from use of org.apache.spark.sql.catalyst.util.QuantileSummaries
    """
    schema = StructType([StructField("value", IntegerType())])
    helper = ColumnStatHelper(col("value"))
    for i in range(1, 100001):
        helper.merge(Row(value=i), schema)
    helper.finalize()
    assert helper.count == 100000
    assert helper.min == 1
    assert helper.max == 100000
    assert helper.mean == 50000.5
    assert helper.stddev == 28867.65779668774  # sample standard deviation
    assert helper.get_quantile(0) == 1
    assert helper.get_quantile(0.25) == 24998
    assert helper.get_quantile(0.5) == 50000
    assert helper.get_quantile(0.75) == 74993
    assert helper.get_quantile(1) == 100000


if __name__ == '__main__':
    test_mean()
    test_column_stat_helper()
