import os
from collections import defaultdict
from pathlib import Path
from typing import Optional

from sphinx.util.docutils import ReferenceRole, nodes


def create_trigger_node(obj):
    # Formatting of the anylink:// url is done in the javascript function when the pages loads
    # to ensure we can get the correct path to local repositories. See anylink.js 
    if obj.config.anylink_link_local_repo:
        repo_relative_path = obj.config.anylink_repo_relative_paths[obj.repo]
        if isinstance(repo_relative_path, tuple):
        # if it is a tuple use the second element for validating the target 
            repo_relative_path, repo_path = repo_relative_path
            if not Path(repo_path).joinpath(obj.target).exists():
                raise ValueError("Target file does not exists")
    else:
        repo_relative_path = ""
    javascript_fun = f"anylink_file(this, '{obj.config.anylink_ams_version}', '{obj.repo}', '{obj.target}', '{repo_relative_path}')"
    # The mall formed <img> element trigger the onerror js function which fills the 
    # href of the parent node (<a>), then it removes the <img> element
    return nodes.raw("", f'<img src onerror="{javascript_fun}"/>', format="html")



class AnyLinkButton(ReferenceRole):
    def __init__(self, repo: str):
        self.repo = repo
        super().__init__()

    def run(self):

        try:
            button = nodes.reference(
                "",
                self.config.anylink_open_text,
                internal=False,
                refuri="",
                classes=["anylink-ref", "sd-btn", "sd-text-wrap", "sd-m-2","sd-shadow-sm", "sd-align-major-center", "sd-btn-outline-primary", "reference", "external"],
                onerror="test"

            )
            button += create_trigger_node(self)

        except ValueError:
            msg = self.inliner.reporter.error(
                "Invalid AMMR link %s" % self.target, line=self.lineno
            )
            prb = self.inliner.problematic(self.rawtext, self.rawtext, msg)
            return [prb], [msg]

        return [button], []



class AnyLinkFile(ReferenceRole):
    def __init__(self, repo: str):
        self.repo = repo
        super().__init__()

    def run(self):

        try:

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
                onerror="test"

            )

            reference += create_trigger_node(self)

            # Wrap the link in super script
            supscript = nodes.superscript()
            supscript += nodes.Text("(", "(")
            supscript += reference
            supscript += nodes.Text(")", ")")

            # wrap the super script in <span> node with anylink-tooltip class
            ref_elem = nodes.inline(classes=["anylink-tooltip"])
            ref_elem += supscript

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

    
    app.add_role("anylink-button", AnyLinkButton(repo="ammr"))
    app.add_role("anylink-file", AnyLinkFile(repo="ammr"))
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
