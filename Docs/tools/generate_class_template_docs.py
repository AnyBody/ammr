"""
This script searches for class templates in the source code and generates
documentation for them.
"""
import re
import warnings
from pathlib import Path
from collections import defaultdict
import textwrap
from typing import Any
from pydantic import BaseModel, ValidationError

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
RE_MATCH_LEADING_SLASHES = re.compile(r"^///", re.MULTILINE)

RE_FILE_DOCS = re.compile(
    r"""
    (^\s?\#.*?\n|^\s?\n)* # Lines with #... or empty lines
    ^\s?/\*+      # Start of comment block
    (?P<docs>.*?) # Documentation string
    \*+/          # End of comment block
    """,
    re.VERBOSE | re.MULTILINE | re.DOTALL,
)



class ClassTemplateInfo(BaseModel):
    classname: str
    classtype: str = ""
    args: list[dict[str, str]] = []
    docs: str = ""


class FileInfo(BaseModel):
    group: str
    topic: str
    description: str = ""
    include_str: str = ""
    class_templates: list[ClassTemplateInfo] = []




def parse_file_docs(file_content: str, include_str:str) -> FileInfo:
    """
    Finds the documentation string of the file.
    """
    stopidx=file_content.find("*/")
    match = RE_FILE_DOCS.match(file_content[:stopidx+10])
    if not match:
        docs = ""
    else:
        docs = match.groupdict()["docs"]
    meta, _ = frontmatter.parse(docs)
    return FileInfo(include_str=include_str, **meta)


def parse_class_template_arguments(arg_string: str) -> tuple[str, list[dict]]:
    """
    Parses the argument string of a class template and returns a dictionary
    with the argument names as keys and the argument values as values.
    """
    args = list()
    classtype = "AnyFolder"
    for arg in arg_string.split(","):
        arg = arg.strip()
        if not arg:
            continue
        argname, _, value = arg.partition("=")
        argname = argname.strip()
        value = value.strip()
        if argname == "__CLASS__":
            classtype = value
            continue
        args.append({"name": argname, "value": value})

    return classtype, args




def find_class_templates(
    file_content: str
) -> list[ClassTemplateInfo]:
    """
    Finds all class templates in the given file content and returns a list of
    dictionaries with the following keys:
    - name: The name of the class template
    - arguments: A dictionary with the argument names as keys and the argument
      values as values.
    - docs: The documentation string of the class template.
    """
    template_list = []
    for match in RE_CLASSTMPL_WITH_DOCS.finditer(file_content):
        groupd = match.groupdict()
        docstring = groupd["docs"]
        docstring = RE_MATCH_LEADING_SLASHES.sub("", docstring)
        docstring = textwrap.dedent(docstring).strip()
        classtype, args = parse_class_template_arguments(groupd["arguments"])
        template_list.append(
            ClassTemplateInfo(
                classname=groupd["name"],
                docs=docstring,
                classtype=classtype,
                args=args,
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

    for file in base_path.glob("**/*.any"):
        content = file.read_text()
        include_str = f"<{ams_path_def}>\\{file.relative_to(base_path)}"
        class_templates = find_class_templates(content)
        if not class_templates:
            continue
        try:
            filedata = parse_file_docs(content, include_str)
        except ValidationError:
            warnings.warn(f"File {file.name} has invalid documentation meta data")
            continue
        filedata.class_templates = class_templates
        # find the compent of the file path relative to search_path

        classt_info[filedata.group][filedata.topic][file.stem] = filedata

        outfile = CLASST_DIR / f"{filedata.group}.{filedata.topic}.{file.stem}.md"
        outfile.write_text(
            template.render(
                filename=file.stem,
                group=f"{filedata.group}.{filedata.topic}",
                filedocstring=filedata.description or "",
                class_templates=class_templates,
                include_str=filedata.include_str,
            )
        )

    # Write group toc files
    for group, topics in classt_info.items():
        group_file = TOOLS_DIR / f"{group}-toc.md"
        group_template = env.get_template("group-toc.md.jinja")
        group_file.write_text(
            group_template.render(group=group, topics=topics)
        )


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
