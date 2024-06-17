import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple


@dataclass
class AMSContext:
    py_file: str
    fun_name: str
    anyfun_full_name: str
    anyfunex_file: str
    anyfunex_line: int
    call_location_file: str




def git_info(context: tuple, fpath: str) -> Tuple[str, str]:
    """
    Get the git information of a repository.

    Args:
        context (tuple): The context of the function call.
        fpath (str): The path to the git repository.

    Returns:
        Tuple[str, str]: A tuple containing the reference (branch or tag name) and the commit hash.

    Raises:
        subprocess.CalledProcessError: If the git command fails.
        subprocess.TimeoutExpired: If the git command times out.
    """
    context = AMSContext(*context)
    gitfolder = Path(fpath)
    if not gitfolder.is_absolute():
        gitfolder = Path(context.call_location_file).parent.joinpath(gitfolder)

    if not gitfolder.is_dir():
        return "unknown", "unknown"

    options = dict(
        creationflags=subprocess.CREATE_NO_WINDOW,
        timeout=2,
        text=True,
    )

    try:
        subprocess.run(["git", "--version"], capture_output=True, **options)
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ):
        return "unknown", "unknown"

    basecmd = ["git", "-C", f"{gitfolder.absolute()}"]
    try:
        cmd = basecmd + ["rev-parse", "HEAD"]
        hashref = subprocess.check_output(cmd, **options).strip()
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ):
        hashref = "unknown"

    try:
        cmd = basecmd + ["symbolic-ref", "-q", "--short", "HEAD"]
        branch_name = subprocess.check_output(cmd, **options).strip()
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ):
        branch_name = None

    try:
        cmd = basecmd + ["describe", "--tags", "--always"]
        tag_name = subprocess.check_output(cmd, **options).strip()
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ):
        tag_name = "unknown"

    ref = branch_name or tag_name
    return ref, hashref
