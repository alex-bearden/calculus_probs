#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 11:23:37 2022

@author: alexb
"""
from django.urls import path

from . import views
from .models import IntegralQuestion

app_name = 'calc_probs'

urlpatterns = [
    # /calc_probs/
    path('', views.IndexView.as_view(model=IntegralQuestion), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('random', views.random_prob, name='random_problem'),
    path('check/', views.check, name='check'),  
    path('check/result/', views.check_result, name='check_result'),  
   ]

