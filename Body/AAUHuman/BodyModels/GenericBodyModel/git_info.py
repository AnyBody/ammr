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


def git_info(context, fpath: str) -> Tuple[str, str]:
    """Get the git head and commit of a file in the repository."""
    context = AMSContext(*context)
    gitfolder = Path(fpath)
    if not gitfolder.is_absolute():
        gitfolder = Path(context.call_location_file).parent.joinpath(gitfolder)
    
    head_file = gitfolder /"HEAD"
    orig_file = gitfolder / "ORIG_HEAD"

    if not head_file.is_file() or not orig_file.is_file():
        raise FileNotFoundError(f"Git folder not found: {gitfolder}")
    
    ref = head_file.read_text(encoding="utf-8").strip()
    hash = orig_file.read_text(encoding="utf-8").strip()
    return ref, hash

