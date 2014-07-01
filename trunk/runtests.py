#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from jing.tests import Test
try:
    directory = sys.argv[1]
except:
    directory = None

if __name__ == '__main__':
    test = Test(directory)
    test.run()
