#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Assumes expression1 and expression2 are valid sympy expressions in one variable, x, with domain all reals.
#Returns True if they are equal (more accuractely, if they evaluate closely on 100 random points) and False if they are not.

from sympy import *
import random

def checker(expression1, expression2):
