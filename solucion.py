#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 08:39:01 2021

@author: debernal
"""

import numpy as np

g=1.46
theta=np.radians(48)
xf=143.5
yf=120.3
v=np.sqrt((g*xf)/(2*(((-yf*((np.cos(theta))**2)/(xf))+((np.sin(theta))*(np.cos(theta)))))))
print(v)