"""
Ideally, we wouldn't need to pull in all the calc symbols here,
but courses were using 'import calc', so we need this for
backwards compatibility
"""

from .calc import *

__version__ = '2.0.1'
