# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'psdemo'
copyright = '© 2019 by Pulse Secure, LLC. All rights reserved'
author = 'Shaloo Shalini'

# The full version, including alpha/beta/rc tags
release = '1.0'

version = u' '+release+u' (alpha) ' 
master_doc='index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx.ext.autodoc',
    'sphinx.ext.ifconfig',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinxcontrib.swaggerdoc',
    'sphinxcontrib.spelling',
    'sphinx.ext.githubpages'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_logo = '_static/psdemo_logo.png'
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
        'display_version': True,
}
#custom css and theme overrides

def setup(app):
    app.add_stylesheet('theme_overrides.css')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']

# Product Name variable

new_product_name = 'PSDemoNew'

rst_epilog = """
.. |Product_name| replace:: %(new_product_name)s
""" % { "new_product_name": new_product_name ,
}
