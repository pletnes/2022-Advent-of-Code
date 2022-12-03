import pathlib
import traceback
from pprint import pprint as pp

from rich.traceback import install
install()


def inp(suffix=''):
    """
    Most / all AoC tasks can read the inputs from one text file.
    This function finds the input based on the python code filename in the
    `input` directory. For instance, `dec03.py` will read inputs from
    `input/dec03.txt`.
    """
    callstack = traceback.extract_stack()
    prev_frame = callstack[-2]
    fname = pathlib.Path(prev_frame.filename).stem
    code_file = pathlib.Path(fname)
    here = code_file.parent
    inputfile = here / "input" / f"{code_file.stem}{suffix}.txt"

    print(f"AoC solution for {code_file.stem}")
    return list(map(str.strip, inputfile.open("r").readlines()))


def p(*s):
    """
    Print arguments with a dash between. Useful for debugging.
    """
    print(*s, sep=" - ")
