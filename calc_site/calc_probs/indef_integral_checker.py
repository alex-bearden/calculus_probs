#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The inputs integrand and antideriv should be strings that give valid sympy expressions in one variable, x.
# This should correctly handle most functions you can write with a single expression,
# especially if the domain is either a single interval or a conull set (e.g., 'x**2', sqrt(x), 1/x, tan(x)).
# It does not handle ab(x) or many piecewise functions well.

# Returns True if the indefinite integral of integrand (restricted to an interval in its domain) is antideriv and False otherwise (based on evaluation at 100 random points).

from sympy import *
import math
import numpy as np
from scipy.stats import truncnorm

def checker(integrand, antideriv):
    x = Symbol('x')
    integrand_expr = parsing.sympy_parser.parse_expr(integrand)
    integrated_expr = integrate(integrand_expr, x)
    antideriv_expr = parsing.sympy_parser.parse_expr(antideriv)
    valid = True
    domain_integrated = calculus.util.continuous_domain(integrate(integrand_expr, x), x, Reals)
    domain_antideriv = calculus.util.continuous_domain(integrate(antideriv_expr, x), x, Reals)
    try:
        left_end = domain_integrated.inf
        right_end = domain_integrated.sup
        if left_end == right_end:
            valid = False
        if left_end == -oo:
            left_end = -np.inf
        if right_end == oo:
            right_end = np.inf
        base_point = truncnorm.rvs(left_end, right_end, loc=0, scale = 10)
        constant = integrated_expr.evalf(subs={x:base_point}) - antideriv_expr.evalf(subs={x:base_point})
        sample_points = truncnorm.rvs(left_end, right_end, loc=0, scale = 10, size=100)
        for point in sample_points:
            diff = integrated_expr.evalf(subs={x:point}) - antideriv_expr.evalf(subs={x:point})
            print(diff)
            if abs(diff - constant) > 1e-5:
                valid = False
                break       
    except:
        base_point = np.random.normal(0, 10)
        constant = integrated_expr.evalf(subs={x:base_point}) - antideriv_expr.evalf(subs={x:base_point})
        sample_points = np.random.normal(0, 10, 100)
        n=0
        for point in sample_points:
            diff = integrated_expr.evalf(subs={x:point}) - antideriv_expr.evalf(subs={x:point})
            print(diff)
            if abs(diff - constant) > 1e-5:
                valid = False
                break
    return valid