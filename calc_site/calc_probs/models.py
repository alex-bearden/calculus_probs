from django.db import models
from sympy import *
from sympy.printing.latex import latex

class IntegralQuestion(models.Model):
    integrand = models.CharField(max_length=200)
    technique = models.CharField(max_length=200)
    def __str__(self):
        return 'integral of ' + self.integrand
    def latex_integral(self):
        x = Symbol('x')
        return latex(Integral(eval(self.integrand), x))