import os
from pathlib import Path
from dataclasses import dataclass
from typing import Tuple


@dataclass
class AMSContext:
    py_file: str
    fun_name: str
    anyfun_full_name: str
    anyfunex_file: str
    anyfunex_line: int
    call_location_file: str


Ctx = Tuple[str, str, str, str, int, str]


def os_path_exists(context: Ctx, fpath: str) -> int:
    context = AMSContext(*context)
    fpath = Path(fpath)
    if not fpath.is_absolute():
        fpath = Path(context.call_location_file).parent.joinpath(fpath)
    return int(os.path.exists(fpath))


def os_path_dirname(context: Ctx, fpath: str) -> str:
    return os.path.dirname(fpath)


def os_path_abspath(context: Ctx, fpath: str) -> str:
    context = AMSContext(*context)
    fpath = Path(fpath)
    if not fpath.is_absolute():
        fpath = Path(context.call_location_file).parent.joinpath(fpath)
    return os.path.abspath(fpath)


def os_path_basename(context: Ctx, fpath: str) -> str:
    return os.path.basename(fpath)

def get_current_file(context: Ctx) -> str:
    context = AMSContext(*context)
    return context.call_location_file
