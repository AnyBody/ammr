import os
from collections import defaultdict

from pathlib import Path
from sphinx.util.docutils import ReferenceRole, nodes

from typing import Optional


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

            # Formatting of the anylink:// url is done in the javascript function when the pages loads
            # to ensure we can get the correct path to local repositories. See anylink.js 
            if self.config.anylink_link_local_repo:
                repo_relative_path = self.config.anylink_repo_relative_paths[self.repo]
            else:
                repo_relative_path = ""
            javascript_fun = f"anylink_file(this, '{self.config.anylink_ams_version}', '{self.repo}', '{self.target}', '{repo_relative_path}')"
            # The mall formed <img> element trigger the onerror js function which fills the 
            # href of the parent node (<a>), then it removes the <img> element
            trigger_element = nodes.raw("", f'<img src onerror="{javascript_fun}"/>', format="html")
            reference += trigger_element

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


def setup(app):

    
    app.add_role("anylink-ammr", AnyLinkFile(repo="ammr"))
    app.add_config_value("anylink_ams_version", "", "env")
    app.add_config_value("anylink_open_text", "AnyBody", "env")
    app.add_config_value("anylink_repo_relative_paths", defaultdict(lambda: "../"), "env")
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
