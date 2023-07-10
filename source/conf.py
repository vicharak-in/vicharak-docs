# Copyright (c) 2023 Vicharak Computers LLP
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.

import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath("_themes"))

# General information about the project.
project = "Vicharak"
author = "Vicharak Computers LLP"
copyright = f"{date.today().year}, {author}"
version = "0.1"

# Extensions
extensions = [
    "breathe",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_favicon",
    "sphinx_tabs.tabs",
    "sphinx_togglebutton",
    "sphinxawesome_theme",
]

# Enable colon fence for code blocks
myst_enable_extensions = [
    "attrs_block",
    # Enable inline attribute parsing
    "attrs_inline",
    # Enable code fences using ::: delimiters
    "colon_fence",
    # Enable definition lists
    "deflist",
    # Enable linkify extension
    "linkify",
    # Automatically convert standard quotations
    # to their opening/closing variants
    "smartquotes",
    # Enable strikethrough
    "strikethrough",
    # Add check-boxes to the start of list items
    "tasklist",
]

# Enable MyST implicit header references
myst_heading_anchors = 4

# Convert MyST titles to header
myst_title_to_header = True

suppress_warnings = ["myst.header", "myst.xref_missing"]

# Source file parsers
source_suffix = [".rst", ".md"]

# Set templates and exclude patterns
templates_path = ["_templates"]
exclude_patterns = ["_build"]

# HTML settings
html_theme = "sphinxawesome_theme"
html_static_path = ["_static"]
html_title = "Vicharak"
# CSS files to include
html_css_files = [
    "css/custom.css",
]
# Theme options
html_theme_options = {
    # sphinxawesome_theme options
    "logo_light": "_static/images/vicharak-logo-light.svg",
    "logo_dark": "_static/images/vicharak-logo-dark.svg",
    "show_breadcrumbs": True,
}
# HTML favicon
html_favicon = "_static/images/favicon.ico"

favicons = [
    "images/android-chrome-192x192.png",
    "images/android-chrome-512x512.png",
    "images/apple-touch-icon.png",
    "images/favicon-16x16.png",
    "images/favicon-32x32.png",
    "images/favicon.ico",
    "images/mstile-150x150.png",
    "images/safari-pinned-tab.svg",
]

# Breathe extension settings
breathe_projects = {"drm_fpga_write": os.getcwd() + "/../xml/"}
breathe_default_project = "drm_fpga_write"
