import importlib

extensions = ['myst_parser']
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'gitbookdocumentation'

theme = importlib.import_module('sphinx_rtd_theme')
html_theme = 'sphinx_rtd_theme'
html_style = None
html_theme_options = {'body_max_width': '100%'}
html_theme_path = [theme.get_html_theme_path()]
