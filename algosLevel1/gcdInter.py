#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 18:49:50 2017

@author: RyanMunguia
"""
def gcd_Inter(x = 0, y = 0):
    low = 0

    if (x<y):
        low = x
    else:
        low = y
    
    for i in range(low):
        if ((x % low) == 0) and ((y % low) == 0):
            print("The low is: ", low)
            return low
        else:
            low = low - 1
  
 
   

print(gcd_Inter(6,9))
print(gcd_Inter(3,10))