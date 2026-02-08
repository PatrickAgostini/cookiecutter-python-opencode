# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{ cookiecutter.project_name }}"
copyright = "2024, {{ cookiecutter.author_name }}"
author = "{{ cookiecutter.author_name }}"
release = "0.1.0"

# -- General configuration ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Theme configuration based on cookiecutter choice
{% if cookiecutter.sphinx_theme == "shibuya" %}
html_theme = "shibuya"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0066cc",
        "color-brand-content": "#004499",
    },
    "dark_css_variables": {
        "color-brand-primary": "#3399ff",
        "color-brand-content": "#66aaff",
    },
}
{% elif cookiecutter.sphinx_theme == "furo" %}
html_theme = "furo"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0066cc",
        "color-brand-content": "#004499",
    },
}
{% elif cookiecutter.sphinx_theme == "pydata_sphinx_theme" %}
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.project_slug }}",
    "show_prev_next": False,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
}
{% elif cookiecutter.sphinx_theme == "sphinx_rtd_theme" %}
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False
}
{% elif cookiecutter.sphinx_theme == "sphinx_book_theme" %}
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.project_slug }}",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 4,
    "show_toc_level": 2,
    "toc_title": "Contents",
}
{% elif cookiecutter.sphinx_theme == "sphinx_immaterial" %}
html_theme = "sphinx_immaterial"
html_theme_options = {
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/brightness-7",
                "name": "Switch to dark mode"
            }
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/brightness-4",
                "name": "Switch to light mode"
            }
        }
    ],
    "font": {
        "text": "Roboto",
        "code": "Roboto Mono"
    },
    "features": ["navigation.tabs", "navigation.top", "search.highlight"]
}
{% elif cookiecutter.sphinx_theme == "alabaster" %}
html_theme = "alabaster"
html_theme_options = {
    "page_width": "1200px",
    "sidebar_width": "300px",
    "body_min_width": "450px",
    "show_related": True,
    "description": "Documentation for {{ cookiecutter.project_name }}",
    "logo": "",
    "logo_name": True,
    "github_button": False,
    "github_count": False,
    "travis_button": False,
    "codecov_button": False
}
{% elif cookiecutter.sphinx_theme == "sphinxawesome_theme" %}
html_theme = "sphinxawesome_theme"
html_theme_options = {
    "awesome_headerlogo": "",
    "awesome_external_links": [
        {"name": "GitHub", "url": "https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.project_slug }}"}
    ]
}
{% elif cookiecutter.sphinx_theme == "piccolo_theme" %}
html_theme = "piccolo_theme"
html_theme_options = {
    "light_theme": True,
    "show_toc_levels": 2
}
{% elif cookiecutter.sphinx_theme == "sphinx_press_theme" %}
html_theme = "press"
html_theme_options = {
    "custom_css": [],
    "custom_js": []
}
{% else %}
html_theme = "default"
{% endif %}

html_static_path = ["_static"]

# -- Extension configuration -------------------------------------------------

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__"
}

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# Todo extension settings
todo_include_todos = True
