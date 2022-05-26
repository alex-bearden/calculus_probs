#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Assumes integrand and antideriv are non-constant functions with domain all reals, input as strings that give valid sympy expressions in one variable, x.
# Returns True if the indefinite integral of integrand is antideriv and False otherwise (based on evaluation at 100 random points).

from sympy import *
from numpy.random import normal
import math

def checker(integrand, antideriv):
    x = Symbol('x')
    integrated_expr = integrate(eval(integrand))
    antideriv_expr = eval(antideriv)
    constant = integrated_expr.evalf(subs={x:0}) - antideriv_expr.evalf(subs={x:0})
    sample_points = normal(0, 10, 100)
    valid = True
    for point in sample_points:
        diff = integrated_expr.evalf(subs={x:point}) - antideriv_expr.evalf(subs={x:point})
        if abs(diff - constant) > 1e-5:
            valid = False
            break
    return valid

    """     num = 0
    for point in sample_points:
        diff = integrated_expr.evalf(subs={x:point}) - antideriv_expr.evalf(subs={x:point})
        if math.isclose(constant):
            num += 1
        else:
            print(constant-diff)
    return num """