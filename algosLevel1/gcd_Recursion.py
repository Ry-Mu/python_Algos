#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:14:40 2017

@author: RyanMunguia
"""

def gcd_rec(x,y, low = 0):
    if low == 0:
        if (x < y):
            low = x
        else:
            low = y
    
    if ((x % low) == 0) and ((y % low) == 0):
        print("Eureka! I think we found it. X is: ",x, "y is: ",y,"and low is: ",low)
        return(low)
    else:
        print("Not yet. Right now, X is: ",x, "y is: ",y,"and low is: ",low)
        return(gcd_rec(x,y,low-1))
    
print(gcd_rec(6,9))
print(gcd_rec(3,10))