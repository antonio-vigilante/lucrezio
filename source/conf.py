# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DRM'
copyright = '2026, Lucrezio'
author = 'Lucrezio'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',   
]

myst_enable_extensions = [
    "colon_fence",  # Abilita la sintassi :::
]

templates_path = ['_templates']
exclude_patterns = []

language = 'it'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'library'
html_static_path = ['_static']
html_title = "DRM"

html_sidebars = {
    "**": [
        "about.html",         # Project name, description, etc.
        "globaltoc.html",     # Global table of contents. 
        "searchbox.html",     # Search.
        "extralinks.html",    # Links specified in theme options.
        #"localtoc.html",     # Contents of the current page.
        "readingmodes.html",  # Light/sepia/dark color schemes.
        "sponsors.html",      # Fancy sponsor links.
    ]
}

html_theme_options = {
    "typography": "academy-native",
}
