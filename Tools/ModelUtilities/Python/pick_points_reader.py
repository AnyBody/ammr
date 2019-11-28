import os
import json
import functools
import dataclasses
from pprint import pprint
from xml.etree import ElementTree


from contextlib import contextmanager
from pathlib import Path
from typing import Tuple


@dataclasses.dataclass(frozen=True)
class AMSContext:
    """ Helper class for easy acces to members in the context variable """

    py_file: str
    fun_name: str
    anyfun_full_name: str
    anyfunex_file: str
    anyfunex_line: int
    call_location_file: str

    def __iter__(self):
        yield from dataclasses.astuple(self)


def save_arguments(func):
    """ Helper decorator for saving arguments from for later debugging"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global __name__
        if __name__ == "__main__":
            # Disable save when run as script
            return func(*args, **kwargs)
        curent_file = Path(__file__)
        filename = curent_file.parent / f"{curent_file.stem}_{func.__name__}.json"
        with open(filename, "w+") as fh:
            fh.write(json.dumps({"args": args, "cwd": os.getcwd()}, indent=4))
        return func(*args, **kwargs)

    return wrapper


@contextmanager
def debug_context(fun):
    context_file = Path(__file__).parent / f"{Path(__file__).stem}_{fun.__name__}.json"
    if not context_file.exists():
        raise FileNotFoundError("No file saved data for debugging")
    with open(context_file, "r+") as fh:
        data = json.load(fh)
    olddir = Path.cwd()
    os.chdir(data["cwd"])
    yield data["args"]
    os.chdir(olddir)


@save_arguments
def read_point(context, ppfile, pointname):
    """ Return a point from a meshlab pickpoints (pp) file """
    context = AMSContext(*context)
    # Change directory to the call location in AMS
    os.chdir(Path(context.call_location_file).parent)
    ppfile = Path(ppfile)
    if not ppfile.exists():
        raise FileNotFoundError(f"The file '{ppfile}' could not be found")
    return _read_point_from_file(ppfile, pointname)


def _read_point(ppfile, pointname):
    """ Return a point from a meshlab pickpoints (pp) file """
    tree = ElementTree.parse(ppfile)
    pp = tree.findall(f"point[@active='1'][@name='{pointname}']")
    assert pp, f"No point named {pointname} found in the file"
    return ( float(pp[0].attrib['x']), float(pp[0].attrib['y']), float(pp[0].attrib['z']))

if __name__ == "__main__":
    with debug_context(read_point_from_file) as args:
        pprint(AMSContext(*args[0]).__dict__)
        print(read_point_from_file(*args))
    pass
