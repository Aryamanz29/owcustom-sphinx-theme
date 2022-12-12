owcustom sphinx theme
=====================

A `Sphinx theme`_ for OpenWISP docs, based on `Read The Docs`_
default theme (sphinx_rtd_theme_).

**Live demo:** https://owcustom-sphinx-theme.readthedocs.io/en/latest/

.. figure:: https://user-images.githubusercontent.com/56113566/206928233-e2ec9653-651c-4b63-95d4-d351aa5f674a.png
  :align: center


Installation
------------

This theme is distributed on PyPI as owcustom-sphinx-theme_ and can be
installed with ``pip``:

.. code:: console

    $ python3 -m pip install owcustom-sphinx-theme

To use the theme in your Sphinx project, you will need to add the following to
your ``conf.py`` file:

.. code:: python

    # add this extension 
    extensions = [...,
    'owcustom.sphinx.theme',
    ...
    ]
    html_theme = "owcustom-sphinx-theme"

Development
-----------

.. code:: bash

    python3 -m pip install -e .
    make clean # not always needed, but better to be cautious
    make html
    open build/html/index.html

Releasing
---------

1. Make sure all your changes have been commited to the ``main`` branch.
2. Add a commit which describes the changes from the previous version to ``CHANGES.rst`` and updates the version number in ``lib/owcustom/sphinx/theme/VERSION``.
3. Tag this commit with the version number, e.g. ``git tag -a 1.0.x -m "version 1.0.x"``.
4. Push the commit and tag to GitHub, e.g. ``git push origin main 1.0.x``.
5. Publish to PyPI by invoking a GitHub Actions workflow:

   1. Go to the workflow: `publish.yml <https://github.com/Aryamanz29/owcustom-sphinx-theme/actions/workflows/publish.yml>`_.
   2. Select **Run workflow**. In the new menu:

      1. Select **Use workflow from** > **Tags** > new version number (e.g. 2022.12).
      2. Set **PyPI instance for publishing** as *PyPI* (default) or *TestPyPI*. `More info <https://packaging.python.org/en/latest/guides/using-testpypi/>`_
      3. Select **Run workflow**.

.. _Sphinx theme: https://www.sphinx-doc.org/en/master/development/theming.html
.. _Read The Docs: https://readthedocs.org
.. _sphinx_rtd_theme: https://github.com/readthedocs/sphinx_rtd_theme
.. _owcustom-sphinx-theme: https://pypi.org/project/owcustom-sphinx-theme/
.. _configuration options: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
