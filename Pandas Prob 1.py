# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:28:22 2019

@author: Mary Mae
"""

import pandas as pd
cars = pd.read_csv('cars.csv')
cars2 = cars.iloc[[0,1,2,3,4,27,28,29,30,31]]