#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_import)

from texttable import Texttable
from knapsack import knapsack as Knapsack

# WTS = [1,3,4,5]
# VALS = [1,4,5,7]

WTS = [1,2,5,6,7]
VALS = [1,6,18,22,28]

# WTS = [2,3,4,5]
# VALS = [3,4,5,6]

CAPACITY = 11

class Main(object):

    def __init__(self):
        '''A practical exercise of the knapsack problem solved with dynamic
        programming

        '''
        print ('''********************Knapsack problem************************
               Author: Oraldo Jacinto Simon
               Professor: M.I. Jesus Roberto López Santillán
               ''')
        knapsack_obj = Knapsack(VALS, WTS, CAPACITY)
        table_result, res = knapsack_obj.dp_knapsack()
        table = Texttable()
        table.set_cols_align(["c" for e in range(CAPACITY+1)])
        rows = []
        head = [index for index in range(CAPACITY+1)]
        rows.append(head)
        [str(rows.append(e)) for e in table_result]
        table.add_rows(rows)
        print("values = %s" % VALS)
        print("weights = %s" % WTS)
        print("capacity = %s" % CAPACITY)
        print(table.draw() + "\n")
        print("Solución: %d" % res)
        path = knapsack_obj.print_path()
        print("Entre las mochilas de la solución se encuentran: %s" % str(path))

Main()
