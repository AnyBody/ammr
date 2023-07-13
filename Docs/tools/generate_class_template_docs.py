"""
This script searches for class templates in the source code and generates
documentation for them.
"""
import re
import warnings
from pathlib import Path
from collections import defaultdict
import textwrap

import jinja2


THIS_DIR = Path(__file__).parent
MODELUTILS = THIS_DIR.joinpath("../../Tools/ModelUtilities").resolve()
OUTDIR = THIS_DIR.joinpath("class-templates")

OUTDIR.mkdir(exist_ok=True)

# Remove all *.md files OUTDIR
for file in OUTDIR.glob("*.md"):
    file.unlink()


# regular expression which finds text starting with #class_template at the
# beginning of a line and match the following text across multiple lines until
# the first end parenthesis ")" is found.
RE_CLASSTMPL_WITH_DOCS = re.compile(
    r"""
    (?P<docs>(^///.*?\n)+)                   # Pre documentation part
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


def find_file_docs(file_content: str) -> str:
    """
    Finds the documentation string of the file.
    """
    match = RE_FILE_DOCS.match(file_content)
    if not match:
        return ""
    docs = match.groupdict()["docs"].strip()
    return docs and docs.splitlines()[0]


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


def find_class_templates(file_content: str) -> list:
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
        classtempl = {"classname": groupd["name"]}

        docstring = groupd["docs"]
        docstring = RE_MATCH_LEADING_SLASHES.sub("", docstring)
        docstring = textwrap.dedent(docstring)
        classtempl["docs"] = docstring.strip()
        classtype, args = parse_class_template_arguments(groupd["arguments"])
        classtempl["classtype"] = classtype
        classtempl["args"] = args
        template_list.append(classtempl)

    return template_list


fileloader = jinja2.FileSystemLoader(searchpath=Path(__file__).parent)
env = jinja2.Environment(loader=fileloader)
template = env.get_template("class-template.md.jinja")

allgroups = defaultdict(lambda: defaultdict(list))


for file in MODELUTILS.glob("**/*.any"):
    content = file.read_text()
    class_templates = find_class_templates(content)
    if not class_templates:
        continue
    filedocstring = find_file_docs(content)
    if not filedocstring:
        warnings.warn(f"File {file} has no documentation string.")

    # find the compent of the file path relative to search_path
    relative_path = file.relative_to(MODELUTILS)
    filename = relative_path.stem
    group = ".".join(relative_path.parent.parts)

    allgroups[group][filename] = [ct["classname"] for ct in class_templates]

    outfile = OUTDIR / f"{group}.{filename}.md"
    outfile.write_text(
        template.render(
            filename=filename,
            group=group,
            filedocstring=filedocstring,
            class_templates=class_templates,
        )
    )
    # Path(

    #     template.render(filename=file.name, class_templates=class_templates)


toc_file = OUTDIR / "class_templates_TOC.txt"
toc_template = env.get_template("class_template_TOC.txt.jinja")
toc_file.write_text(toc_template.render(groups=allgroups))
