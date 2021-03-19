.. _api_fileio:


fileio
------

.. currentmodule:: gelanis

The functionality provided by this module is used in :func:`Context.textFile`
for reading and in :func:`RDD.saveAsTextFile` for writing.

.. currentmodule:: gelanis.fileio

You can use this submodule with :func:`File.dump`, :func:`File.load` and
:func:`File.exists` to read, write and check for existance of a file.
All methods transparently handle various schemas (for example ``http://``,
``s3://`` and ``file://``) and compression/decompression of ``.gz`` and
``.bz2`` files (among others).


.. autoclass:: gelanis.fileio.File
    :members:

.. autoclass:: gelanis.fileio.TextFile
    :members:


File System
^^^^^^^^^^^

.. autoclass:: gelanis.fileio.fs.FileSystem
    :members:

.. autoclass:: gelanis.fileio.fs.Local
    :members:

.. autoclass:: gelanis.fileio.fs.GS
    :members:

.. autoclass:: gelanis.fileio.fs.Hdfs
    :members:

.. autoclass:: gelanis.fileio.fs.Http
    :members:

.. autoclass:: gelanis.fileio.fs.S3
    :members:


Codec
^^^^^

.. autoclass:: gelanis.fileio.codec.Codec
    :members:

.. autoclass:: gelanis.fileio.codec.Bz2
    :members:

.. autoclass:: gelanis.fileio.codec.Gz
    :members:

.. autoclass:: gelanis.fileio.codec.Lzma
    :members:

.. autoclass:: gelanis.fileio.codec.SevenZ
    :members:

.. autoclass:: gelanis.fileio.codec.Tar
    :members:

.. autoclass:: gelanis.fileio.codec.TarGz
    :members:

.. autoclass:: gelanis.fileio.codec.TarBz2
    :members:

.. autoclass:: gelanis.fileio.codec.Zip
    :members:
