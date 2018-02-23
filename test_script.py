# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:22:43 2018

@author: stephanie.labou
"""

import pandas

dat = pandas.read_csv('data/gapminder_all.csv')

dat['lifeExp_2002'].max()