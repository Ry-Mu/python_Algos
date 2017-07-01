#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 10:47:57 2017

@author: RyanMunguia
"""
#polygon

import math

def polySum(n,s):
    
    #compute area
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    
    #compute perimeter
    perimeter = s*n
    
    return round((area + perimeter**2),4)

print(polySum(96,89))