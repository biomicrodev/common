import cProfile
import functools
import os
import pstats
from pathlib import Path
from typing import Callable, Any


def str2int(s: str) -> int:
    return int(round(float(s)))


def is_dir_empty(path: Path) -> bool:
    if not path.is_dir():
        raise ValueError(f"Path not a directory!")
    return not any([True for _ in os.scandir(path)])


def cprofile(
    msg: str = None,
    *,
    sort_by: str = "tottime",
    n_lines: int = 10,
    filename: Path = None,
) -> Callable:
    """
    A simple decorator for seeing how long something takes.
    For in-depth profiling, use cProfile.

    Usage
    -----
    @profile()  # not sure how to use the decorator without parentheses in a nice way
    def my_function():
        ...

    @profile("Time to run my function")
    def my_function():
        ...

    Parameters
    ----------
    msg : str
        A short description of the running task
    sort_by : str
        How to sort profile results
    n_lines : int
        How many profile lines to print

    """

    def outer(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args, **kwargs) -> Any:
            pr = cProfile.Profile()
            pr.enable()

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                raise e
            else:
                return result
            finally:
                pr.disable()
                if msg:
                    print(msg)
                ps = (
                    pstats.Stats(pr)
                    .strip_dirs()
                    .sort_stats(sort_by)
                    .print_stats(n_lines)
                )
                if filename is not None:
                    ps.dump_stats(filename)

        return inner

    return outer
