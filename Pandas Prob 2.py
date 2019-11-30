# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:15:48 2019

@author: Mary Mae
"""

import pandas as pd
cars = pd.read_csv('cars.csv')
carsA = cars.iloc[0:5,[0,2,4,6,8,10]]
carsB = cars.iloc[0]
carsC = cars.loc[23,'cyl']
carsD = cars.loc[[1,28,18],['Model','cyl','gear']]