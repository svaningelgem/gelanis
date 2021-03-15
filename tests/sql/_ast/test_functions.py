import pytest

from pysparkling import Row
from pysparkling.sql._ast.ast_to_python import parse_expression
from pysparkling.sql.types import IntegerType, StructField, StructType

ROW = Row(a=1, b=2, c=3)
SCHEMA = StructType([
    StructField("a", IntegerType()),
    StructField("b", IntegerType()),
])


SCENARIOS = {
    'Least(-1,0,1)': ('least', 'least(-1, 0, 1)', -1),
    'GREATEST(-1,0,1)': ('greatest', 'greatest(-1, 0, 1)', 1),
    'shiftRight ( 42, 1 )': ('shiftright', 'shiftright(42, 1)', 21),
    'ShiftLeft ( 42, 1 )': ('shiftleft', 'shiftleft(42, 1)', 84),
    "concat_ws('/', a, b )": ('concat_ws', 'concat_ws(/, a, b)', "1/2"),
    'instr(a, a)': ('instr', 'instr(a, a)', 1),  # rely on columns
    'instr(a, b)': ('instr', 'instr(a, b)', 0),  # rely on columns
    "instr('abc', 'c')": ('instr', 'instr(abc, c)', 3),  # rely on lit
}


@pytest.mark.parametrize('string, expected', SCENARIOS.items())
def test_functions(string, expected):
    operator, expected_parsed, expected_result = expected
    actual_parsed = parse_expression(string, True)

    assert expected_parsed == str(actual_parsed)
    assert operator == actual_parsed.pretty_name

    actual_result = actual_parsed.eval(ROW, SCHEMA)

    assert expected_result == actual_result
