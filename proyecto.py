# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import numpy as np


def rotate(surface, angle):
    rotated_surface=pygame.transform.rotozoom(surface,angle,1)
    rotated_rect = rotated_surface.get_rect(center=(64,537))
    return rotated_surface,rotated_rect

def main():
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    clock=pygame.time.Clock()
    pygame.display.set_caption('Juego grupo 3')
    
    #CARGA DE IMAGENES
    image = pygame.image.load("plano.jpg")          #Imagen de fondo
    image1=pygame.image.load("bolacañon.png")       #Imagen de bala
    image2=pygame.image.load("cañonx.png")          #Imagen de cañon
    image2_rect=image2.get_rect(center=(64,537))
    
    #POSICION DE IMAGENES
    screen.blit(image,(0,0))                        #Carga la imagen de fondo
    screen.blit(image2,(0,473))                     #Carga la imagen del cañon
    pygame.display.flip()                           #Superpone las imagenes
    running=True                                    #Variable que mantiene activo el juego
    pos= 110,460                                    #Declaración de posición inicial de la bala
    step= 0,0                                       #vector velocidad
    angle=0                                         #Declaración de variable ángulo del cañon
    speedangle=0                                    #Variable que almacena la rotación del cañon
    a=0                                             #
    n=0                                             #
    v0=40                                           #Velocidad inicial
    t=0                                             #Variable de tiempo
    
    while(running):
        ns=clock.tick(30)                           #Periodo de recarga de imagen
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:           #Permite salir del juego
                running = False
            
            elif event.type == pygame.KEYDOWN:      #Evento presionar tecla
               if event.key==pygame.K_SPACE:        #Tecla espacio 
                   v_x0=v0*np.cos(np.radians(angle))                            #Velocidad inicial en x
                   v_y0=-v0*np.sin(np.radians(angle))                           #Velocidad inicial en y(Es negativa porque el pixel (0,0) se encuentra en la esquina sup izq)
                   step=v_x0,v_y0                   #Tras presionar la tecla espacio 
                   n=0.2
               elif event.key==pygame.K_LEFT:       #Tecla izquierda rotación en sentido positivo
                   speedangle=1
               elif event.key==pygame.K_RIGHT:      #Tecla derecha rotación en sentido negativo
                   speedangle=-1
               elif event.key==pygame.K_ESCAPE:     #Tecla escape sale del juego
                   running = False
            
            elif event.type == pygame.KEYUP:        #Eventos dejar de presionar tecla
               if event.key==pygame.K_LEFT:         #Dejar de presionar tecla izquierda detiene la rotación
                   speedangle=0
               elif event.key==pygame.K_RIGHT:      #Dejar de presionar tecla derecha detiene la rotación
                   speedangle=0
            
                   
        screen.blit(image,(0,0))                    #Carga la imagen de fondo tras cada paso del ciclo while
       
        angle=angle+speedangle                      #Incrementa el ángulo del cañon de acuerdo a las teclas presionadas
      
        image2_rotated , image2_rotated_rect = rotate(image2,angle)             #Rota el cañon
        screen.blit(image2_rotated,image2_rotated_rect)                         #Carga la imagen del cañon rotado

        
        screen.blit(image1,pos)                     #Carga la imagen de la bala
        pos=pos[0]+step[0],pos[1]+step[1]+(5*(a**2))                            #(x,y)=(x0+v_x0,y0+v_y0)
        a=a+n
        #print(angle)
        t=t+0.033                                    #El incremento 0.05 viene dado de la tasa tiempo_real/tiempo_maquina
        
        pygame.display.flip()                                                   #Hace visibles las imagenes cargadas

        
        
main()#ahora si
