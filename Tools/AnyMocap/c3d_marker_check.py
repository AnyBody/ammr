import os
from pathlib import Path
from textwrap import fill
from typing import NamedTuple

import ezc3d 

import functools


class Context(NamedTuple):
    py_file: str
    fun_name: str
    anyfun_full_name: str
    anyfunex_file: str
    anyfunex_line: str
    call_location_file:str



def check_c3d_file(context: Context, c3d_file: str):
    """ Check if fpath is a writeable file """
    
    report_str = "" 

    if not os.path.isfile(c3d_file):
        return f"{c3d_file} is not a file\n"

    c3d = ezc3d.c3d(c3d_file)
    points_used = c3d['parameters']['POINT']['USED']['value'][0];  # Print the number of points used
    point_data = c3d['data']['points']

    report_str += f"Points used: {points_used}\n"
    report_str += f"Points data: \n{point_data}\n"
    
    return report_str




if __name__ == "__main__":
   check_c3d_file("test.c3d")