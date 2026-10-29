# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Classify three integer side lengths in the inclusive range 1 through 200. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of the squares of two sides equals the square of the third side, then return 'Right'
      
      Right triangles are recognized in any side order.
    """

    # Check types before comparisons; bool is not a side-length integer.
    if not(type(a) is int and type(b) is int and type(c) is int):
        return 'InvalidInput'

    # Require that the input values be >= 1 and <= 200.
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly greater than the third side
    # or the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif (a ** 2 + b ** 2 == c ** 2 or
          a ** 2 + c ** 2 == b ** 2 or
          b ** 2 + c ** 2 == a ** 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'
