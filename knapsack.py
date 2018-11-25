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


import numpy as np

class knapsack(object):
    '''Represent a little abstract, we are going to try to solve a classic dynamic
    programming problems, the knapsack problem (or the knapsack).

    '''

    def __init__(self, values, wts_values, capacity):
        # ​​values of the items in the knapsack
        self.values = values
        # ​​weights of the items in the knapsack
        self.wts_values = wts_values
        self.capacity = capacity
        self.count_weights_row = capacity + 1
        self.count_values = len(values)
        self.table = np.zeros([len(values)+1, self.count_weights_row])

    def dp_knapsack(self):
        '''Calculate the maximum weight that can be stored in the knapsack.

        Return the auxiliary table for the calculation and the maximum weight

        '''
        # First iterate over the items (rows)
        for index in range(1, self.count_values + 1):
            # Second iterate over the columns which represent weights
            for weight in range(1, self.count_weights_row):
                # If the item weights more than the capacity at that column?
                # Take above value, that problem was solved
                if self.wts_values[index-1] > weight:
                    self.table[index][weight] = self.table[index - 1][weight]
                    continue
                # if the value of the item < capacity
                prior_value = self.table[index-1][weight]
                # val of current item  + val of remaining weight
                new_option_best = self.values[index-1] + self.table[index - 1][weight - self.wts_values[index-1]]
                self.table[index][weight] = max(prior_value, new_option_best)
        return self.table, self.table[index][weight]

    def dp_knapsack_v2(self):
        '''Calculate the maximum weight that can be stored in the knapsack.

        Return the auxiliary table for the calculation and the maximum weight

        '''
        V = self.table
        wts = self.wts_values
        b = self.values
        # First iterate over the items (rows)
        for i in range(1, self.count_values + 1):
            # Second iterate over the columns which represent weights
            for w in range(1, self.count_weights_row):
                if wts[i-1] <= w:
                    if b[i-1] + V[i-1, w-wts[i-1]] > V[i-1,w]:
                        V[i,w] = b[i-1] + V[i-1,w-wts[i-1]]
                    else:
                        V[i,w] = V[i-1,w]
                else:
                    V[i,w] = V[i-1,w]
        return self.table, self.table[i][w]


    def print_path(self):
        '''Return the path with the weights

        '''
        res = {}
        values = []
        i = self.count_values
        k = self.capacity
        while i > 0:
            if self.table[i,k] != self.table[i-1,k]:
                weight = self.wts_values[i-1]
                value = self.values[i-1]
                values.append(value)
                res[weight]=('value = %s' % value)
                k -= self.wts_values[i-1]
                i -= 1
            else:
                i -= 1
        res['Sum(values)']= sum(values)
        return res
