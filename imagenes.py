#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 18:37:50 2021
@author: debernal
"""
import cv2
import numpy as np

def rotarcanon(angle):
    cañon = cv2.imread('img/base_rueda1.png',-1)
    ancho = cañon.shape[1]
    alto = cañon.shape[0]
    print(cañon.shape)
    M = cv2.getRotationMatrix2D((ancho//2,alto//2), angle, 1)
    cañon = cv2.warpAffine(cañon,M,(ancho,alto))

    base = cv2.imread('img/base_rueda.png',-1)
    filas,columnas,canales = base.shape

    base=cv2.addWeighted(cañon[0:0+filas, 0:0+columnas],1,base,1,0)

    cañon[0:0+filas, 0:0+columnas ] = base

    #cv2.imwrite('adsasd',base)
    cv2.imwrite('Salidasa.png',base)
    return

rotarcanon(90)    