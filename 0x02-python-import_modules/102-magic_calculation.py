#!/usr/bin/python3
import dis
from magic_calculation_102 import magic_calculation


def magic_calculation(a, b):
    """Recreate Python bytecode from a Python function."""
    if a < b:
        c = magic_calculation(a, b)
        return c
    else:
        return a + b


dis.dis(magic_calculation)
