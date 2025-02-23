"""The Sphinx documentation toolchain."""

# Keep this file executable as-is in Python 3!
# (Otherwise getting the version out of it when packaging is impossible.)

from __future__ import annotations

import warnings

from sphinx.util._pathlib import _StrPath

__version__ = '8.3.0'
__display_version__ = __version__  # used for command line version

warnings.filterwarnings(
    'ignore',
    'The frontend.Option class .*',
    DeprecationWarning,
    module='docutils.frontend',
)

#: Version info for better programmatic use.
#:
#: A tuple of five elements; for Sphinx version 1.2.1 beta 3 this would be
#: ``(1, 2, 1, 'beta', 3)``. The fourth element can be one of: ``alpha``,
#: ``beta``, ``rc``, ``final``. ``final`` always has 0 as the last element.
#:
#: .. versionadded:: 1.2
#:    Before version 1.2, check the string ``sphinx.__version__``.
version_info = (8, 3, 0, 'final', 0)

package_dir = _StrPath(__file__).resolve().parent

_in_development = True
if _in_development:
    # Only import subprocess if needed
    import subprocess

    try:
        if ret := subprocess.run(
            ('git', 'rev-parse', '--short', 'HEAD'),
            cwd=package_dir,
            check=False,
            encoding='utf-8',
            errors='surrogateescape',
            stdout=True,
        ).stdout:
            __display_version__ += f'+/{ret.strip()}'
        del ret
    finally:
        del subprocess
del _in_development
