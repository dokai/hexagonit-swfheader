The ``hexagonit.swfheader`` package provides a single function --
``parse`` -- that is able to parse the metadata in a SWF (Flash
animation) file. The main use case is to interrogate the dimensions of
a SWF file to help in embedding the file in a HTML page.

.. contents::

Usage
*****

Using the parser is very simple, simply call the
``hexagonit.swfheader.parse`` function and call it with either a
filesystem path or a file-like object.

    >>> import hexagonit.swfheader
    >>> metadata = hexagonit.swfheader.parse(TEST_SWF)
    >>> list(sorted(metadata.keys()))
    ['compressed', 'fps', 'frames', 'height', 'size', 'version', 'width', 'xmax', 'xmin', 'ymax', 'ymin']

    >>> metadata['width'], metadata['height']
    (550, 400)


The ``parse`` function returns a dictionary that contains the
following items:

``version (int)``

    The version of the Flash format, e.g. 7.

``compressed (bool)``

    ``True``, if the contents of the file are compressed using zlib
    compression, ``False`` otherwise.

``size (int)``

    Byte size of the (uncompressed) contents of the SWF file.

``xmin (int)``

    The lesser x-coordinate of the bounding rectangle of the contents.

``xmax (int)``

    The greater x-coordinate of the bounding rectangle of the contents.

``ymin (int)``

    The lesser y-coordinate of the bounding rectangle of the contents.

``ymax (int)``

    The greater y-coordinate of the bounding rectangle of the contents.

``width (int)``

    The width of the SWF file in pixels.

``height (int)``

    The height of the SWF file in pixels.

``frames (int)``

    The number of frames in the SWF file.

``fps (int)``

    Frames per second.

Command line
************

When installed with setuptools a script named ``swfheader`` is placed
in your bin directory which can be used to easily introspect SWF files
on the filesystem::

  $ swfheader some_file.swf
  SWF header
  ----------
  Version:      7
  Compression:  False
  Dimensions:   1105 x 1629
  Bounding box: (0, 1105, 0, 1629)
  Frames:       64
  FPS:          1
