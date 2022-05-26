#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 11:23:37 2022

@author: alexb
"""
from django.urls import path

from . import views

app_name = 'calc_probs'
urlpatterns = [
    # /calc_probs/
    path('', views.index, name='index'),
    # example: /calc_probs/3/
    path('<int:question_id>/', views.detail, name='detail'),
    # example: /calc_probs/3/result/
    path('<int:question_id>/result/', views.result, name='result'),
    # /calc_probs/check/
    path('check/', views.check, name='check'),    
    # /calc_probs/check_result/
    path('check/result/', views.check_result, name='check_result'),  
   ]