import os
import sys
import sphinx_rtd_theme  # noqa: F401
from time import strftime

sys.path.insert(0, os.path.abspath('../..'))

project = 'Pyrogram-Hosting'
copyright = '2020 - 2021, Sakty'
author = 'Sakty'

version = "0.17.1"
release = 'stable'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme"
]

master_doc = 'index'
autosummary_generate = True
napoleon_use_rtype = False
pygments_style = "monokai"
pagename = "Pyrogram-Hosting Documentation"
html_title = "Pyrogram-Hosting Documentation"
html_short_title = "Pyrogram-Hosting"
html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = False
html_theme = "sphinx_rtd_theme"
html_logo = "_images/logo.svg"
html_favicon = "_images/favicon.ico"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
templates_path = ['_templates']
html_static_path = ['_static']
show_authors = True


intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}

html_theme_options = {
    'canonical_url': 'heroku-pyrogram.readthedocs.io',
    'logo_only': False,
    'display_version': True,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'style_external_links': False,
    'style_nav_header_background': '#333FF0'
}

html_context = {
    # Our last updated format.
    'l_updated': strftime('%b %d, %Y'),
    # Enable the "Edit in GitHub link within the header of each page.
    'display_github': True,
    'github_user': 'pyrogram',
    'github_repo': 'pyrogram',
    'github_version': 'master',
    'conf_py_path': '/docs/source/'
}
