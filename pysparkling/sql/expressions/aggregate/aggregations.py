from pysparkling.sql.expressions.expressions import Expression
from pysparkling.sql.types import ArrayType


class Aggregation(Expression):
    @property
    def is_an_aggregation(self):
        return True

    def merge(self, row, schema):
        raise NotImplementedError

    def mergeStats(self, other, schema):
        raise NotImplementedError

    def eval(self, row, schema):
        raise NotImplementedError

    def args(self):
        raise NotImplementedError

    def data_type(self, schema):
        return ArrayType(
            elementType=schema[str(self.column)].dataType,
            containsNull=self.column.is_nullable
        )
