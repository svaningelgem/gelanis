import contextlib
import io

import pytest

from pysparkling import Context
from pysparkling.sql._ast.ast_to_python import parse_data_type, SqlParsingError
from pysparkling.sql.session import SparkSession
from pysparkling.sql.types import (
    ArrayType, BinaryType, BooleanType, ByteType, DateType, DecimalType, DoubleType, FloatType, IntegerType, LongType,
    MapType, NullType, ShortType, StringType, StructField, StructType, TimestampType
)

DATA_TYPE_SCENARIOS = {
    "BooLean": BooleanType(),
    "tinYint": ByteType(),
    "byte": ByteType(),
    "smallint": ShortType(),
    "short": ShortType(),
    "INT": IntegerType(),
    "integer": IntegerType(),
    "bigint": LongType(),
    "long": LongType(),
    "float": FloatType(),
    "real": FloatType(),
    "double": DoubleType(),
    "date": DateType(),
    "timestamp": TimestampType(),
    "string": StringType(),
    "binary": BinaryType(),
    "void": NullType(),
    "decimal": DecimalType(10, 0),
    "decimal(5)": DecimalType(5, 0),
    "decimal(5, 2)": DecimalType(5, 2),
    "deC": DecimalType(10, 0),
    "Dec(10,5)": DecimalType(10, 5),
    "numeric": DecimalType(10, 0),
    "Array<string>": ArrayType(StringType()),
    "Array<doublE>": ArrayType(DoubleType()),
    "Array<int>": ArrayType(IntegerType()),
    "Array<map<int, tinYint>>": ArrayType(MapType(IntegerType(), ByteType())),
    "Map<string, int>": MapType(StringType(), IntegerType()),
    "Map < integer, String >": MapType(IntegerType(), StringType()),
    "Struct<name: string, age: int>": StructType([
        StructField(name="name", dataType=StringType()),
        StructField(name="age", dataType=IntegerType()),
    ]),
    "array<struct<tinYint:tinyint>>": ArrayType(
        StructType([StructField('tinYint', ByteType())]),
    ),
    "MAp<int, ARRAY<double>>": MapType(IntegerType(), ArrayType(DoubleType())),
    "MAP<int, struct<varchar:string>>": MapType(
        IntegerType(),
        StructType([StructField("varchar", StringType())])
    ),
    "struct<intType: int, ts:timestamp>": StructType([
        StructField("intType", IntegerType()),
        StructField("ts", TimestampType())
    ]),
    "Struct<int: int, timestamp:timestamp>": StructType([
        StructField("int", IntegerType()),
        StructField("timestamp", TimestampType())
    ]),
    """
    struct<
        struct:struct<deciMal:DECimal, anotherDecimal:decimAL(5,2)>,
        MAP:Map<timestamp, varchar(10)>,
        arrAy:Array<double>,
        anotherArray:Array<char(9)>
    >
    """: StructType([
        StructField("struct", StructType([
            StructField("deciMal", DecimalType()),
            StructField("anotherDecimal", DecimalType(5, 2))
        ])),
        # StructField("MAP", MapType(TimestampType(), VarcharType(10))),
        StructField("MAP", MapType(TimestampType(), StringType())),
        StructField("arrAy", ArrayType(DoubleType())),
        # StructField("anotherArray", ArrayType(CharType(9)))])
        StructField("anotherArray", ArrayType(StringType()))
    ]),
    "struct<`x+y`:int, `!@#$%^&*()`:string, `1_2.345<>:\"`:varchar(20)>": StructType([
        StructField("x+y", IntegerType()),
        StructField("!@#$%^&*()", StringType()),
        # StructField("1_2.345<>:\"", VarcharType(20))])
        StructField("1_2.345<>:\"", StringType())
    ]),
    # # todo: "interval": CalendarIntervalType(),
    # # todo: "char": CharType(), + with param
    # # todo: "character": CharType(), + with param
    # # todo: "varchar": VarChar(), + with param
    # # Empty struct
    "strUCt<>": StructType([]),
    # DataType parser accepts certain reserved keywords.
    "Struct<TABLE: string, DATE:boolean>": StructType([
        StructField("TABLE", StringType()),
        StructField("DATE", BooleanType())
    ]),
    "struct<end: long, select: int, from: string>": StructType([
        StructField("end", LongType()),
        StructField("select", IntegerType()),
        StructField("from", StringType()),
    ]),
    "Struct<x: INT, y: STRING COMMENT 'test'>": StructType([
        StructField("x", IntegerType()),
        StructField("y", StringType(), metadata={'comment': 'test'}),
    ])
}


UNSUPPORTED_DATATYPES = [
    "it is not a data type",
    "struct<x+y: int, 1.1:timestamp>",
    "struct<x: int",
    "struct<x int, y string>",
]


SCHEMA_SCENARIOS = {
    'some_str: string, some_int: integer, some_date: date': (
        'root\n'
        ' |-- some_str: string (nullable = true)\n'
        ' |-- some_int: integer (nullable = true)\n'
        ' |-- some_date: date (nullable = true)\n'
    ),
    'some_str: string, arr: array<string>': (
        'root\n'
        ' |-- some_str: string (nullable = true)\n'
        ' |-- arr: array (nullable = true)\n'
        ' |    |-- element: string (containsNull = true)\n'
    ),
    'some_str: string, arr: array<array<string>>': (
        'root\n'
        ' |-- some_str: string (nullable = true)\n'
        ' |-- arr: array (nullable = true)\n'
        ' |    |-- element: array (containsNull = true)\n'
        ' |    |    |-- element: string (containsNull = true)\n'
    ),
}


@pytest.mark.parametrize("string, data_type", DATA_TYPE_SCENARIOS.items())
def test_equal(string, data_type):
    assert parse_data_type(string, debug=True) == data_type


@pytest.mark.parametrize("string", UNSUPPORTED_DATATYPES)
def test_raises(string):
    with pytest.raises(SqlParsingError):
        print(parse_data_type(string))


@pytest.mark.parametrize("schema, printed_schema", SCHEMA_SCENARIOS.items())
def test_dataframe_schema_parsing(schema, printed_schema):
    spark = SparkSession(Context())
    df = spark.createDataFrame([], schema=schema)

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        df.printSchema()
    assert printed_schema == f.getvalue()
