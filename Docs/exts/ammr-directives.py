# -*- coding: utf-8 -*-
#
#
#  Based on Sphinx Domain specification from the Apache Traffic
#  Server project. See:
#  https://docs.trafficserver.apache.org/en/latest/developer-guide/documentation/adding-domains.en.html
#
#    :copyright: Copyright 2013 by the Apache Software Foundation
#    :license: Apache
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
    TS Sphinx Directives
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Sphinx Docs directives for Apache Traffic Server

    :copyright: Copyright 2017 AnyBodyTechnology
    :license: Apache
"""
import subprocess
import re
import os

from docutils import nodes
from docutils.parsers import rst
from docutils.parsers.rst import directives
from sphinx.domains import Domain, ObjType, std
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
import sphinx




class AMMR_BMStatement(std.Target):
    """
    Description of a AMMR Body Model Statements.

    Required argument is: Variable name

    Options supported are:

        :deprecated: - A simple flag option indicating whether the variable
        is slated for removal in future releases.

        :default: - A string representing the default value
        :options: - A list of possible values 
        :type: - A string witht defines which can be set. 
    """

    option_spec = {
        "deprecated": rst.directives.flag,
        "default": rst.directives.unchanged,
        "type": rst.directives.unchanged,
        "noindex": rst.directives.flag,
    }

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True

    def make_field(self, tag, value):
        field = nodes.field()
        field.append(nodes.field_name(text=tag))
        body = nodes.field_body()
        if isinstance(value, str):
            body.append(sphinx.addnodes.compact_paragraph(text=value))
        else:
            body.append(value)
        field.append(body)
        return field

    def run(self):
        env = self.state.document.settings.env
        var_name = self.arguments[0]

        # Create a documentation node to use as the parent.
        node = sphinx.addnodes.desc()
        node.document = self.state.document
        node["objtype"] = "bm_statement"
        node.set_class("section")

        # Add the signature child node for permalinks.
        title = sphinx.addnodes.desc_signature(var_name, "")
        title["ids"].append(nodes.make_id(var_name))
        title["ids"].append(var_name)
        title["names"].append(var_name)
        title["first"] = False
        title["objtype"] = node["objtype"]
        self.add_name(title)
        title.set_class("ammr-bm_statement-title")

        title += sphinx.addnodes.desc_name(var_name, var_name)
        node.append(title)

        # This has to be a distinct node before the title. if nested then
        # the browser will scroll forward to just past the title.
        anchor = nodes.target("", "", names=[var_name])
        # Second (optional) arg is 'msgNode' - no idea what I should pass for that
        # or if it even matters, although I now think it should not be used.
        self.state.document.note_explicit_target(title)

        env.domaindata["ammr"]["bm_statement"][var_name] = env.docname

        # Create table detailing all provided domain options
        fl = nodes.field_list()
        if "deprecated" in self.options:
            fl.append(self.make_field("Deprecated", "Yes"))

        # Parse any associated block content for the item's description
        nn = nodes.compound()
        self.state.nested_parse(self.content, self.content_offset, nn)

        # Create an index node so Sphinx will list this variable and its
        # references in the index section.
        indexnode = sphinx.addnodes.index(entries=[])
        indexnode["entries"].append(
            ("single", _("%s") % var_name, nodes.make_id(var_name), "", None)
        )

        rtn = []
        if "noindex" not in self.options:
            rtn.append(indexnode)
        rtn.append(node)
        if len(fl):
            rtn.append(fl)
        rtn.append(nn)

        return rtn


class AMMR_BMStatementRef(XRefRole):
    def process_link(self, env, ref_node, explicit_title_p, title, target):
        return title, target


class AMMR_BMConstant(std.Target):
    """
    Description of a AMMR Body Model Constants.

    Required argument is: Constant name

    Options supported are:

        :deprecated: - A simple flag option indicating whether the variable
        is slated for removal in future releases.

        :value: - A string descripting the values of the constant
    """

    option_spec = {
        "deprecated": rst.directives.flag,
        "value": rst.directives.unchanged,
        "noindex": rst.directives.flag,
    }

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = True

    def make_field(self, tag, value):
        field = nodes.field()
        field.append(nodes.field_name(text=tag))
        body = nodes.field_body()
        if isinstance(value, str):
            body.append(sphinx.addnodes.compact_paragraph(text=value))
        else:
            body.append(value)
        field.append(body)
        return field

    def run(self):
        env = self.state.document.settings.env
        var_name = self.arguments[0]

        # Create a documentation node to use as the parent.
        node = sphinx.addnodes.desc()
        node.document = self.state.document
        node["objtype"] = "bm_constant"
        node.set_class("section")

        # Add the signature child node for permalinks.
        title = sphinx.addnodes.desc_signature(var_name, "")
        title["ids"].append(nodes.make_id(var_name))
        title["ids"].append(var_name)
        title["names"].append(var_name)
        title["first"] = False
        title["objtype"] = node["objtype"]
        self.add_name(title)
        title.set_class("ammr-bm_constant-title")

        title += sphinx.addnodes.desc_name(var_name, var_name)
        node.append(title)

        # This has to be a distinct node before the title. if nested then
        # the browser will scroll forward to just past the title.
        anchor = nodes.target("", "", names=[var_name])
        # Second (optional) arg is 'msgNode' - no idea what I should pass for that
        # or if it even matters, although I now think it should not be used.
        self.state.document.note_explicit_target(title)

        env.domaindata["ammr"]["bm_constant"][var_name] = env.docname

        # Create table detailing all provided domain options
        fl = nodes.field_list()

        if "deprecated" in self.options:
            fl.append(self.make_field("Deprecated", "Yes"))

        if "value" in self.options:
            fl.append(self.make_field("Value", self.options["value"]))

        # Parse any associated block content for the item's description
        nn = nodes.compound()
        self.state.nested_parse(self.content, self.content_offset, nn)

        # Create an index node so Sphinx will list this variable and its
        # references in the index section.
        indexnode = sphinx.addnodes.index(entries=[])
        indexnode["entries"].append(
            ("single", _("%s") % var_name, nodes.make_id(var_name), "", None)
        )

        rtn = []
        if "noindex" not in self.options:
            rtn.append(indexnode)
        rtn.extend([node, fl, nn])

        return rtn


class AMMR_BMConstantRef(XRefRole):
    def process_link(self, env, ref_node, explicit_title_p, title, target):
        return title, target


class AMMRDomain(Domain):
    """
    AMMR Documentation.
    """

    name = "ammr"
    label = "AMMR"
    data_version = 2

    object_types = {
        "bm_statement": ObjType(l_("Body Model Statement"), "bm_statement"),
        "bm_constant": ObjType(l_("Body Model Constant"), "bm_constant"),
    }

    directives = {"bm_statement": AMMR_BMStatement, "bm_constant": AMMR_BMConstant}

    roles = {"bm_statement": AMMR_BMStatementRef(), "bm_constant": AMMR_BMConstantRef()}

    initial_data = {"bm_statement": {}, "bm_constant": {}}  # full name -> docname

    dangling_warnings = {
        "bm_statement": "No definition found for Body Model statement '%(target)s'",
        "bm_constant": "No definition found for Body Model constant '%(target)s'",
    }

    def clear_doc(self, docname):
        bm_statement_list = self.data["bm_statement"]
        for var, doc in list(bm_statement_list.items()):
            if doc == docname:
                del bm_statement_list[var]
        bm_constant_list = self.data["bm_constant"]
        for var, doc in list(bm_constant_list.items()):
            if doc == docname:
                del bm_constant_list[var]

    def find_doc(self, key, obj_type):
        zret = None

        if obj_type == "bm_statement":
            obj_list = self.data["bm_statement"]
        elif obj_type == "bm_constant":
            obj_list = self.data["bm_constant"]
        else:
            obj_list = None

        if obj_list and key in obj_list:
            zret = obj_list[key]

        return zret

    def resolve_xref(self, env, src_doc, builder, obj_type, target, node, cont_node):
        dst_doc = self.find_doc(target, obj_type)
        if dst_doc:
            return sphinx.util.nodes.make_refnode(
                builder,
                src_doc,
                dst_doc,
                nodes.make_id(target),
                cont_node,
                "records.config",
            )

    def get_objects(self):
        for var, doc in self.data["bm_statement"].items():
            yield var, var, "bm_statement", doc, var, 1
        for var, doc in self.data["bm_constant"].items():
            yield var, var, "bm_constant", doc, var, 1


# get the branch this documentation is building for in X.X.x form
with open(os.path.join(__file__, "../../../AMMR.version.any"), "r") as f:
    contents = f.read()
    match = re.compile(r'.*AMMR_VERSION\s"(?P<version>.*)"').search(contents)
    ammr_version = ".".join(match.groupdict()["version"].split(".", 3)[:3])

# get the current branch the local repository is on
git_branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])


def make_git_link(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    This docutils role lets us link to source code via the handy :ammr:git: markup.
    Link references are rooted at the top level source directory. All links resolve
    to GitLab.

    Examples:

        To link to proxy/Main.cc:

            This is a link to seg.any file: :ts:git:`proxy/Main.cc`.

        To link to CONTRIBUTING.md:

            If you want to contribute, take a look at :ammr:git:`CONTRIBUTING.md`.
    """
    url = "https://gitlab.com/anybody/beta/ammr/blob/{}/{}"
    ref = ammr_version if ammr_version == git_branch else "master"
    node = nodes.reference(rawtext, text, refuri=url.format(ref, text), **options)
    return [node], []


def setup(app):
    # app.add_crossref_type('configfile', 'file',
    #                       objname='Configuration file',
    #                       indextemplate='pair: %s; Configuration files')
    # app.add_crossref_type('logfile', 'file',
    #                       objname='Log file',
    #                       indextemplate='pair: %s; Log files')

    app.add_domain(AMMRDomain)

    # this lets us do :ammr:git:`<file_path>` and link to the file on gitlab
    app.add_role_to_domain("ammr", "git", make_git_link)

