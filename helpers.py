import pathlib
from pprint import pprint as pp


def inp(fname):
    code_file = pathlib.Path(fname)
    here = code_file.parent
    inputfile = here / "input" / f"{code_file.stem}.txt"
    print(f"AoC solution for {code_file.stem}")

    return list(map(str.strip, inputfile.open("r").readlines()))


def p(*s):
    print(*s, sep=" - ")
