Namespace Package Test
======================

This is a test repository to test creating namespace packages.

Under src there are two distributions for packages which represent
subpackages of a package named ``silly_walking``. You can install the
distributions separately, but imports are made using the same top-level
namespace package:

::

    pip install silly-walking-client silly-walking-api-v1

|

Package silly-walking-client has a dependency for silly-walking-api-v1, so that will
actually be installed without specifying it explicitly.

To import:

::

    from silly_walking.client import Client
    from silly_walking.api_v1 import APIv1

|

To be able to find imports when developing, you must add all the namespace
packages into your PYTHONPATH:

::

    PYTHONPATH=<path-here>/src/silly-walking-client:<path-here>/src/silly-walking-api-v1

|


Mypy issue
----------

Namespace packages are not supported by mypy without the
``--namespace-packages`` command line argument or a
``namespace_packages = True`` congfiguration option. This is
likely to change as the default in the future:

https://github.com/python/mypy/issues/8584

