#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
start.py - v0.0.1 2019-05-10 Antonio Andrade
This module provides simple classes and interfaces
Author's website: http://
"""

__version_info__ = (0, 0, 1)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "Antonio Andrade"
__copyright__ = "Copyright 2019, Antonio Andrade"
__credits__ = ["Antonio Andrade", ]
__license__ = "Apache 2.0"
__maintainer__ = "Antonio Andrade"
__email__ = "andrade.antonio@gmail.com"
__status__ = "Development"

### CHANGES ###
# 2019-05-10: v0.0.1 AA:
#   - First version

### TODO ###
#

### REFERENCES ###
#


def testing_var_1():

    return 1


def testing_var_2():
    return 2


def testing_failed():
    return None


def testing(var):
    if var == 1:
        return testing_var_1()
    if var == 2:
        return testing_var_2()
    else:
        return testing_failed()


if __name__ == "__main__":

    print(testing(1))
    print(testing(2))
    print(testing(22))
