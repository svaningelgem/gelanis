import logging

import pytest

from pysparkling import Row
from pysparkling.sql._ast.ast_to_python import parse_expression
from pysparkling.sql.types import StructType

ROW = Row()
SCHEMA = StructType()


SCENARIOS = {
    '60=60': ('EQ', '(60 = 60)', True),
    '60=12': ('EQ', '(60 = 12)', False),
    '60==12': ('EQ2', '(60 = 12)', False),
    '12<>12': ('NEQ', '(NOT (12 = 12))', False),
    '60<>12': ('NEQ', '(NOT (60 = 12))', True),
    '60!=12': ('NEQ2', '(NOT (60 = 12))', True),
    '60<12': ('LT', '(60 < 12)', False),
    '60<=12': ('LTE', '(60 <= 12)', False),
    '60!>12': ('LTE2', '(60 <= 12)', False),
    '60>12': ('GT', '(60 > 12)', True),
    '60>=12': ('GTE', '(60 >= 12)', True),
    '60!<12': ('GTE2', '(60 >= 12)', True),
    '60+12': ('PLUS', '(60 + 12)', 72),
    '60-12': ('MINUS', '(60 - 12)', 48),
    '60*12': ('TIMES', '(60 * 12)', 720),
    # '60/12': ('DIVIDE', '(60 / 12)', None),
    '60%12': ('MODULO', '(60 % 12)', 0),
    # '60 div 12': ('DIV', '(60 DIV 12)', None),
    '6&3': ('BITWISE_AND', '(6 & 3)', 2),
    '6|3': ('BITWISE_OR', '(6 | 3)', 7),
    # '60||12': ('CONCAT', '(60 || 12)', None),
    '6^3': ('BITWISE_XOR', '(6 ^ 3)', 5),
    'true and false': ('LOGICAL_AND', '(true AND false)', False),
    'TRUE AND TRUE': ('LOGICAL_AND', '(true AND true)', True),
    'true AND null': ('LOGICAL_AND', '(true AND NULL)', None),
    'True or False': ('LOGICAL_OR', '(true OR false)', True),
    'false or false': ('LOGICAL_OR', '(false OR false)', False),
    'true or NULL': ('LOGICAL_OR', '(true OR NULL)', None),
    "+1": ("UNARY_PLUS", '(+ 1)', 1),
    "-(1)": ("UNARY_MINUS", '(- 1)', -1),
    "~8": ("BITWISE_NOT", '~8', -9),
    'not true': ("NOT", '(NOT true)', False),
    'Not Null': ("NOT", '(NOT NULL)', None),
}


@pytest.mark.parametrize('string, expected', SCENARIOS.items())
def test_operations(string, expected):
    operator, expected_parsed, expected_result = expected
    logging.debug("Testing %s", operator)
    actual_parsed = parse_expression(string, True)

    assert expected_parsed == str(actual_parsed)

    actual_result = actual_parsed.eval(Row(), SCHEMA)

    assert expected_result == actual_result
