#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:24:53 2017

@author: RyanMunguia
"""

# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

# def flatten(aList):
#    ''' 
#    aList: a list 
#    Returns a copy of aList, which is a flattened version of aList 
#    '''
  


def flatten(aList):
    newList = []
    for item in aList:
        if type(item) != type([]):
            newList.append(item)
        else:
            newList.extend(flatten(item))
    return newList