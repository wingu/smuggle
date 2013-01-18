"""
Support for importing a module from a specific path without (permanently)
modifying sys.path.
"""

import sys


def smuggle(module, path):
    """
    Imports `module` from `path`, even if it's not on sys.path, without
    (permanently) modifying sys.path.

    Sorry.
    """
    if module in sys.modules:
        return module
    orig_sys_path = list(sys.path)
    try:
        sys.path.insert(0, path)
        loaded_module = globals()[module] = __import__(module)
        return loaded_module
    finally:
        sys.path = orig_sys_path
