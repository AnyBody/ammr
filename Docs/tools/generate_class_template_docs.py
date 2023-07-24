"""
This script searches for class templates in the source code and generates
documentation for them.
"""
import re
import os
import warnings
from pathlib import Path
from collections import defaultdict
import textwrap
from typing import Any
from pydantic import BaseModel, ValidationError

from tqdm import tqdm

import frontmatter
import jinja2


TOOLS_DIR = Path(__file__).parent
AMMR_TOOLS = TOOLS_DIR.joinpath("../../Tools").resolve()
CLASST_DIR = TOOLS_DIR.joinpath("class-templates")


# regular expression which finds text starting with #class_template at the
# beginning of a line and match the following text across multiple lines until
# the first end parenthesis ")" is found.
RE_CLASSTMPL_WITH_DOCS = re.compile(
    r"""
    (?P<docs>(^///[^\n]*?\n)+)                   # Pre documentation part
    ^\#class_template[\s\n]+  #
    (?P<name>[\w]+)             # Class name
    [\s\n]?\(                   # Opening parenthesis
    (?P<arguments>.*?)          # Class arguments
    \)                          # Closing parenthesis
    """,
    re.VERBOSE | re.MULTILINE | re.DOTALL,
)
RE_MATCH_3_SLASHES = re.compile(r"^\s*///", re.MULTILINE)
RE_MATCH_2_SLASHES = re.compile(r"^\s*//", re.MULTILINE)

RE_FILE_DOCS = re.compile(
    r"""
    (^\s?\#.*?\n|^\s?\n)* # Lines with #... or empty lines
    ^\s?/\*+      # Start of comment block
    (?P<docs>.*?) # Documentation string
    \*+/          # End of comment block
    """,
    re.VERBOSE | re.MULTILINE | re.DOTALL,
)

class MemberInfo(BaseModel):
    """ Information about a documented class member."""
    group: str = ""
    name: str
    type: str = ""
    value: str = ""
    docs: str = ""

class ArgInfo(BaseModel):
    """ Information about a class template argument."""
    name: str
    value: str = ""
    docs: str = ""


class ClassTemplateInfo(BaseModel):
    """ Information about a class template."""
    name: str
    type: str = ""
    args: list[ArgInfo] = []
    docs: str = ""
    members: list[MemberInfo] = []
    expected_members: list[MemberInfo] = []


class FileInfo(BaseModel):
    """" Information about a file."""
    group: str
    topic: str
    descr: str = ""
    include_str: str = ""
    class_templates: list[ClassTemplateInfo] = []


def parse_file_docs(file: str | os.PathLike, include_str: str) -> FileInfo:
    """
    Finds the documentation string of the file.
    """
    file_content = Path(file).read_text(encoding="utf-8")
    stopidx = file_content.find("*/")
    match = RE_FILE_DOCS.match(file_content[: stopidx + 10])
    if not match:
        docs = ""
    else:
        docs = match.groupdict()["docs"]
    meta, _ = frontmatter.parse(docs)
    return FileInfo(include_str=include_str, **meta)

def parse_class_type(args: list[ArgInfo]) -> str:
    """ Returns the class type of the class template."""
    for arg in args:
        if arg.name == "__CLASS__":
            return arg.value
    return "AnyFolder"

def parse_class_args(arg_string: str) -> list[ArgInfo]:
    """
    Parses the argument string of a class template and returns a dictionary
    with the argument names as keys and the argument values as values.
    """
    args = []
    for arg_str in arg_string.split(","):
        arg_str = arg_str.strip()
        if not arg_str:
            continue
        argname, _, value = arg_str.partition("=")
        args.append(ArgInfo(
            name=argname.strip(),
            value=value.strip(),
        ))
    return args

def parse_arg_docs(filecontent:str, classname:str, argname:str) -> str:
    """ Parses the documentation string of a class template argument.
        Looks for a comment block starting with 
        //{classname}#{argname}
        // <Some doc string>
        //
        and returns the doc string.
    """
    re_arg_docs = re.compile(
        rf"""
        ^\s*//\s*{classname}\s*\#\s*{argname}\s*?\n #Match start of argument
        (?P<docs>\s*//.*?)   #Match documentation string
        ^\s*?(//|//\s*?{classname}\s*\#\w+?)?\s*?\n     # Match an empty line
        """, re.MULTILINE |  re.DOTALL |  re.VERBOSE
    )
    if not (match:= re_arg_docs.search(filecontent)):
        return ""
    docs = match.groupdict()["docs"]
    docs = RE_MATCH_2_SLASHES.sub("", docs)
    docs = textwrap.dedent(docs).strip()
    return docs

def parse_expected_member_docs(filecontent:str, classname:str) -> list[MemberInfo]:
    """ Parses the documentation string of a class template argument.
        Looks for a comment block starting with 
        //{classname}#{argname}
        // <Some doc string>
        //
        and returns the doc string.
    """
    re_docs = re.compile(
        rf"""
        ^\s*//\s*{classname}\.(?P<group>[\w\.]+)\s*?\n #Match start of member
        (?P<docs>\s*//.*?)   #Match documentation string
        ^\s*?(//)?\s*?   # match start line
        (?P<type>\w+)\s+?
        (?P<name>\w+)
        \s*?=\s*
        (?P<value>.*?;.*?)\n
        """, re.MULTILINE |  re.DOTALL |  re.VERBOSE
    )
    expected_members = []
    for match in re_docs.finditer(filecontent):
        docs = match.groupdict()["docs"]
        docs = RE_MATCH_2_SLASHES.sub("", docs)
        docs = textwrap.dedent(docs).strip()
        expected_members.append(MemberInfo(
            group=match.groupdict()["group"],
            type=match.groupdict()["type"],
            name=match.groupdict()["name"],
            value=match.groupdict()["value"],
            docs=docs,
        ))
    return expected_members

def parse_class_members(filecontent:str, classname:str) -> list[MemberInfo]:
    """ Parses the file for documented members of a class template.
        Looks for members with documentation stirngs looking like this:  
        ```
        /// <docs>
        #var [type] <name> [= <value>];
        ```
        and return list of MemberInfo objects.
    """
    re_member_docs = re.compile(
        rf"""
        ^\s*///\s*{classname}(\.(?P<group>.+?))?\s*\n # Match keyword for member docs
        (?P<docs>(^\s*///.*?\n)+)   #Match member docs
        ^\s*\#var\s+              #Match start of member declaration
        (?P<type>\w+)?\s*       #Match member type
        (?P<name>\w+)\s*          #Match member name
        (=\s*(?P<value>.*?))?\s*;    #Match member value
        """, re.MULTILINE |  re.DOTALL |  re.VERBOSE
    )
    members = []
    for match in re_member_docs.finditer(filecontent):
        groupd = match.groupdict()
        member_name = groupd["name"] 
        if groupd["group"]:
            member_name = groupd["group"] + "." + member_name 
        member_type = groupd["type"]
        member_value = groupd["value"]
        member_docstring = groupd["docs"]
        member_docstring = RE_MATCH_3_SLASHES.sub("", member_docstring)
        member_docstring = textwrap.dedent(member_docstring).strip()
        members.append(MemberInfo(
            name=member_name,
            type=member_type,
            value=member_value or "",
            docs=member_docstring,
        ))
    return members

def find_class_templates(file: str | os.PathLike) -> list[ClassTemplateInfo]:
    """
    Finds all class templates in the given file content and returns a list of
    dictionaries with the following keys:
    - name: The name of the class template
    - arguments: A dictionary with the argument names as keys and the argument
      values as values.
    - docs: The documentation string of the class template.
    """
    template_list = []
    file = Path(file).resolve()
    filecontent = file.read_text(encoding="utf-8")
    for match in RE_CLASSTMPL_WITH_DOCS.finditer(filecontent):
        groupd = match.groupdict()
        class_name=groupd["name"]
        class_docstring = groupd["docs"]
        class_docstring = RE_MATCH_3_SLASHES.sub("", class_docstring)
        class_docstring = textwrap.dedent(class_docstring).strip()
        class_args = parse_class_args(groupd["arguments"])
        classtype = parse_class_type(class_args)
        for arg in class_args:
            arg.docs = parse_arg_docs(filecontent,class_name, arg.name)
        class_members = parse_class_members(filecontent, class_name)
        expected_members = parse_expected_member_docs(filecontent, class_name)
        
        template_list.append(
            ClassTemplateInfo(
                name=class_name,
                docs=class_docstring,
                type=classtype,
                args=class_args,
                members=class_members,
                expected_members=expected_members,
            )
        )
    return template_list


# Nested default dict for storing class template info
# allgroups[group][topic][filename] = class_templates
classt_info: defaultdict[
    str, defaultdict[str, defaultdict[str, list[Any]]]
] = defaultdict(lambda: defaultdict(lambda: defaultdict(FileInfo)))


def run(ams_path_def, base_path):
    fileloader = jinja2.FileSystemLoader(searchpath=Path(__file__).parent)
    env = jinja2.Environment(loader=fileloader)
    template = env.get_template("class-template.md.jinja")
    files = list(base_path.glob("**/*.any"))

    for file in tqdm(files, desc="Looking for class templates"):
        include_str = f"<{ams_path_def}>\\{file.relative_to(base_path)}"
        class_templates = find_class_templates(file)
        if not class_templates:
            continue
        try:
            filedata = parse_file_docs(file, include_str)
        except ValidationError:
            # warnings.warn(f"File {file.name} has invalid documentation meta data")
            continue
        filedata.class_templates = class_templates
        # find the compent of the file path relative to search_path

        classt_info[filedata.group][filedata.topic][file.stem] = filedata

        outfile = CLASST_DIR / f"{filedata.group}.{filedata.topic}.{file.stem}.md"
        outfile.write_text(
            template.render(
                filename=file.stem,
                group=filedata.group,
                topic=filedata.topic,
                filedocstring=filedata.descr or "",
                class_templates=class_templates,
                include_str=filedata.include_str,
            ), encoding="utf-8"
        )

    # Write group toc files
    for group, topics in classt_info.items():
        group_file = TOOLS_DIR / f"{group}-toc.md"
        group_template = env.get_template("group-toc.md.jinja")
        group_file.write_text(group_template.render(group=group, topics=topics))


def run_all():
    CLASST_DIR.mkdir(exist_ok=True)

    # Remove all *.md files CLASST_DIR
    for file in CLASST_DIR.glob("*.md"):
        file.unlink()

    # Remove all *.md files TOOLS_DIR
    for file in TOOLS_DIR.glob("*-toc.md"):
        file.unlink()

    run("AMMR_TOOLS", AMMR_TOOLS)


if __name__ == "__main__":
    run_all()
