# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
import sys

yellow=(245, 245, 66)
green=(22,234,72)
blue=(2,12,207)

def crear_boton(pantalla,boton,palabra):                #Función para crear botones como los de la intro
    
    letra1 = pygame.font.SysFont('ravie', 30)       #Fuente de los botones
    if boton.collidepoint(pygame.mouse.get_pos()):    #Cambia el color del boton si el cursor está sobre él  
        pygame.draw.rect(pantalla,yellow,boton,0)
    else:
        pygame.draw.rect(pantalla,green,boton,0)      #Dibuja el boton cuando el cursor no está encima
    texto=letra1.render(palabra,True,blue)      #Genera el texto del botón
    pantalla.blit(texto,(boton.x+(boton.width-texto.get_width())/2,boton.y+(boton.height-texto.get_height())/2))    #Pone el botón en la pantalla y centra el texto.

def crear_cuadro_de_texto(pantalla,cuadro,texto,fuente,color_fondo,color_texto):      #Funcion para realizar cualquier tipo de cuadro de texto
    pygame.draw.rect(pantalla,color_fondo,cuadro,0)
    txt=fuente.render(texto,True,color_texto)
    pantalla.blit(txt,(cuadro.x+(cuadro.width-txt.get_width())/2,cuadro.y+(cuadro.height-txt.get_height())/2))

def intro_game(): #Pantalla de intro
    intro=True
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    pygame.display.set_caption('Titulo')
    
    intro_background = pygame.image.load("fondo_intro.jpg") 
    screen.blit(intro_background,(0,0))

    
     
    letra = pygame.font.SysFont('ravie', 90)                 #Genera la fuente del primer texto      
    imagenTexto = letra.render('Título ',True, blue,green )  #Genera la imagen con el texto                             
    rectanguloTexto = imagenTexto.get_rect()                 
    rectanguloTexto.centerx = screen.get_rect().centerx     #Ubica el texto
    rectanguloTexto.centery = 320
    screen.blit(imagenTexto, rectanguloTexto)   #Pone la imagen con el texto en el programa

    
    play=pygame.Rect(screen.get_rect().centerx-150/2,450,150,50)        #Figuras de los botones jugar y salir
    exit=pygame.Rect(screen.get_rect().centerx-150/2,550,150,50)

    while(intro):                           
        for event in pygame.event.get():            
            if event.type == pygame.QUIT  or event.type==pygame.K_ESCAPE:           #Permite salir del juego desde la intro
                pygame.quit()
                quit()

            elif event.type==pygame.K_ESCAPE:   #Tecla q o esc sale del juego
                pygame.quit()
                quit()

            elif event.type==MOUSEBUTTONDOWN and event.button==1:       #Si se hace click derecho:

                if play.collidepoint(pygame.mouse.get_pos()):           #Si el click se hizo sobre el botón jugar, continuar con el juego
                    intro=False
                elif exit.collidepoint(pygame.mouse.get_pos()):         #Si el click se hiz en salir...
                    pygame.quit()
                    quit()
                    
        crear_boton(screen,play,'Jugar')        #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima
        crear_boton(screen,exit,'Salir')
        pygame.display.flip()
               
            

def rotate(surface, angle):
    rotated_surface=pygame.transform.rotozoom(surface,angle,1)
    rotated_rect = rotated_surface.get_rect(center=(64,537))
    return rotated_surface,rotated_rect

def main():
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    clock=pygame.time.Clock()
    pygame.display.set_caption('Titulo')
    
    #CARGA DE IMAGENES
    
    plano = pygame.image.load("plano.jpg")          #Imagen de fondo
    bola=pygame.image.load("bolacañon.png")       #Imagen de bala
    cañon=pygame.image.load("cañonx.png")          #Imagen de cañon
    recorte=pygame.image.load("planorecortado.jpg")    #Imagen recortada del fondo, que va entre el cañon y la bola para que no se vea la bola cuando no se ha disparado aun.
    explosion=pygame.image.load("explosión.png")    #imagen de la Explosón al disparar
    cuadro_angulo=pygame.Rect(0,0,250,50)
    letra_cuadro_angulo=pygame.font.SysFont('arial', 30) 
    
    #POSICION DE IMAGENES Y VARAIABLES A UTILIZAR
    
    
    screen.blit(plano,(0,0))
    
    screen.blit(recorte,(0,473))                   #Carga la imagen de fondo
   
    screen.blit(cañon,(0,473))                     #Carga la imagen del cañon
    pygame.display.flip()                           #Superpone las imagenes
    running=True                                    #Variable que mantiene activo el juego
    pos= 0,473                                    #Declaración de posición inicial de la bala
    pos1=-0,473                                   #Posición de la explosión antes de disparar
    step= 0,0 
                                        #vector velocidad
    angle=-22                                         #Declaración de variable ángulo del cañon
    speedangle=0                                    #Variable que almacena la rotación del cañon
                                                
    n=0                                             #
    v0=50                                       #Velocidad inicial
    t=0                                             #Variable de tiempo
    while(running):
        ns=clock.tick(30)                           #Periodo de recarga de imagen
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:           #Permite salir del juego
                running = False
            
            elif event.type == pygame.KEYDOWN:      #Evento presionar tecla
               if event.key==pygame.K_SPACE:        #Tecla espacio 
                   v_x0=v0*np.cos(np.radians(angle+22))                            #Velocidad inicial en x
                   v_y0=-v0*np.sin(np.radians(angle+22))                           #Velocidad inicial en y(Es negativa porque el pixel (0,0) se encuentra en la esquina sup izq)           
                   step=v_x0,v_y0                   #Tras presionar la tecla espacio 
                   n=10/ns
                   pos1=(150,400)                   #posición de la explosión al disparar
               elif event.key==pygame.K_LEFT:       #Tecla izquierda rotación en sentido positivo
                   speedangle=1
               elif event.key==pygame.K_RIGHT:      #Tecla derecha rotación en sentido negativo
                   speedangle=-1
               elif event.key==pygame.K_ESCAPE:     #Tecla escape sale del juego
                   running = False
            
            elif event.type == pygame.KEYUP:        #Eventos dejar de presionar tecla
               if event.key==pygame.K_SPACE:
                   pos1=(0,473)
               if event.key==pygame.K_LEFT:         #Dejar de presionar tecla izquierda detiene la rotación
                   speedangle=0
               elif event.key==pygame.K_RIGHT:      #Dejar de presionar tecla derecha detiene la rotación
                   speedangle=0
            
                
        screen.blit(plano,(0,0))                    #Carga la imagen de fondo tras cada paso del ciclo while
        screen.blit(bola,pos)                     #Carga la imagen de la bala
        pos=pos[0]+step[0],pos[1]+step[1]+((9.8/2)*(t**2))                            #(x,y)=(x0+v_x0,y0+v_y0)
         
            
        
        t=t+n
        screen.blit(explosion,pos1)                 #carga imagen explosón disparar 
        screen.blit(recorte,(0,473))                #carga imagen del recorte para que no se vea la bola antes de disprar 
        
        angle=angle+speedangle                      #Incrementa el ángulo del cañon de acuerdo a las teclas presionadas
      
        image2_rotated , image2_rotated_rect = rotate(cañon,angle)             #Rota el cañon
        screen.blit(image2_rotated,image2_rotated_rect)                         #Carga la imagen del cañon rotado
        
       
        #REBOTES DE LA BOLA CUANDO IMPACTA CONTRA EL PISO O COSTADOS
        if pos[0]>948 or pos[0]<0 :
            step= -step[0],step[1]
         
        if pos[1]>=540 :
          #rebotar en la misma posición
          #step= 0,-step[1]-1
          #t=0
            
          #rebota y desliza horizontalmente  
           pos=(pos[0],540)
          
           #no funciona igual que step=0,0
           #step[0]==0
           #step[1]==0
            
           #la deja estatica dónde cae
           step=0,0
           
           #rebota infitimante
           #step[1]==-step[1]
           t=0
           n=0
            
        crear_cuadro_de_texto(screen,cuadro_angulo,'Ángulo:'+str(angle),letra_cuadro_angulo,(0,0,0),(255,255,255))   #Agrega un cuadro de texto con el angulo.
       
            
                                    #El incremento 0.05 viene dado de la tasa tiempo_real/tiempo_maquina
        print(angle+22)
        pygame.display.flip()                                                   #Hace visibles las imagenes cargadas

        
intro_game()        #Ejecución de la intro
main()                                                                          #Ejecución del juego

#La pelota rebote, no solo paredes rigidas
#Colocar los limites
#Pantalla de inicio y de game over                                 Nelson,
#Cambiar el planeta del disparo, niveles
#Incluir la resistencia del aire y la superficie de aterrizaje
#Rotacion del cañon y la bola detras de la imagen del cañon        ... se hizo la bola detrás del cañon
#Cambiar los nombres de las variables de las imagenes   ...ya se hizo
#Cambiar el angulo inicial a negativo en lugar de cero  ...ya se hizo
#Colocar una barra para aumentar la velocidad
#Rotacion usando otras librerias
#cómo hacer para rebotar
#cómo hacer para preguntar la velocidad
#como rotar el cañon sobre el eje de la rueda
