import os
from pathlib import Path
from sphinx.util.docutils import ReferenceRole, nodes

from typing import Optional


class AnyLinkFile(ReferenceRole):
    def __init__(self, repo: str):
        self.repo = repo
        super().__init__()

    def run(self):

        try:
            refuri = self.build_uri()

            title = self.title

            title_elem = nodes.inline("", "", classes=["anylink-title"])

            if self.has_explicit_title:
                title_elem += nodes.inline(self.title, self.title)
            else:
                title = self.title
                parts = title.split("/")
                title_elem += nodes.inline("", parts[0])
                for part in parts[1:]:
                    title_elem += nodes.inline("", " ", classes=["anylink-hiddenws"])
                    title_elem += nodes.inline("", "/" + part)

            reference = nodes.inline(classes=["anylink-tooltip"])
            supscript = nodes.superscript()
            supscript += nodes.Text("(", "(")
            supscript += nodes.reference(
                "",
                self.config.anylink_open_text,
                internal=False,
                refuri=refuri,
                classes=["anylink-ref"],
            )
            supscript += nodes.Text(")", ")")
            reference += supscript
            # reference += nodes.inline(
            #     "", self.config.anylink_open_tooltip, classes=["anylink-tooltiptext"]
            # )

        except ValueError:
            msg = self.inliner.reporter.error(
                "Invalid AMMR link %s" % self.target, line=self.lineno
            )
            prb = self.inliner.problematic(self.rawtext, self.rawtext, msg)
            return [prb], [msg]

        return [title_elem, reference], []

    def build_uri(self):

        refuri = f"anylink://AnyFile?"
        refuri += f"repo={self.repo}&"
        ver = self.config.anylink_ams_version
        if ver:
            refuri += f"version={ver}&"
        refuri += f"file={self.target}"
        return refuri


from sphinx.util.fileutil import copy_asset


def copy_css(app, exc):
    cssfile = Path(__file__).with_name("anylink.css")
    copy_asset(str(cssfile), os.path.join(app.outdir, "_static"))


def setup(app):

    app.add_role("anylink-ammr", AnyLinkFile(repo="ammr"))
    app.add_config_value("anylink_ams_version", None, "env")
    app.add_config_value("anylink_open_text", "AnyBody", "env")
    app.add_config_value(
        "anylink_open_tooltip", "Open model in AnyBody.\n Requires AnyBody", "env"
    )

    app.connect("build-finished", copy_css)

    app.add_css_file("anylink.css")

    return {"parallel_read_safe": True, "parallel_write_safe": True}
