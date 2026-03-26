# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lucrezio 4.0'
copyright = '2026, Antonio Vigilante'
author = 'Antonio Vigilante'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',   
]
myst_enable_extensions = [
    'colon_fence',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'it'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'library'
html_title = "De rerum natura"
html_static_path = ['_static']
html_logo = '_static/logo_botticelli.png'
html_theme_options = {
    "typography": "swiss-native",
    "extra_links": {
        "GitHub": "https://github.com/",
    }
    
     }


html_css_files = [
    'custom.css',
]

html_sidebars = {
    "**": [
        "about.html",         # Project name, description, etc.
        "globaltoc.html",     # Global table of contents. 
        "searchbox.html",     # Search.
        "extralinks.html",    # Links specified in theme options.
        #"localtoc.html",     # Contents of the current page.
        "sponsors.html",      # Fancy sponsor links.
    ]
}

# Footer personalizzato
html_show_sphinx = False  # Nasconde "Created using Sphinx"
html_show_copyright = False
copyright = 'Lucrezio 4.0 è un progetto di Antonio Vigilante rilasciato con licenza BB BY-SA 4.0'

# Aggiungere HTML personalizzato al footer
html_context = {
    'display_github': True,
    'github_user': 'tuousername',
    'github_repo': 'tuorepo',
    'github_version': 'main',
}

