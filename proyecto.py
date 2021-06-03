# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import random
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN


yellow=(245, 245, 66)
green=(22,234,72)
blue=(2,12,207)
pygame.init()
letra1 = pygame.font.SysFont('ravie', 30) 

def crear_boton(pantalla,boton,palabra,fuente,color_fondo1,color_fondo2,color_texto):                #Función para crear botones como los de la intro

    if boton.collidepoint(pygame.mouse.get_pos()):    #Cambia el color del boton si el cursor está sobre él  
        pygame.draw.rect(pantalla,color_fondo2,boton,0)
    else:
        pygame.draw.rect(pantalla,color_fondo1,boton,0)      #Dibuja el boton cuando el cursor no está encima
    texto=fuente.render(palabra,True,color_texto)      #Genera el texto del botón
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

    
    play=pygame.Rect(screen.get_rect().centerx-350/2,450,350,50)        #Figuras de los botones jugar y salir
    exit=pygame.Rect(screen.get_rect().centerx-350/2,650,350,50)
    instructions=pygame.Rect(screen.get_rect().centerx-350/2,550,350,50)

    while(intro):                           
        for event in pygame.event.get():            
            if event.type == pygame.QUIT :           #Permite salir del juego desde la intro
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.type==pygame.K_ESCAPE:   #Tecla  esc sale del juego (NO ESTÁ FUNCIONANDO)
                    pygame.quit()
                    quit()

            elif event.type==MOUSEBUTTONDOWN and event.button==1:       #Si se hace click derecho:

                if play.collidepoint(pygame.mouse.get_pos()):           #Si el click se hizo sobre el botón jugar, continuar con el juego
                    intro=False
                    main()
                elif exit.collidepoint(pygame.mouse.get_pos()):         #Si el click se hiz en salir...
                    pygame.quit()
                    quit()
                    
        crear_boton(screen,play,'Jugar',letra1,green,yellow,blue)        #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima
        crear_boton(screen,exit,'Salir',letra1,green,yellow,blue)
        crear_boton(screen,instructions,'Instrucciones',letra1,green,yellow,blue)
        pygame.display.flip()

def outro():
    pygame.init()
    game_over=True
    screen= pygame.display.set_mode((948,720))
    pygame.display.set_caption('Titulo')
    
    intro_background = pygame.image.load("fondo_intro.jpg") 
    screen.blit(intro_background,(0,0))

    
     
    letra = pygame.font.SysFont('ravie', 90)                 #Genera la fuente del primer texto      
    imagenTexto = letra.render('Fin del juego ',True, blue,green )  #Genera la imagen con el texto                             
    rectanguloTexto = imagenTexto.get_rect()                 
    rectanguloTexto.centerx = screen.get_rect().centerx     #Ubica el texto
    rectanguloTexto.centery = 320
    screen.blit(imagenTexto, rectanguloTexto)   #Pone la imagen con el texto en el programa

    
    replay=pygame.Rect(screen.get_rect().centerx-350/2,450,350,50)        #Figuras de los botones volver a jugar y salir
    exit1=pygame.Rect(screen.get_rect().centerx-350/2,650,350,50)
    credits=pygame.Rect(screen.get_rect().centerx-350/2,550,350,50)

    while(game_over):                           
        for event in pygame.event.get():            
            if event.type == pygame.QUIT :           #Permite salir del juego desde la outro
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.type==pygame.K_ESCAPE:   #Tecla  esc sale del juego (NO ESTÁ FUNCIONANDO)
                    pygame.quit()
                    quit()

            elif event.type==MOUSEBUTTONDOWN and event.button==1:       #Si se hace click derecho:

                if replay.collidepoint(pygame.mouse.get_pos()):           #Si el click se hizo sobre el botón volver a  jugar, vuelve a la intro
                    game_over=False
                    intro_game()
                elif exit1.collidepoint(pygame.mouse.get_pos()):         #Si el click se hiz en salir...
                    pygame.quit()
                    quit()
                    
        crear_boton(screen,replay,'Volver a jugar',letra1,green,yellow,blue)        #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima
        crear_boton(screen,exit1,'Salir',letra1,green,yellow,blue)
        crear_boton(screen,credits,'Créditos',letra1,green,yellow,blue)
        pygame.display.flip()        

def rotate(surface, angle):
    rotated_surface=pygame.transform.rotozoom(surface,angle,1)
    rotated_rect = rotated_surface.get_rect(center=(400,350))
    return rotated_surface,rotated_rect

def main():
    pygame.init()
    screen= pygame.display.set_mode((800,700))
    clock=pygame.time.Clock()
    pygame.display.set_caption('Titulo')
    
    #CARGA DE IMAGENES
    
    plano = pygame.image.load("enorme.jpg")          #Imagen de fondo
    planorect=plano.get_rect()
    bola=pygame.image.load("bolacañonpequeña.png")       #Imagen de bala
   
    cañon=pygame.image.load("cañon5.png")          #Imagen de cañon
  
    explosion=pygame.image.load("explosión.png")    #imagen de la Explosón al disparar
    objetivo=pygame.image.load("objetivop.png")
    cuadro_posicion_objetivo=pygame.Rect(0,100,350,50)
    cuadro_velocidad=pygame.Rect(0,50,350,50)
    letra_cuadro_velocidad=pygame.font.SysFont('arial',30)
    cuadro_angulo=pygame.Rect(0,0,250,50)
    letra_cuadro_angulo=pygame.font.SysFont('arial', 30) 
    
    #POSICION DE IMAGENES Y VARAIABLES A UTILIZAR
    posobjetivo= random.randrange(400,3840), random.randrange(-1300,350)
    
    posplano=0,-1300
    screen.blit(plano,posplano)
    
    #screen.blit(recorte,(0,473))                   #Carga la imagen de fondo
    poscañon=336,286
    #screen.blit(cañon,poscañon)                     #Carga la imagen del cañon
    pygame.display.flip()                           #Superpone las imagenes
    running=True                                    #Variable que mantiene activo el juego
    posimg=400,350
    distancia=((posobjetivo[0]-posimg[0])/10),-((posobjetivo[1]-posimg[1])/10)
    pos= -400,-350                                    #Declaración de posición inicial de la bala
    pos1=-400,-350                                   #Posición de la explosión antes de disparar
    step= 0,0 
                                        #vector velocidad
    angle=0                                        #Declaración de variable ángulo del cañon
    speedangle=0                                    #Variable que almacena la rotación del cañon
                                                
    n=0                                             #
    v0=0                                      #Velocidad inicial
    g=3.06
    vi=0
    speedv0=0
    t=0                                             #Variable de tiempo
    while(running):
        ns=clock.tick(30)                           #Periodo de recarga de imagen
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:           #Permite salir del juego
                pygame.quit()
                quit()
            
            elif event.type == pygame.KEYDOWN:      #Evento presionar tecla
               if event.key==pygame.K_SPACE:        #Tecla espacio 
                   v_x0=vi*np.cos(np.radians(angle))                            #Velocidad inicial en x
                   v_y0=-vi*np.sin(np.radians(angle))                           #Velocidad inicial en y(Es negativa porque el pixel (0,0) se encuentra en la esquina sup izq)           
                   step=v_x0,v_y0                   #Tras presionar la tecla espacio 
                   n=0.0303
                   #n=10/ns
                   pos= 400,350  
                   
                   pos1=(450,250)                   #posición de la explosión al disparar
               elif event.key==pygame.K_UP:       #Tecla izquierda rotación en sentido positivo
                   speedv0=1
               elif event.key==pygame.K_DOWN:      #Tecla derecha rotación en sentido negativo
                   speedv0=-1
                   
               elif event.key==pygame.K_LEFT:       #Tecla izquierda rotación en sentido positivo
                   speedangle=1
               elif event.key==pygame.K_RIGHT:      #Tecla derecha rotación en sentido negativo
                   speedangle=-1
               elif event.key==pygame.K_ESCAPE:     #Tecla escape sale del juego
                   running = False
                   outro()
            
            elif event.type == pygame.KEYUP:        #Eventos dejar de presionar tecla
               
               if event.key==pygame.K_UP:       #Tecla izquierda rotación en sentido positivo
                   speedv0=0
               elif event.key==pygame.K_DOWN:      #Tecla derecha rotación en sentido negativo
                   speedv0=0    
               elif event.key==pygame.K_LEFT:         #Dejar de presionar tecla izquierda detiene la rotación
                   speedangle=0
               elif event.key==pygame.K_RIGHT:      #Dejar de presionar tecla derecha detiene la rotación
                   speedangle=0
            
                
        screen.blit(plano,posplano)                    #Carga la imagen de fondo tras cada paso del ciclo while
                            
        posplano=posplano[0]-step[0],posplano[1]-step[1]-((g/2)*(t**2))                            #(x,y)=(x0+v_x0,y0+v_y0)
         
        screen.blit(objetivo,posobjetivo)
        posobjetivo=posobjetivo[0]-step[0],posobjetivo[1]-step[1]-((g/2)*(t**2))
        objetivorect=objetivo.get_rect(center=posobjetivo)
        screen.blit(explosion,pos1)                 #carga imagen explosón disparar 
        pos1=pos1[0]-step[0],pos1[1]-step[1]-((g/2)*(t**2))
        
        screen.blit(bola,pos)     #carga la imagen de la bola
        bolarect=bola.get_rect(center=pos)
        
        angle=angle+speedangle                      #Incrementa el ángulo del cañon de acuerdo a las teclas presionadas
        v0=v0 + speedv0
        vi=(v0*10)/32
        image2_rotated , image2_rotated_rect = rotate(cañon,angle)             #Rota el cañon
        poscañon=poscañon[0]-step[0],poscañon[1]-step[1]-((g/2)*(t**2))                            #(x,y)=(x0+v_x0,y0+v_y0)
        screen.blit(image2_rotated,poscañon)
                         
        t=t+n
        if bolarect.colliderect(objetivorect):
            step=0,0
            t=0
            
            print("colision")
        #REBOTES DE LA BOLA CUANDO IMPACTA CONTRA EL PISO O COSTADOS
        if posplano[0]<-3440 or posplano[0]>= 400 :
            step= -step[0],step[1]
         
        if posplano[1]<=-1300 :
           
           posplano=(posplano[0],-1300)
          
           step=0,0
           
           t=0
           
          
        crear_cuadro_de_texto(screen,cuadro_angulo,'Ángulo:'+str(angle)+"°",letra_cuadro_angulo,(0,0,0),(255,255,255))   #Agrega un cuadro de texto con el angulo.
        crear_cuadro_de_texto(screen,cuadro_velocidad,'Velocidad incial:'+str(v0)+"m/s",letra_cuadro_velocidad,(0,0,0),(255,255,255))
        crear_cuadro_de_texto(screen,cuadro_posicion_objetivo,'coord. obj.(x,y):'+str(distancia[0])+"m"","+str(distancia[1])+"m",letra_cuadro_velocidad,(0,0,0),(255,255,255))
                                    #El incremento 0.05 viene dado de la tasa tiempo_real/tiempo_maquina
        
        print(distancia,posobjetivo,vi)
        pygame.display.flip()                                                   #Hace visibles las imagenes cargadas

        
intro_game()        #Ahora desde la función intro_game se llama la función main y desde main se puede llamar el outro(por ahora con la tecla esc porque aun no se puede perder o ganar en el juego)                                                                    

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