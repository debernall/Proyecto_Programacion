#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 00:19:12 2021

@author: debernal
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi

def runge_kutta(f,g,x0,y0,vx0,vy0,a,b,h):
    t=np.arange(a,b+h,h)
    n=len(t)
    x=np.zeros(n)
    y=np.zeros(n)
    vx=np.zeros(n)
    vy=np.zeros(n)
    x[0]=x0
    y[0]=y0
    vx[0]=vx0
    vy[0]=vy0
    for i in range(n-1):
        k1=h*vx[i]
        l1=h*f(x[i],y[i],vx[i],vy[i],t[i])
        q1=h*vy[i]
        m1=h*g(x[i],y[i],vx[i],vy[i],t[i])
        
        k2=h*(vx[i]+(1/2)*l1)
        l2=h*f(x[i]+(1/2)*k1,y[i]+(1/2)*q1,vx[i]+(1/2)*l1,vy[i]+(1/2)*m1,t[i]+(1/2)*h)
        q2=h*(vy[i]+(1/2)*m1)
        m2=h*g(x[i]+(1/2)*k1,y[i]+(1/2)*q1,vx[i]+(1/2)*l1,vy[i]+(1/2)*m1,t[i]+(1/2)*h)
        
        k3=h*(vx[i]+(1/2)*l2)
        l3=h*f(x[i]+(1/2)*k2,y[i]+(1/2)*q2,vx[i]+(1/2)*l2,vy[i]+(1/2)*m2,t[i]+(1/2)*h)
        q3=h*(vy[i]+(1/2)*m2)
        m3=h*g(x[i]+(1/2)*k2,y[i]+(1/2)*q2,vx[i]+(1/2)*l2,vy[i]+(1/2)*m2,t[i]+(1/2)*h)
        
        k4=h*(vx[i]+l3)
        l4=h*f(x[i]+k3,y[i]+q3,vx[i]+l3,vy[i]+m3,t[i]+h)
        q4=h*(vy[i]+m3)
        m4=h*g(x[i]+k3,y[i]+q3,vx[i]+l3,vy[i]+m3,t[i]+h)
        
        x[i+1]=x[i]+(1/6)*(k1+2*k2+2*k3+k4)
        y[i+1]=y[i]+(1/6)*(q1+2*q2+2*q3+q4)
        vx[i+1]=vx[i]+(1/6)*(l1+2*l2+2*l3+l4)
        vy[i+1]=vy[i]+(1/6)*(m1+2*m2+2*m3+m4)
        
    return t,x,y,vx,vy

def Distancia(x,x0,y,y0):                                                       #Calcula un vector con distancias a un punto
    d=np.sqrt(((x-x0)**2)+((y-y0)**2))
    return d

def graficar(impactos,x,y):
    for i in range(len(impactos)):
        gamma=np.arange(0,pi*2,0.0001)
        x1=(impactos[i][2]*np.cos(gamma))
        y1=(impactos[i][2]*np.sin(gamma))
        plt.plot(-x1+impactos[i][0],-y1+impactos[i][1])
        plt.plot(x,y)
    plt.show()
    return

def parabolaseguridad(x0,y0,theta0,v0,g,xlim,ylim,epsilon,b,tipo):
    if tipo==0:
        F=lambda x,y,vx,vy,t: 0
        G=lambda x,y,vx,vy,t: -g
    elif tipo==1:
        F=lambda x,y,vx,vy,t: -b*vx
        G=lambda x,y,vx,vy,t: -g-b*vy
    elif tipo==2:
        F=lambda x,y,vx,vy,t: -b*vx*np.sqrt(vx**2+vy**2)
        G=lambda x,y,vx,vy,t: -g-b*vy*np.sqrt(vx**2+vy**2)
    
    t,x,y,vx,vy=runge_kutta(F,G,x0,y0,v0*np.cos(theta0),v0*np.sin(theta0),0,100,epsilon)
    if g!=0:
        if max(y)<ylim:
            aux=True
        else:
            aux=False
    else:
        aux=True
    return aux


        
def calc_vect(x0,y0,theta0,v0,g,e,xlim,ylim,yliminf,epsilon,impactos,max_rebotes,b,tipo):       
    x_f=[]
    y_f=[]
    t_f=[]
    t0=0
    f=True                          #TRUE: AVANZA EN SENTIDO X+
    alpha=0                         #ANGULO MEDIDA DESDE LA HORIZONTAL EN SENT POSTIVO DEL PUNTO DE IMPACTO EN LA CIRCUNF
    beta=0                          #ANGULO DE IMPACTO MEDIDA DESDE LA NORMAL AL PUNTO DE IMPACTO EN LA CIRCUNF
    tff=0
    impacto = False
    objetivo=False
    tt=0
    inf=False
    if tipo==0:
        F=lambda x,y,vx,vy,t: 0
        G=lambda x,y,vx,vy,t: -g
    elif tipo==1:
        F=lambda x,y,vx,vy,t: -b*vx
        G=lambda x,y,vx,vy,t: -g-b*vy
    elif tipo==2:
        F=lambda x,y,vx,vy,t: -b*vx*np.sqrt(vx**2+vy**2)
        G=lambda x,y,vx,vy,t: -g-b*vy*np.sqrt(vx**2+vy**2)
    
    while (x0<xlim and not(objetivo)) or (not(x0<xlim) and objetivo):               #MIENTRAS LA POSICION NUEVA A CALCULAR SEA MENOR A LA MAXIMA PERMITIDA 
        t,x,y,vx,vy=runge_kutta(F,G,x0,y0,v0*np.cos(theta0),v0*np.sin(theta0),0,100,epsilon)
        vdistancia=[]                                                               #distancias hasta el centro de cada obstaculo
        for i in impactos:
            distancia=Distancia(x,i[0],y,i[1])-i[2]                                 #CALCULA LAS DISTANCIAS AL BORDE DE CADA OBSTACULO
            vdistancia.append(distancia)                                            #GUARDA EN UN VECTOR LAS DISTANCIAS
        
        if len(distancia)==0:                               
            break    
        
        aux=[]

        for i in range(len(vdistancia)):
            mdis = min(vdistancia[i])                                               #CALCULA EL MINIMO DE CADA VECTOR DISTANCIA AL BORDE
            if mdis<0:                                                              #SI DISTANCIA ES MENOR A CERO YA HA IMPACTADO
                impacto=True
                k=np.where(vdistancia[i]<=0)[0][0]                                  #ENCUENTRA EL PRIMER MINIMO LOCAL DE DISTANCIA
                objetivo=False
                if impactos[i][-1]==True:                                           #SI EL OBSTACULO ES EL OBJETIVO
                    objetivo=True
                    kaux=np.where(vdistancia[i]<=0)[0]
                    k=int(kaux[0]+((kaux[-1]-kaux[0])/2))                           #ENCUENTRA LA POSICION MEDIA DE ACIERTA EN EL OBJETIVO
                xk=x[k]
                aux.append((xk,i,impacto))                                          #ADICIONA A UN VECTOR LAS POSICIONES DE IMPACTO A CADA OBSTACULO
            else:
                impacto=False
                aux.append((x[-1],i,impacto))                                       #SI NO HAY IMPACTO ADICIONA LAS POSICIONES DE FINAL DE PARABOLA
    
        #ENCUENTRA EL OBSTACULO CON EL QUE PRIMERO IMPACTA
        aux2=[]
        aux3=[]
        
        for i in range(len(aux)):
            if aux[i][-1]==True:
                aux2.append(aux[i][0])                                              #GUARDA LAS POSICIONES X DE IMPACTO
                aux3.append(aux[i][-2])                                             #GUARDA EL NUMERO DEL OBSTACULO U OBJETIVO
        print(y)
        if len(aux2)!=0:                                                            #SI EL VECTOR DE POSICIONES X DE IMPACTO ES VACIO
            if f == True:                                                           #SI LA DIRECCIÓN ES ADELANTE SE ELIGE LA DE MENOR X
                xc=min(aux2)                                                        
                kc=np.where(x==xc)[0][0]
                a=np.where(aux2==xc)[0][0]       
                vdis_i=aux3[a]
            else:
                xc=max(aux2)                                                        #SI LA DIRECCION ES HACIA ATRAS, ELIGE LA DE MAYOR DISTANCIA EN X
                kc=np.where(x==xc)[0][0]
                a=np.where(aux2==xc)[0][0]       
                vdis_i=aux3[a]
        elif min(y)>=0:
            kc=np.where(y>ylim)[0][0]
            inf=True
        else:                                                                       #SI NO SE ENCUENTRA CON NINGUN OBSTACULO:
            if objetivo==False:
                kc=np.where(y[1:]<0.001)[0][0]                   
                vdis_i=-1
            
        xc=np.copy(x[:kc])
        yc=np.copy(y[:kc])
        tc=np.copy(t[:kc])
        vc=np.sqrt((vx[kc])**2+(vy[kc])**2)
        if inf==False:
            if theta0>0:
                thetac=np.arctan2(y[kc+1]-y[kc],x[kc+1]-x[kc]) 
                if thetac<0:
                        thetac=2*pi+thetac
            else:
                thetac=pi+np.arctan2(y[kc+1]-y[kc],x[kc+1]-x[kc])
                
            alpha=np.arctan2((y[kc]-impactos[vdis_i][1]),(x[kc]-impactos[vdis_i][0]))
            if alpha<0:
                alpha=2*pi+alpha
            
            if thetac>pi:
                beta=thetac-pi
            else:
                beta=thetac+pi
                
            if vdis_i==-1:
                alpha=pi/2
                
            xaux1=np.cos(beta)
            yaux1=np.sin(beta)
            xaux2=(xaux1*np.cos(alpha))+(yaux1*np.sin(alpha))
            yaux2=(-xaux1*np.sin(alpha))+(yaux1*np.cos(alpha))
            beta=np.arctan2(yaux2,xaux2)
            if beta<0:
                phi=-np.arctan2(5*yaux2,7*e*xaux2)
            elif beta>=0:
                phi=-np.arctan2(5*yaux2,7*e*xaux2)
            xaux3=np.cos(phi)
            yaux3=np.sin(phi)
            xaux4=(xaux3*np.cos(alpha))+(-yaux3*np.sin(alpha))
            yaux4=(xaux3*np.sin(alpha))+(yaux3*np.cos(alpha))
            v0=e*vc
            theta0=np.arctan2(yaux4,xaux4)
            if theta0<0:
                theta0=pi*2+theta0
            
            
            if theta0>(pi/2) and theta0<(3*pi/2):
                f=False
            else:
                f=True
            
            x0=xc[-1]
            y0=yc[-1]
        
            if tt>max_rebotes:
                x0=xlim+1
            elif x0<0:
                x0=xlim+1
            elif g==0:
                x0=xlim+1
        
        else:
            x0=xlim+1
            
        sxliminf=np.where(xc<0)[0]
        sxlimsup=np.where(xc>xlim)[0]
        sylimsup=np.where(yc>ylim)[0]
        
        if len(sxliminf)!=0:
            kc=sxliminf[0]
            xc=np.copy(xc[:kc])
            yc=np.copy(yc[:kc])
            tc=np.copy(tc[:kc])
            x0=xlim+1
        elif len(sxlimsup)!=0:
            kc=sxlimsup[0]
            xc=np.copy(xc[:kc])
            yc=np.copy(yc[:kc])
            tc=np.copy(tc[:kc])
            x0=xlim+1
        elif len(sylimsup)!=0:
            kc=sylimsup[0]
            xc=np.copy(xc[:kc])
            yc=np.copy(yc[:kc])
            tc=np.copy(tc[:kc])
            x0=xlim+1
        if tt!=0:
            tff=t_f[-1]   
            
        tcc=tff+tc    
        x_f=np.concatenate((x_f,xc))
        y_f=np.concatenate((y_f,yc))
        t_f=np.concatenate((t_f,tcc))

        tt+=1

    return (x_f,y_f,t_f,impactos)


#VARIABLES NECESARIAS PARA OBTENER LOS VECTORES POSICION
# x0=0                            #POSICION INICIAL
# y0=0
# theta0=1.5            #ANGULO DE LANZAMIENTO
# v0=14                           #MAGNITUD DE VELOCIDAD INICIAL
# g=10                            
# e=0.9                           #FACTOR DE PERDIDA DE VELOCIDAD
# xlim=20                        #LONGITUD MAXIMA DEL TABLERO EN X
# ylim=10
# epsilon=0.01                  #ESPACIAMIENTO DEL VECTOR TIEMPO
# impactos=((20,9,1.1,False),(16,4,1,True),(7,4,1,False))    #VECTOR CON LOS CENTRO Y RADIOS DE LOS OBSTACULOS, True LO CONVIERTE EN OBJETIVO
# max_rebotes=10
# yliminf=0
# b=0.01
# tipo=0

# a=calc_vect(x0,y0,theta0,v0,g,e,xlim,ylim,yliminf,epsilon,impactos,max_rebotes,b,tipo)
# graficar(a[3],a[0],a[1])
# est_pseg=parabolaseguridad(x0,y0,theta0,v0,g,xlim,ylim,epsilon,b,tipo)