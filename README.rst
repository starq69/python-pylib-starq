========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-pylib-starq/badge/?style=flat
    :target: https://readthedocs.org/projects/python-pylib-starq
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/pylib-starq.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pylib-starq

.. |commits-since| image:: https://img.shields.io/github/commits-since/starq69/python-pylib-starq/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/starq69/python-pylib-starq/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pylib-starq.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pylib-starq

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pylib-starq.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pylib-starq

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pylib-starq.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pylib-starq


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT license

Installation
============

::

    pip install pylib-starq

Documentation
=============

https://python-pylib-starq.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
