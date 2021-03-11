from .. import Expression
from ...types import ArrayType


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
        # TODO: Check if we can generalize this. By default, this should be fine, but needs to be overridden in each
        #    subclass where it deviates from this standard.
        # pylint: disable=E1101
        return ArrayType(
            elementType=schema[str(self.column)].dataType,
            containsNull=self.column.is_nullable
        )
