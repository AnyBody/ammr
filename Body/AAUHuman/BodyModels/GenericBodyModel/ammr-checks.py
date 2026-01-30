import dataclasses

# import debugpy
# debugpy.configure({"python":"C:/Program Files/AnyBody Technology/AnyBody.8.2_Beta/Python/python.exe"})
# debugpy.listen(5679, in_process_debug_adapter=True)
# print('Waiting for debugger attach')
# debugpy.wait_for_client()
# debugpy.breakpoint()
# print('break on this line')


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


def is_file_writeable(context, fpath):
    """ Check if fpath is a writeable file """
    context = AMSContext(*context)
    is_writeable = True
    try:
        with open(fpath, "r+"):
            pass
    except PermissionError:
        is_writeable = False

    return is_writeable


def endswith(context, string: str, arg: str):
    """ Check if string ends with arg """
    context = AMSContext(*context)
    return int(string.endswith(arg))


if __name__ == "__main__":
    pass
