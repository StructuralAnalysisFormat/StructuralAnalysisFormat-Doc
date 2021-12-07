import importlib

extensions = ['myst_parser']
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'SAF Documentation'

html_css_files = [
    'custom.css',
]

myst_enable_extensions = ['html_image', 'dollarmath']
