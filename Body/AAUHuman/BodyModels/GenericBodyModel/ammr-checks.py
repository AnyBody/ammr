import os
import json
import logging
import hashlib
import inspect
import functools
from contextlib import contextmanager

from glob import iglob

from pathlib import Path

import dataclasses
from typing import Tuple


import functools


def create_logger(filename):
    """
    Creates a logging object and returns it
    """
    logger = logging.getLogger("ams_python_logger")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler(filename)

    fmt = "\n%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.handlers = []
    # add handler to logger object
    logger.addHandler(fh)
    return logger


# logger = create_logger(Path(__file__).with_suffix(".log"))


def log_exception(logger):
    """
    A decorator that wraps the passed in function and logs 
    exceptions should one occur
 
    @param logger: The logging object
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                logger.exception(f"There was an exception in {func.__name__}")
                raise

        return wrapper

    return decorator


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
            # Disable save not called externally.
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


# @log_exception(logger)
# @save_arguments
def is_file_writeable(context, fpath):
    """ Check if fpath is a writeable file """
    try:
        with open(fpath, "r+"):
            pass
    except PermissionError:
        return False
    return True

def endswith(context, string:str, arg:str):
    return int(string.endswith(arg))


#@save_arguments
def hash_directory(context, dirpath, subsearch="**/*.any"):
    """ Compute an md5 hash of all files matching a `subsearch` globbing expression
        defaults is recursive search for anyscript files (**/*.any"). 
    """
    hashval = ""
    try:
        digest = hashlib.md5()
        dirpath = Path(dirpath)
        for fpath in sorted(dirpath.glob(subsearch)):
            # Hash relative path of file. To handle empty files and renames
            digest.update(
                hashlib.md5(str(fpath.relative_to(dirpath)).encode('utf-8')).digest()
            )
            with open(fpath, "rb") as fh:
                while True:
                    buf = fh.read(2 ** 16)
                    if not buf:
                        break
                    digest.update(buf)
        hashval = digest.hexdigest()
    except Exception:
        # Errors must not prevent AnyBody from loading.
        pass
        # logger.exception(f"There was an exception in hash_directory()")
    finally:
        return hashval


if __name__ == "__main__":
    with debug_context(hash_directory) as args:
        print(AMSContext(*args[0]))
        hashcode = hash_directory(*args)
    print(hashcode)
