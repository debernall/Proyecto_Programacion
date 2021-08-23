#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 08:39:01 2021

@author: debernal
"""

import numpy as np

g=1.6
theta=np.radians(48.5)
xf=324.4
yf=0
v=np.sqrt((g*xf)/(2*(((-yf*((np.cos(theta))**2)/(xf))+((np.sin(theta))*(np.cos(theta)))))))
print(v)