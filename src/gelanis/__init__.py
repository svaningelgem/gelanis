"""gelanis module"""
# flake8: noqa

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

from . import exceptions, fileio, streaming
from ._config import config
from .accumulators import Accumulator, AccumulatorParam
from .broadcast import Broadcast
from .cache_manager import CacheManager, TimedCacheManager
from .context import SparkContext
from .rdd import RDD
from .sql import Row
from .statcounter import StatCounter
from .storagelevel import StorageLevel

__all__ = [
    'RDD', 'SparkContext', 'Broadcast', 'StatCounter', 'CacheManager', 'Row',
    'TimedCacheManager', 'StorageLevel',
    'exceptions', 'fileio', 'streaming',
    'config',
]


def setup(spark_version: str) -> None:
    config.spark_version = spark_version

    from ._auto_injector import Pyspark2Gelanis
    Pyspark2Gelanis.setup()
