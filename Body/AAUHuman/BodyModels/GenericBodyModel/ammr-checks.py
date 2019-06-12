import os
import pickle
import hashlib
import inspect
import functools
import logging

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
        curent_file = Path(__file__)
        filename = curent_file.parent / f"{curent_file.stem}_{func.__name__}.txt"
        with open(filename, "wb") as fh:
            pickle.dump(args, fh)
        return func(*args, **kwargs)

    return wrapper


def load_arguments(name):
    """ Helper function for loading arguments from a pickled file"""
    curent_file = Path(__file__)
    filename = curent_file.parent / f"{curent_file.stem}_{name}.txt"
    with open(filename, "rb") as fh:
        return pickle.load(fh)


# @log_exception(logger)
# @save_arguments
def is_file_writeable(context, fpath):
    """ Check if fpath is a writeable file """
    return int(os.access(fpath, os.W_OK))


# @save_arguments
def hash_directory(context, dirpath, subsearch="**/*.any"):
    """ Compute an md5 hash of all "*.any" files in directory  
    """
    hashval = ""
    try:
        digest = hashlib.md5()
        dirpath = Path(dirpath)
        for fpath in dirpath.glob(subsearch):
            # Hash relative path of file. To handle empty files and renames
            digest.update(
                hashlib.md5(str(fpath.relative_to(dirpath)).encode()).digest()
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
    context, *args = load_arguments("hash_directory")
    print(context)
    hashval = hash_directory(context, *args)
    print(hashval)
