#!/usr/bin/python
# encoding: utf-8

from __future__ import print_function
import sys

# 调试日志
def log(s, *args):
    if args:
        s = s % args
    print(s, file = sys.stderr)