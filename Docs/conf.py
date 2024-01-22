# -- Project information -----------------------------------------------------
import os
import sys
from urllib.request import urlopen
from pathlib import Path
import re
from datetime import datetime
import subprocess

sys.path.insert(0, os.path.abspath("exts"))
sys.path.insert(0, os.path.abspath("tools"))


current_year = os.environ.get("YEAR", datetime.now().year)


project = "AMMR"
copyright = f"{current_year}, AnyBody Technology"
author = "AnyBody Technology"
# language = "fr"  # For testing language translations


def tagged_commit():
    """Check if we are on a tagged commit"""
    try:
        subprocess.check_call(
            ["git", "describe", "--tags", "--exact-match", "HEAD"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return False
    else:
        return True


if tags.has("offline"):
    # building offline version
    pass


if not tagged_commit() and not tags.has("offline"):
    tags.add("draft")

# `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = tags.has("draft")


master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "myst_parser",
    "ammr_directives",
    "inline_highlight",
    "sphinxext.opengraph",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_copybutton",

    # "sphinxcontrib.youtube",
    # "sphinx_copybutton",
    # "sphinx_design",
    # "sphinx_examples",
    # "sphinx_tabs.tabs",
    # "sphinx_togglebutton",
    # "sphinxcontrib.bibtex",
    # "sphinxext.opengraph",
    # For the kitchen sink
    # "sphinx.ext.todo",
]


myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "dollarmath",
    "amsmath",
    "html_image",
    "substitution",
    "attrs_inline",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]


source_suffix = [".rst", ".md"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "README.md",
    "Thumbs.db",
    ".DS_Store",
    "exts",
    "auto_examples",
    ".pixi",
]

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = "AnyScriptDoc"
pygments_style = "AnyScript"

ams_version = os.environ.get("AMS_VERSION", "7.4.3")
if not re.match("^\d\.\d\.\d", ams_version):
    raise ValueError("Wrong format for AMS version, environment variable")
ams_version_short = ams_version.rpartition(".")[0]
ams_version_x = ams_version_short + ".x"


ammr_version = os.environ.get("AMMR_VERSION", None)
if ammr_version is None:
    AMMR_VERSION_RE = re.compile(r'.*AMMR_VERSION\s"(?P<version>.*)"')
    with open("../AMMR.version.any") as fh:
        match = AMMR_VERSION_RE.search(fh.read())
        if match:
            ammr_version = match.groupdict()["version"]
        else:
            raise Exception("Could not parse AMMR version")


if not re.match("^\d\.\d\.\d", ammr_version):
    raise ValueError("Wrong format for AMMR version, environment variable")

ammr_version_short = ammr_version.rpartition(".")[0]

rst_epilog = f"""

.. |AMS| replace:: AnyBody Modeling System™
.. |AMS_VERSION_X| replace:: {ams_version_x}
.. |AMS_VERSION| replace:: {ams_version}
.. |AMS_VERSION_SHORT| replace:: {ams_version_short}
.. |AMMR_VERSION_SHORT| replace:: {ammr_version_short}
.. |AMMR_VERSION| replace:: {ammr_version}
.. |AMMR_DEMO_INST_DIR| replace:: :literal:`~/Documents/{ams_version_x}/AMMR.v{ammr_version}-Demo`
.. |CURRENT_YEAR| replace:: {current_year}
.. |WHAT_IS_NEW| replace:: :ref:`What's new in AMMR {ammr_version} <whats-new>`
.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1250764.svg
                 :target: https://doi.org/10.5281/zenodo.1250764
"""

myst_substitutions = {
    "AMS": "AnyBody Modeling System™",
    "AMS_VERSION_X": ams_version_x,
    "AMS_VERSION": ams_version_x,
    "AMS_VERSION_SHORT": ams_version_short,
    "AMMR_VERSION_SHORT": ams_version_short,
    "AMMR_VERSION": ammr_version,
    "CURRENT_YEAR": current_year,
    "AMMR_DEMO_INST_DIR": f"`~/Documents/{ams_version_x}/AMMR.v{ammr_version}-Demo`",
    "DOI": "[![DOI image](https://zenodo.org/badge/DOI/10.5281/zenodo.1250764.svg)](https://doi.org/10.5281/zenodo.1250764)",
    "WHAT_IS_NEW": f"{{ref}}`What's new in AMMR {ammr_version} <whats-new>`",
    "WHAT_IS_NEW2": f"{{material-outlined}}`update;1em` New in AMMR {ammr_version}",
}


no_index = """
.. meta::
   :robots: noindex
"""
myst_html_meta = {}

if tags.has("draft"):
    rst_epilog = rst_epilog + no_index
    myst_html_meta["robots"] = "noindex"

github_doc_root = "https://github.com/AnyBody/ammr/tree/master/Docs"

version = f"{ammr_version_short}"
# The full version, including alpha/beta/rc tags.
release = f"{ammr_version}"

if tags.has("draft") and not release.endswith("beta"):
    release = release + "-beta"





# suppress_warnings = ["myst.domains", "ref.ref"]

numfig = True



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
# html_logo = "_static/logo-wide.svg"
html_title = f"{project} v{release} Documentation"
html_copy_source = False
# html_favicon = "_static/logo-square.svg"
html_last_updated_fmt = ""

# html_sidebars = {
#     "reference/blog/*": [
#         "navbar-logo.html",
#         "search-field.html",
#         "ablog/postcard.html",
#         "ablog/recentposts.html",
#         "ablog/tagcloud.html",
#         "ablog/categories.html",
#         "ablog/archives.html",
#         "sbt-sidebar-nav.html",
#     ]
# }
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "body/_static"]
html_css_files = ["_static/custom.css"]


html_logo = "_static/AMMR.svg"
html_favicon = "_static/favicon.ico"


html_theme_options = {
    "path_to_docs": "Docs",
    "repository_url": "https://github.com/anybody/ammr",
    "repository_branch": "master",
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_issues_button": False,
    "use_repository_button": True,
    "use_download_button": False,

    "home_page_in_toc": False,
    "show_toc_level": 1,

    "pygment_light_style": "AnyScript",
    "pygment_dark_style": "stata-dark",


    # "use_sidenotes": True,
    # "announcement": (
    #     "⚠️The latest release refactored our HTML, "
    #     "so double-check your custom CSS rules!⚠️"
    # ),
    "logo": {
        "image_dark": "_static/AMMR.svg",
        # "text": html_title,  # Uncomment to try text with logo
    },
    "icon_links": [
        # {
        #     "name": "AnyBody Technology",
        #     "url": "https://anybodytech.com/",
        #     # "icon": "_static/ebp-logo.png",
        #     "type": "local",
        # },
        # {
        #     "name": "GitHub",
        #     "url": "https://github.com/anybody/ammr",
        #     "icon": "fa-brands fa-github",
        # },
    ],
    # For testing
    # "use_fullscreen_button": False,
    # "home_page_in_toc": True,
    # "extra_footer": "<a href='https://google.com'>Test</a>",  # DEPRECATED KEY
    # "show_navbar_depth": 2,
    # Testing layout areas
    # "navbar_start": ["test.html"],
    # "navbar_center": ["test.html"],
    # "navbar_end": ["test.html"],
    # "navbar_persistent": ["test.html"],
    # "footer_start": ["test.html"],
    # "footer_end": ["test.html"]
}

bibtex_bibfiles = ["references.bib"]
# To test that style looks good with common bibtex config
bibtex_reference_style = "author_year"
bibtex_default_style = "plain"
numpydoc_show_class_members = False  # for automodule:: urllib.parse stub file issue
linkcheck_ignore = [
    "http://someurl/release",  # This is a fake link
    "https://doi.org",  # These don't resolve properly and cause SSL issues
]



intersphinx_mapping = {}
if tags.has("offline"):
    # Todo. Find a way to link to offline html versions.
    intersphinx_mapping["tutorials"] = ("https://anyscript.org/tutorials/", None)
else:
    if tags.has("draft"):
        intersphinx_mapping["tutorials"] = (
            "https://anyscript.org/tutorials/beta/",
            None,
        )
    else:
        intersphinx_mapping["tutorials"] = ("https://anyscript.org/tutorials/", None)



# sphinxext.opengraph
# ogp_social_cards = {
#     "image": "_static/logo-square.png",
# }

ogp_site_url = "https://anyscript.org/"
ogp_site_name = "AMMR Documentation"
ogp_image = "https://anyscript.org/ammr/_static/AMMR_Logo.png"
ogp_use_first_image = True  # if not found defaults to 'ogp_image'


# Generate gallery files
import jinja2
import frontmatter

gallery = {}
galleryfolders = [x for x in Path("Applications").iterdir() if x.is_dir()]
for folder in galleryfolders:
    gallery[folder] = []
    for file in sorted(folder.glob("*.md"), key=lambda x: x.name.upper()):
        post = frontmatter.load(file)
        if "gallery_title" in post:
            gallery[folder].append(
                {
                    "doc": file.with_suffix("").as_posix(),
                    "title": post["gallery_title"],
                    "image": post["gallery_image"],
                }
            )


with open("Applications/gallery.txt.jinja2") as fh:
    gallery_template = jinja2.Template(fh.read())

for folder, section in gallery.items():
    gallery_txt = folder / "gallery.txt"
    content = gallery_template.render(examples=section)
    with open(gallery_txt, encoding="utf8") as fh:
        previous_content = fh.read()
    if content != previous_content:
        with open(gallery_txt, "w", encoding="utf8") as fh:
            fh.write(content)

# Run the python file "tools/generate_class_template_docs.py"
# to generate the class template documentation

import generate_class_template_docs
generate_class_template_docs.run_all()


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

linkcheck_ignore = [
    r".*linkcheck_ignore",
    "https://doi.org/10.1115/1.4037100",  # asme.org prevents the linkcheck
    "https://doi.org/10.1115/1.4052115",  # asme.org prevents the linkcheck
    "https://dx.doi.org/10.1115/1.4001678",  # asme.org prevents the linkcheck
    "https://dx.doi.org/10.1115/1.4029258",  # asme.org prevents the linkcheck
    "https://doi.org/10.1080/10255842.2020.1851367",  # tandfonline.com prevents the linkcheck
    "https://dx.doi.org/10.1002/jor.20255",  # wiley.com prevents the linkcheck
    "https://doi.org/10.1016/j.clinbiomech.2006.10.003",  # clinbiomech.com prevents the linkcheck
    "https://doi.org/10.1002/jor.25267", # wiley.com prevents the linkcheck
    "https://doi.org/10.5281/zenodo.10527958",  # AMMR 3 not released yet
    "https://www.anybodytech.com/download/anybodysetup-8-0-0-.*_x64/",  # AMMR 8 not released yet
]

linkcheck_allowed_redirects = {
    "https://doi.org.*": ".*",
    "https://dx.doi.org.*": ".*",
    "https://www.anybodytech.com/download/anybodysetup.*": ".*",
}

def setup(app):
   ...