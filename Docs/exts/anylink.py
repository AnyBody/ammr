import os
from collections import defaultdict
from pathlib import Path
from typing import Optional, cast

import docutils
from myst_parser.config.main import read_topmatter
from myst_parser.mdit_to_docutils.html_to_nodes import html_to_nodes
from myst_parser.mocking import MockState
from sphinx.util.docutils import ReferenceRole, SphinxDirective, nodes

BASE_BUTTON_CLASSES  = ["anylink-on-top", "anylink-ref", "sd-btn", "sd-text-wrap", "sd-m-2","sd-shadow-sm", "sd-align-major-center", "sd-btn-outline-primary", "reference", "external"]


import debugpy

# 5678 is the default attach port in the VS Code debug configurations. Unless a host and port are specified, host defaults to 127.0.0.1
# debugpy.listen(5678)
# print('Waiting for debugger attach')
# debugpy.wait_for_client()

def get_topmatter(obj): 
    return read_topmatter(Path(obj.get_source_info()[0]).read_text(encoding="utf-8"))

def create_trigger_node(obj, target):
    # Formatting of the anylink:// url is done in the javascript function when the pages loads
    # to ensure we can get the correct path to local repositories. See anylink.js 
    if obj.config.anylink_link_local_repo:
        repo_relative_path = obj.config.anylink_repo_relative_paths["ammr"]
        if isinstance(repo_relative_path, tuple):
        # if it is a tuple use the second element for validating the target 
            repo_relative_path, repo_path = repo_relative_path
            if not Path(repo_path).joinpath(obj.target).exists():
                raise ValueError("Target file does not exists")
    else:
        repo_relative_path = ""
    javascript_fun = f"anylink_file(this, '{obj.config.anylink_ams_version}', 'ammr', '{target}', '{repo_relative_path}')"
    # The mall formed <img> element trigger the onerror js function which fills the 
    # href of the parent node (<a>), then it removes the <img> element
    return nodes.raw("", f'<img src onerror="{javascript_fun}" alt="" aria-hidden="true" width="0" height="0" /> ', format="html")


class AnyLinkGallerySidebar(SphinxDirective): 

    required_arguments = 0
    has_content = True

    option_spec = {
        "link-classes": docutils.parsers.rst.directives.unchanged,
        "margin": docutils.parsers.rst.directives.flag,
        "anylink": docutils.parsers.rst.directives.unchanged,
        "title": docutils.parsers.rst.directives.unchanged,
        "image": docutils.parsers.rst.directives.unchanged,
        "style": docutils.parsers.rst.directives.unchanged, # button or gallery
    }

    def run(self):

        topmatter = get_topmatter(self)
        top_classes = ["sd-text-center"]

        if "margin" in self.options:
            top_classes.append("margin")

        elements = nodes.container(
            classes=top_classes
        )

        image = self.options.get("image") or topmatter.get("gallery_image", "")

        img = html_to_nodes( f'<img src="{image}" align="center" width= "100%"/>', self.lineno, self.state._renderer)
        elements += img


        if self.content:
            content_nodes = self.parse_inline(self.content[0], lineno=self.lineno+self.content_offset)[0]
        else:
            open_text = self.config.anylink_open_text
            content_nodes = nodes.inline(open_text, open_text)
            #content_nodes = nodes.paragraph(text= self.config.anylink_open_text).children


        style_option = self.options.get("style", "button")
        if style_option == "button": 
            ref_classes = BASE_BUTTON_CLASSES
        elif style_option == "gallery":
            ref_classes = ["anylink-on-top", "anylink-ref", "reference", "external"]

        open_ref = nodes.reference(
            "",
            "",
            internal=False,
            refuri="",
            classes=ref_classes,
        )
        open_ref.children.extend(content_nodes)

        anylink = self.options.get("anylink") or topmatter.get("anylink", "")
        open_ref.children.append(create_trigger_node(self, anylink))

        link_p = nodes.paragraph()
        link_p.append(open_ref)

        link_classes = self.options.get("link-classes", "").split(" ")
        link_div = nodes.container("", link_p, classes=link_classes)

        #paragraph += open_ref #(nodes.container(classes=["sd-text-right"]) + open_ref)
        elements += link_div

        return [elements]

class AnyLinkButton(ReferenceRole):

    def run(self):


        if self.target == " ":
            topmatter = get_topmatter(self)
            self.target = topmatter.get("anylink", "")
            self.title = self.target

        try:
            button = nodes.reference(
                "",
                self.config.anylink_open_text,
                internal=False,
                refuri="",
                classes=BASE_BUTTON_CLASSES,
            )
            button += create_trigger_node(self, self.target)

        except ValueError:
            msg = self.inliner.reporter.error(
                "Invalid AMMR link %s" % self.target, line=self.lineno
            )
            prb = self.inliner.problematic(self.rawtext, self.rawtext, msg)
            return [prb], [msg]

        return [button], []





class AnyLink(ReferenceRole):

    def run(self):


        reference = nodes.reference(
            "",
            self.title,
            internal=False,
            refuri="",
            classes=["anylink-on-top"]
        )
        reference += create_trigger_node(self, self.target) 

        return [reference], []


class AnyLinkFile(ReferenceRole):

    def run(self):


        try:

            if self.target == " ":
                topmatter = get_topmatter(self)
                self.target = topmatter.get("anylink", "")
                self.title = self.target

            title_elem = nodes.inline("", "", classes=["anylink-title"])

            if self.has_explicit_title:
                title_elem += nodes.inline(self.title, self.title)
            else:
                # We split the file name in parts and assemble it again with
                # hidden whitespaces between. This ensures that it wraps nicely 
                # with narrow browser windows
                title = self.title
                parts = title.split("/")
                title_elem += nodes.inline("", parts[0])
                for part in parts[1:]:
                    title_elem += nodes.inline("", " ", classes=["anylink-hiddenws"])
                    title_elem += nodes.inline("", "/" + part)


            reference = nodes.reference(
                "",
                self.config.anylink_open_text,
                internal=False,
                refuri="",
                classes=["anylink-ref"],
            )

            reference += create_trigger_node(self, self.target)

            # Wrap the link in super script
            superscript = nodes.superscript()
            superscript += nodes.Text("(", "(")
            superscript += reference
            superscript += nodes.Text(")", ")")

            # wrap the super script in <span> node with anylink-tooltip class
            ref_elem = nodes.inline(classes=["anylink-tooltip"])
            ref_elem += superscript

        except ValueError:
            msg = self.inliner.reporter.error(
                "Invalid AMMR link %s" % self.target, line=self.lineno
            )
            prb = self.inliner.problematic(self.rawtext, self.rawtext, msg)
            return [prb], [msg]

        return [title_elem, ref_elem], []




from sphinx.util.fileutil import copy_asset


def copy_assets(asset_files):

    def copy_files(app, exc):
        for asset in asset_files:
            fn = Path(__file__).with_name(asset)
            copy_asset(str(fn), os.path.join(app.outdir, "_static"))
    
    return copy_files

def tmp():
    return "../"

relative_path_dict = defaultdict(tmp)


def setup(app):

    
    app.add_role("anylink-button", AnyLinkButton())
    app.add_role("anylink-file", AnyLinkFile())
    app.add_role("anylink", AnyLink())
    app.add_directive("anylink-gallery", AnyLinkGallerySidebar)
    app.add_config_value("anylink_ams_version", "", "env")
    app.add_config_value("anylink_open_text", "AnyBody", "env")


    app.add_config_value("anylink_repo_relative_paths", relative_path_dict, "env")
    app.add_config_value(
        "anylink_open_tooltip", "Open model in AnyBody.\n Requires AnyBody", "env"
    )
    app.add_config_value("anylink_link_local_repo", True, "env")

    # Add js and css files to sphinx
    css_files = ["anylink.css"]
    js_files = ["anylink.js", "anylink-npm-path.js"]
    app.connect("build-finished", copy_assets(css_files+js_files))

    for fn in css_files:
        app.add_css_file(fn)
    for fn in js_files:
        app.add_js_file(fn)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
