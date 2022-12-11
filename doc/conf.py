import os
import sys
sys.path.append(os.path.abspath("./demo/"))
from owcustom.sphinx.theme import __version__ as theme_version

project = 'owcustom docs theme'
version = theme_version
author = 'owcustom'
extensions = [
    'sphinx.ext.autodoc',
    'owcustom.sphinx.theme',
]

# OpenWISP demo site configuration
from datetime import date
project = 'OpenWISP'
copyright = f'2017-{date.today().year}, OpenWISP'
author = 'OpenWISP Community'
exclude_patterns = []
templates_path = ['templates']
html_theme = 'owcustom-sphinx-theme'
html_logo = 'demo/assets/design/openwisp-logo-black.svg'
html_favicon = 'demo/assets/design/favicon.png'
html_favicon = 'demo/assets/design/favicon.png'
