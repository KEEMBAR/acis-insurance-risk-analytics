import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "ACIS Insurance Risk Analytics"
copyright = "2025, 10 Academy"
author = "10 Academy"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
