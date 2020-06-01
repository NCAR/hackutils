.. image:: https://img.shields.io/github/workflow/status/NCAR/hackutils/CI?logo=github&style=for-the-badge
    :target: https://github.com/NCAR/hackutils/actions
    :alt: GitHub Workflow CI Status

.. image:: https://img.shields.io/github/workflow/status/NCAR/hackutils/code-style?label=Code%20Style&style=for-the-badge
    :target: https://github.com/NCAR/hackutils/actions
    :alt: GitHub Workflow Code Style Status

.. image:: https://img.shields.io/codecov/c/github/NCAR/hackutils.svg?style=for-the-badge
    :target: https://codecov.io/gh/NCAR/hackutils

hackutils
=========

Development
------------

For a development install, do the following in the repository directory:

.. code-block:: bash

    conda env update -f ci/environment.yml
    conda activate sandbox-devel
    python -m pip install -e .
