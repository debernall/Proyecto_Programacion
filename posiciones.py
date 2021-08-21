#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:31:55 2021

@author: debernal
"""

from numpy import sin,cos,tan,arctan,arctan2,sqrt,arange,where,copy,concatenate
from math import pi
from matplotlib.pyplot import plot,show


def Tiempo(v0,g,theta0,y0,xlim,x0,yliminf,ylim):                                                     #Calcula el tiempo final dadas unas condiciones iniciales
    if g>0.1:
        tf=(v0/g)*(sin(theta0)+sqrt(((sin(theta0))**2)+((2*g*(y0-yliminf))/(v0**2))))
    elif theta0==pi/2:
        tf=(ylim-y0)/(v0*sin(theta0))
    else:
        tf=(xlim-x0)/(v0*cos(theta0))
        #print(tf)
    return tf

def Distancia(x,x0,y,y0):                                                       #Calcula un vector con distancias a un punto
    d=sqrt(((x-x0)**2)+((y-y0)**2))
    return d

def Vectorx(x0,v0,theta0,t):                                                    #Calcula el vector x
    x=x0+(v0*t*cos(theta0))
    return x

def Vectory(y0,v0,theta0,g,t):                                                  #Calcula el vector y
    y=y0+(v0*t*sin(theta0))-((g*(t**2))/2)
    return y

def Thetaf(theta,g,t,v0):                                                       #Calcula el angulo de impacto
    thetaf = arctan((tan(theta))-((g*t)/(v0*cos(theta))))
    return thetaf

def Velocidadf(v0,g,t,theta):                                                   #Calcula la velocidad de impacto
    v = sqrt((v0**2)+((g**2)*(t**2))-(2*g*t*v0*sin(theta)))
    return v

def graficar(impactos,x,y):
    for i in range(len(impactos)):
        gamma=arange(0,pi*2,0.0001)
        x1=(impactos[i][2]*cos(gamma))
        y1=(impactos[i][2]*sin(gamma))
        plot(-x1+impactos[i][0],-y1+impactos[i][1])
        plot(x,y)
    show()
    return

def posiciones(x0,y0,theta0,v0,g,e,xlim,ylim,yliminf,epsilon,impactos,max_rebotes):
    if g<0.1:
        g=0
        
    x_f=[]
    y_f=[]
    t_f=[]
    #x0=0                            #POSICION INICIAL
    #y0=6
    #theta0=1.6*math.pi/4            #ANGULO DE LANZAMIENTO
    #v0=14                           #MAGNITUD DE VELOCIDAD INICIAL
    #g=10                            
    t0=0
    #e=0.8                           #FACTOR DE PERDIDA DE VELOCIDAD
    f=True                          #TRUE: AVANZA EN SENTIDO X+
    alpha=0                         #ANGULO MEDIDA DESDE LA HORIZONTAL EN SENT POSTIVO DEL PUNTO DE IMPACTO EN LA CIRCUNF
    beta=0                          #ANGULO DE IMPACTO MEDIDA DESDE LA NORMAL AL PUNTO DE IMPACTO EN LA CIRCUNF
    
    #xlim=100                        #LONGITUD MAXIMA DEL TABLERO EN X
    #epsilon=0.0001                  #ESPACIAMIENTO DEL VECTOR TIEMPO
    tff=0
    #impactos=((20,3,1.1,True),(35,4,1,False),(10,8,2,False))    #VECTOR CON LOS CENTRO Y RADIOS DE LOS OBSTACULOS, True LO CONVIERTE EN OBJETIVO
    impacto = False
    objetivo=False
    tt=0
    while (x0<xlim and not(objetivo)) or (not(x0<xlim) and objetivo):                                                                  #MIENTRAS LA POSICION NUEVA A CALCULAR SEA MENOR A LA MAXIMA PERMITIDA
        
        tf=Tiempo(v0,g,theta0,y0,xlim,x0,yliminf,ylim)                                                   #CALCULA LOS VECTORES, t,x,y
        t=arange(t0,tf,epsilon)
        x=Vectorx(x0,v0,theta0,t)
        y=Vectory(y0,v0,theta0,g,t)
        
        vdistancia=[]                                                               #distancias hasta el centro de cada obstaculo
        for i in impactos:
            distancia=Distancia(x,i[0],y,i[1])-i[2]                                 #CALCULA LAS DISTANCIAS AL BORDE DE CADA OBSTACULO
            vdistancia.append(distancia)                                            #GUARDA EN UN VECTOR LAS DISTANCIAS
        
        if len(distancia)==0:
            break    
        
        aux=[]
        #print("asedasd",distancia)
        #print(t)
        for i in range(len(vdistancia)):
            mdis = min(vdistancia[i])                                               #CALCULA EL MINIMO DE CADA VECTOR DISTANCIA AL BORDE
            if mdis<0:                                                              #SI DISTANCIA ES MENOR A CERO YA HA IMPACTADO
                impacto=True
                k=where(vdistancia[i]<=0)[0][0]                                  #ENCUENTRA EL PRIMER MINIMO LOCAL DE DISTANCIA
                objetivo=False
                if impactos[i][-1]==True:                                           #SI EL OBSTACULO ES EL OBJETIVO
                    objetivo=True
                    kaux=where(vdistancia[i]<=0)[0]
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
        if len(aux2)!=0:                                                            #SI EL VECTOR DE POSICIONES X DE IMPACTO ES VACIO
            if f == True:                                                           #SI LA DIRECCIÓN ES ADELANTE SE ELIGE LA DE MENOR X
                xc=min(aux2)                                                        
                kc=where(x==xc)[0][0]
                a=where(aux2==xc)[0][0]       
                vdis_i=aux3[a]
            else:
                xc=max(aux2)                                                        #SI LA DIRECCION ES HACIA ATRAS, ELIGE LA DE MAYOR DISTANCIA EN X
                kc=where(x==xc)[0][0]
                a=where(aux2==xc)[0][0]       
                vdis_i=aux3[a]
        else:                                                                       #SI NO SE ENCUENTRA CON NINGUN OBSTACULO:
            if objetivo==False:
                kc=len(t)                    
                vdis_i=-1
    
        xc=copy(x[:kc])
        yc=copy(y[:kc])
        tc=copy(t[:kc])
        vc=Velocidadf(v0,g,tc[-1],theta0)
        if theta0>0 and theta0<(pi/2):
            thetac=arctan(tan(theta0)-((g*tc[-1])/(v0*cos(theta0))))
            if thetac<0:
                thetac=2*pi+thetac
    
        else:
            thetac=pi+arctan(tan(theta0)-((g*tc[-1])/(v0*cos(theta0))))
            
        alpha=arctan2((yc[-1]-impactos[vdis_i][1]),(xc[-1]-impactos[vdis_i][0]))
        if alpha<0:
            alpha=2*pi+alpha
        
        if thetac>pi:
            beta=thetac-pi
        else:
            beta=thetac+pi
            
    
        xaux1=cos(beta)
        yaux1=sin(beta)
        xaux2=(xaux1*cos(alpha))+(yaux1*sin(alpha))
        yaux2=(-xaux1*sin(alpha))+(yaux1*cos(alpha))
        beta=arctan2(yaux2,xaux2)
        if beta<0:
            phi=-arctan2(5*yaux2,7*e*xaux2)
        elif beta>=0:
            phi=-arctan2(5*yaux2,7*e*xaux2)
            
        xaux3=cos(phi)
        yaux3=sin(phi)
        xaux4=(xaux3*cos(alpha))+(-yaux3*sin(alpha))
        yaux4=(xaux3*sin(alpha))+(yaux3*cos(alpha))
        
        if vdis_i!=-1:
            theta0=arctan2(yaux4,xaux4)
            v0=vc
            if theta0<0:
                theta0=pi*2+theta0
        else:
            if objetivo==False:
                if theta0<0:
                    theta0=pi+arctan((5/(7*e))*(tan(theta0)-((g*tf)/(v0*cos(theta0)))))
                    f=False
                else:
                   # print("asdas!",g,theta0,tf,e,(v0*np.cos(theta0)),"adsdasad")
                    theta0=-arctan((5/(7*e))*(tan(theta0)-((g*tf)/(v0*cos(theta0)))))
                    v0=e*vc
    
    
        x0=xc[-1]
        y0=yc[-1]
        t0=0
    
        if tt>max_rebotes:
            x0=xlim+1
        elif x0<0:
            x0=xlim+1
        elif g==0:
            x0=xlim+1
        tt+=1                                                                       #CONTADOR DE MAXIMOS MOVIMIENTOS
        sxliminf=where(xc<0)[0]
        sxlimsup=where(xc>xlim)[0]
        sylimsup=where(yc>ylim)[0]
        if len(sxliminf)!=0:
            kc=sxliminf[0]
            xc=copy(xc[:kc])
            yc=copy(yc[:kc])
            tc=copy(tc[:kc])
            x0=xlim+1
        elif len(sxlimsup)!=0:
            kc=sxlimsup[0]
            xc=copy(xc[:kc])
            yc=copy(yc[:kc])
            tc=copy(tc[:kc])
            x0=xlim+1
        elif len(sylimsup)!=0:
            kc=sylimsup[0]
            xc=copy(xc[:kc])
            yc=copy(yc[:kc])
            tc=copy(tc[:kc])
            x0=xlim+1
        if t_f!=[]:
            tff=t_f[-1]    
        tcc=tff+tc    
        x_f=concatenate((x_f,xc))
        y_f=concatenate((y_f,yc))
        t_f=concatenate((t_f,tcc))
        #graficar(impactos,xc,yc)
        #plt.plot(yc)
        #LIMITES

        
    return (x_f,y_f,t_f,impactos)


#VARIABLES NECESARIAS PARA OBTENER LOS VECTORES POSICION
# x0=0                            #POSICION INICIAL
# y0=0
# theta0=0.9            #ANGULO DE LANZAMIENTO
# v0=13                           #MAGNITUD DE VELOCIDAD INICIAL
# g=10                            
# e=0.8                           #FACTOR DE PERDIDA DE VELOCIDAD
# xlim=4000                        #LONGITUD MAXIMA DEL TABLERO EN X
# ylim=10000
# epsilon=0.01                  #ESPACIAMIENTO DEL VECTOR TIEMPO
# impactos=((20,3,1.1,False),(20,5,1,True),(10,8,2,False))    #VECTOR CON LOS CENTRO Y RADIOS DE LOS OBSTACULOS, True LO CONVIERTE EN OBJETIVO
# max_rebotes=10
# yliminf=0


# a=posiciones(x0,y0,theta0,v0,g,e,xlim,ylim,yliminf,epsilon,impactos,max_rebotes)
# graficar(a[3],a[0],a[1])
# for u in a[2]:
#     print(u)
