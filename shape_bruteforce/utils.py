import pathlib
import re
from setuptools.extern import packaging


def get_version():
    """Version info, read without importing"""
    path = (pathlib.Path(__file__).parent / "__init__.py").absolute()
    with open(path, "rt", encoding="utf8") as f:
        version_re = re.search(r"__version__ = \"(.*?)\"", f.read())
        if version_re:
            version = version_re.group(1)
        else:
            raise ValueError("Could not determine package version")
        # Normalize version so `setup.py --version` show same version as twine.
        version = str(packaging.version.Version(version))

    return version
