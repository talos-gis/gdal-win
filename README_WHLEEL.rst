GDAL/OGR in Python for Windows
================================

This binary Python package of GDAL_ is available for easy installation on Windows.

* Based on `Christoph Gohlke's GDAL wheels <https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal>`_
* Essentially a merge of his `GDAL‑3.X.Y‑cp3*‑cp3*‑[win32|win_amd64].whl`
  wheels to support multiple Python versions.
* Currently supports Python 3.7-3.9 on Windows 32bit and 64bit.
* gdalplugins
    * You may add gdalplugins by adding their respective DLL files to the `gdalplugins` subdir.
    * You may get plugin dlls from
      `gisinternals <https://download.gisinternals.com/sdk/downloads/release-1911-dev.zip>`_.
* Built with a custom `setup.py` file.