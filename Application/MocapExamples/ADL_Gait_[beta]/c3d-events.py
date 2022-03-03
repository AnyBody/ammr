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


def save_debug_context(func):
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
def load_debug_context(fun):
    context_file = Path(__file__).parent / f"{Path(__file__).stem}_{fun.__name__}.json"
    if not context_file.exists():
        raise FileNotFoundError("No file saved data for debugging")
    with open(context_file, "r+") as fh:
        data = json.load(fh)
    olddir = Path.cwd()
    os.chdir(data["cwd"])
    yield data["args"]
    os.chdir(olddir)



# import debugpy
# # 5678 is the default attach port in the VS Code debug configurations. Unless a host and port are specified, host defaults to 127.0.0.1
# debugpy.listen(5678)
# print('Waiting for debugger attach')
# debugpy.wait_for_client()
# # debugpy.breakpoint()
# # print('break on this line')

# @save_debug_context
def get_event(info, event_context, event_label, times_data, contexts_data, labels_data):
    
    # debugpy.breakpoint()

    info = AMSContext(*info)


    contexts = ["".join(_).strip() for _ in contexts_data]
    labels = ["".join(_).strip() for _ in labels_data]
    times = [t for (_, t) in times_data]

    idx = [
        i
        for i, pair in enumerate(zip(contexts, labels))
        if (event_context, event_label) == pair
    ]

    events_times = [ times[i] for i in idx]

    events_times += [-1] * (len(times) - len(events_times))

    # if debug:
    #     db = shelve.Shelf(dumbdbm.open('test.shelf'))
    #     db['info'] = info
    #     db['event_context'] = event_context
    #     db['label'] = label
    #     db['times_data'] = times_data
    #     db['labels_data'] = labels_data
    #     db['contexts_data'] = contexts_data
    #     db.close()

    return tuple(events_times)

def get_event_time(info, event_context, event_label, times_data, contexts_data, labels_data, time_array):
    """ Use a extra time vector input to lookup the time closest to the event """

    # debugpy.breakpoint()
    event_times =  get_event(info, event_context, event_label, times_data, contexts_data, labels_data)

    event_times = list(event_times)
    for i, t0 in enumerate(event_times):
        if t0 < 0:
            break
        event_times[i] = time_array[argmin(diff(time_array,t0))]

    return tuple(event_times)

def diff(vec, val):
    return [abs(v-val) for v in vec]

def argmin(v):
    return v.index(min(v))


if __name__ == "__main__":
    with debug_context(hash_directory) as args:
        print(AMSContext(*args[0]))
        hashcode = hash_directory(*args)
    print(hashcode)
