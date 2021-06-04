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


###############################    DECLARACIONES INICIALES        ##################################
yellow=(245, 245, 66)
green=(22,234,72)
blue=(2,12,207)
pygame.init()
letra1 = pygame.font.SysFont('ravie', 30) 

def crear_boton(pantalla,boton,palabra,fuente,color_fondo1,color_fondo2,color_texto):                #Función para crear botones como los de la intro

    if boton.collidepoint(pygame.mouse.get_pos()):                              #Cambia el color del boton si el cursor está sobre él  
        pygame.draw.rect(pantalla,color_fondo2,boton,0)
    else:
        pygame.draw.rect(pantalla,color_fondo1,boton,0)                         #Dibuja el boton cuando el cursor no está encima
    texto=fuente.render(palabra,True,color_texto)                               #Genera el texto del botón
    pantalla.blit(texto,(boton.x+(boton.width-texto.get_width())/2,boton.y+(boton.height-texto.get_height())/2))    #Pone el botón en la pantalla y centra el texto.

def crear_cuadro_de_texto(pantalla,cuadro,texto,fuente,color_fondo,color_texto):      #Funcion para realizar cualquier tipo de cuadro de texto
    pygame.draw.rect(pantalla,color_fondo,cuadro,0)
    txt=fuente.render(texto,True,color_texto)
    pantalla.blit(txt,(cuadro.x+(cuadro.width-txt.get_width())/2,cuadro.y+(cuadro.height-txt.get_height())/2))

def intro_game(): #Pantalla de intro
    intro=True
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    pygame.display.set_caption('JUEGO DE LANZAMIENTO')
    
    intro_background = pygame.image.load("fondo_intro.jpg") 
    screen.blit(intro_background,(0,0))

    
     
    letra = pygame.font.SysFont('ravie', 90)                                    #Genera la fuente del primer texto      
    imagenTexto = letra.render('JUEGO DE LANZAMIENTO',True, blue,green )                     #Genera la imagen con el texto                             
    rectanguloTexto = imagenTexto.get_rect()                 
    rectanguloTexto.centerx = screen.get_rect().centerx                         #Ubica el texto
    rectanguloTexto.centery = 320
    screen.blit(imagenTexto, rectanguloTexto)                                   #Pone la imagen con el texto en el programa

    
    play=pygame.Rect(screen.get_rect().centerx-350/2,450,350,50)                #Figuras de los botones jugar y salir
    exit=pygame.Rect(screen.get_rect().centerx-350/2,650,350,50)
    instructions=pygame.Rect(screen.get_rect().centerx-350/2,550,350,50)

    while(intro):                           
        for event in pygame.event.get():            
            if event.type == pygame.QUIT :                                      #Permite salir del juego desde la intro
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:                                 #Tecla  esc sale del juego (NO ESTÁ FUNCIONANDO)
                    pygame.quit()
                    quit()

            elif event.type==MOUSEBUTTONDOWN and event.button==1:               #Si se hace click derecho:

                if play.collidepoint(pygame.mouse.get_pos()):                   #Si el click se hizo sobre el botón jugar, continuar con el juego
                    intro=False
                    mundo.main(tierra)
                elif exit.collidepoint(pygame.mouse.get_pos()):                 #Si el click se hiz en salir...
                    pygame.quit()
                    quit()
                    
        crear_boton(screen,play,'Jugar',letra1,green,yellow,blue)               #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima
        crear_boton(screen,exit,'Salir',letra1,green,yellow,blue)
        crear_boton(screen,instructions,'Instrucciones',letra1,green,yellow,blue)
        pygame.display.flip()


#################################     CLASE MUNDO     ######################################
class mundo:
    
    def __init__(self):
        self.no_hago_nada=0
        # self.yellow=(245, 245, 66)
        # self.green=(22,234,72)
        # self.blue=(2,12,207)
        # self.letra1 = pygame.font.SysFont('ravie', 30) 
        
    
    def outro(self,titulo,estado):
        pygame.init()
        game_over=True
        screen= pygame.display.set_mode((948,720))
        pygame.display.set_caption(titulo)
        
        intro_background = pygame.image.load("fondo_intro.jpg") 
        screen.blit(intro_background,(0,0))
    
        letra = pygame.font.SysFont('ravie', 90)                                    #Genera la fuente del primer texto      
        imagenTexto = letra.render(estado,True,blue,green )              #Genera la imagen con el texto                             
        rectanguloTexto = imagenTexto.get_rect()                 
        rectanguloTexto.centerx = screen.get_rect().centerx                         #Ubica el texto
        rectanguloTexto.centery = 320
        screen.blit(imagenTexto, rectanguloTexto)                                   #Pone la imagen con el texto en el programa
    
        
        replay=pygame.Rect(screen.get_rect().centerx-350/2,450,350,50)              #Figuras de los botones volver a jugar y salir
        exit1=pygame.Rect(screen.get_rect().centerx-350/2,650,350,50)
        credits=pygame.Rect(screen.get_rect().centerx-350/2,550,350,50)
    
        while(game_over):                           
            for event in pygame.event.get():            
                if event.type == pygame.QUIT :                                      #Permite salir del juego desde la outro
                    pygame.quit()
                    quit()
    
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:                                 #Tecla  esc sale del juego (NO ESTÁ FUNCIONANDO)
                        pygame.quit()
                        quit()
    
                elif event.type==MOUSEBUTTONDOWN and event.button==1:               #Si se hace click derecho:
    
                    if replay.collidepoint(pygame.mouse.get_pos()):                 #Si el click se hizo sobre el botón volver a  jugar, vuelve a la intro
                        game_over=False
                        intro_game()
                    elif exit1.collidepoint(pygame.mouse.get_pos()):                #Si el click se hiz en salir...
                        pygame.quit()
                        quit()
                        
            crear_boton(screen,replay,'Volver a jugar',letra1,green,yellow,blue)    #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima
            crear_boton(screen,exit1,'Salir',letra1,green,yellow,blue)
            crear_boton(screen,credits,'Créditos',letra1,green,yellow,blue)
            pygame.display.flip()        
    
    def rotate(self,surface, angle):
        rotated_surface=pygame.transform.rotozoom(surface,angle,1)
        rotated_rect = rotated_surface.get_rect(center=(400,350))
        return rotated_surface,rotated_rect
    
    def nueva_pos(self,pos_inicial,v,t,g):
        pos_final=()
        pos_final=pos_inicial[0]-v[0],pos_inicial[1]-v[1]-((g/2)*(t**2))
        return pos_final
    
    def dibujar_img(self,list_img):
        screen= pygame.display.set_mode((800,700))
        for i in list_img:
            screen.blit(i[0],i[1])
        return 
           
    def f_rebote(self,step,r):
        step_nuevo=(step[0]/(r),step[1]/(r))
        return step_nuevo
     
    
    def main(self):
        #PROPIEDADES INICIALES PYGAME
        pygame.init()
        screen= pygame.display.set_mode((800,700))
        clock=pygame.time.Clock()
        #pygame.display.set_caption('JUEGO DE LANZAMIENTO')
        
        #CARGA DE IMAGENES
        plano = pygame.image.load("enorme.jpg")                                     #Imagen de fondo
        #planorect=plano.get_rect()
        bola=pygame.image.load("bolacañonpequeña.png")                              #Imagen de bala
        cañon=pygame.image.load("cañon5.png")                                       #Imagen de cañon
        explosion=pygame.image.load("explosión.png")                                #imagen de la Explosón al disparar
        objetivo=pygame.image.load("objetivop.png")
        
        #CARACTERISTICAS DE LOS CUADROS DE TEXTO
        cuadro_posicion_objetivo=pygame.Rect(0,100,350,50)
        cuadro_velocidad=pygame.Rect(0,50,350,50)
        letra_cuadro_velocidad=pygame.font.SysFont('arial',30)
        cuadro_angulo=pygame.Rect(0,0,250,50)
        letra_cuadro_angulo=pygame.font.SysFont('arial', 30)
        cuadro_posicion_tiempo=pygame.Rect(700,0,150,50)
        letra_cuadro_tiempo=pygame.font.SysFont('arial', 30)
        
        #POSICION DE IMAGENES Y VARIABLES A UTILIZAR
        posobjetivo= random.randrange(400,3840), random.randrange(-1300,350)
        posplano=0,-1300
        pos_canon=(336,286)
        
        #pygame.display.flip()                                                       #Superpone las imagenes
        running=True                                                                #Variable que mantiene activo el juego
        posimg=400,350
        distancia=((posobjetivo[0]-posimg[0])/10),-((posobjetivo[1]-posimg[1])/10)
        pos_bola= -400,-350                                                              #Declaración de posición inicial de la bala
        pos_expl=-400,-350                                                              #Posición de la explosión antes de disparar
        step= 0,0 
                                                                                    #vector velocidad
        angle=0                                                                     #Declaración de variable ángulo del cañon
        speedangle=0                                                                #Variable que almacena la rotación del cañon
                                                    
        n=0                                             #
        v0=0                                                                        #Velocidad inicial
        g=3.06
        vi=0
        speedv0=0
        t=0  
        t1=0                                                                       #Variable de tiempo
        colision=False
        disparo=False
        fact_perdida_choque=1.4
        
        while(running):
            ns=clock.tick(30)                                                       #Periodo de recarga de imagen
            for event in pygame.event.get():            
                if event.type == pygame.QUIT:                                       #Permite salir del juego
                    pygame.quit()
                    quit()
                
                
                #INTERACCIONES POR MEDIO DE TECLADO EN EL JUEGO
                elif event.type == pygame.KEYDOWN:                                  #Evento presionar tecla
                    if event.key==pygame.K_SPACE:                                    #Tecla espacio 
                        if colision==True:
                            step=(0,0)
                        elif disparo==False:
                            v_x0=vi*np.cos(np.radians(angle))                            #Velocidad inicial en x
                            v_y0=-vi*np.sin(np.radians(angle))                           #Velocidad inicial en y(Es negativa porque el pixel (0,0) se encuentra en la esquina sup izq)           
                            step=v_x0,v_y0                                               #Tras presionar la tecla espacio 
                            n=0.0303
                            #n=10/ns
                            pos_bola=(400,350)  
                            pos_expl=(450,250)                                       #posición de la explosión al disparar
                            disparo=True
                           
                    elif event.key==pygame.K_UP and disparo==False:                  #Tecla izquierda rotación en sentido positivo
                        speedv0=1
                   
                    elif event.key==pygame.K_DOWN and disparo==False:                #Tecla derecha rotación en sentido negativo
                        speedv0=-1
                       
                    elif event.key==pygame.K_LEFT and disparo==False:                #Tecla izquierda rotación en sentido positivo
                        speedangle=1
                    elif event.key==pygame.K_RIGHT and disparo==False:               #Tecla derecha rotación en sentido negativo
                        speedangle=-1
                    elif event.key==pygame.K_ESCAPE:                                 #Tecla escape sale del juego
                        running = False
                        self.outro('FIN DEL JUEGO','FIN DEL JUEGO')
                
                elif event.type == pygame.KEYUP:                                    #Eventos dejar de presionar tecla
                   
                    if event.key==pygame.K_UP and disparo==False:                    #Tecla izquierda rotación en sentido positivo
                        speedv0=0
                    elif event.key==pygame.K_DOWN and disparo==False:                #Tecla derecha rotación en sentido negativo
                        speedv0=0    
                    elif event.key==pygame.K_LEFT and disparo==False:                #Dejar de presionar tecla izquierda detiene la rotación
                        speedangle=0
                    elif event.key==pygame.K_RIGHT and disparo==False:               #Dejar de presionar tecla derecha detiene la rotación
                        speedangle=0
                
            
            #ROTACION DEL CAÑON
            angle=angle+speedangle                                                  #Incrementa el ángulo del cañon de acuerdo a las teclas presionadas
            v0=v0 + speedv0
            vi=(v0*10)/32
            image2_rotated , image2_rotated_rect = self.rotate(cañon,angle)              #Rota el cañon
                                                                                    #poscañon=poscañon[0]-step[0],poscañon[1]-step[1]-((g/2)*(t**2))         #(x,y)=(x0+v_x0,y0+v_y0)
            
            #DIBUJAR EN PANTALLA LAS DIFERENTES IMAGENES
            self.dibujar_img(((plano,posplano),(objetivo,posobjetivo),(explosion,pos_expl),(bola,pos_bola),(image2_rotated,pos_canon)))        
            
            #CALCULA NUEVAS POSICIONES
            t=t+n
            t1=t1+n
            posplano=self.nueva_pos(posplano,step,t,g) 
            posobjetivo=self.nueva_pos(posobjetivo,step,t,g)       
            pos_expl=self.nueva_pos(pos_expl,step,t,g)
            pos_canon=self.nueva_pos(pos_canon,step,t,g)
            
            
            #OBTENCION DE COLISION OBJETIVO-BOLA
            objetivorect=objetivo.get_rect(center=posobjetivo)
            bolarect=bola.get_rect(center=pos_bola)
            if bolarect.colliderect(objetivorect)==True:
                step=(0,0)
                t=0
                colision=True
                self.outro('TIRO ACERTADO','FELICITACIONES')
            
            #REBOTES DE LA BOLA CUANDO IMPACTA CONTRA LOS COSTADOS
            if posplano[0]<-3440 or posplano[0]>= 400 :
                step= -step[0],step[1]
    
            #REBOTES DE LA BOLA CUANDO IMPACTA CONTRA EL PISO
            horizonte_rect=plano.get_rect(center=(posplano[0]+1900,posplano[1]+2750))       #1900 Y 2750 CORRESPONDEN AL DESPLAZAMIENTO DEL RECTANGULO IMAGEN HACIA LA PARTE INFERIOR PARA QUE SIRVA DE REFERENCIA AL CHOQUE BOLA-PISO
            if bolarect.colliderect(horizonte_rect) and t>0.3:                              #t>0.3 evita rebotes debidos a una lectura anomala 
                if (step[1]>-0.001 and step[1]<0) or (step[0]<0.1):
                    step=(0,0)
                    self.outro('FIN DEL JUEGO','TIRO ERRADO')
                    
                else:
                    t=0
                    step=self.f_rebote(step,fact_perdida_choque)
                    
               
            #CUADROS DE TEXTO
            crear_cuadro_de_texto(screen,cuadro_angulo,'Ángulo:'+str(angle)+"°",letra_cuadro_angulo,(0,0,0),(255,255,255))   #Agrega un cuadro de texto con el angulo.
            crear_cuadro_de_texto(screen,cuadro_velocidad,'Velocidad incial:'+str(v0)+"m/s",letra_cuadro_velocidad,(0,0,0),(255,255,255))
            crear_cuadro_de_texto(screen,cuadro_posicion_objetivo,'coord.objivo(x,y): ('+str(distancia[0])+"m,"+str(distancia[1])+"m)",letra_cuadro_velocidad,(0,0,0),(255,255,255))
            crear_cuadro_de_texto(screen,cuadro_posicion_tiempo,str(int(t1))+'s',letra_cuadro_tiempo,(0,0,0),(255,255,255))
                  
            pygame.display.flip()                                                   #Hace visibles las imagenes cargadas
    
     


tierra=mundo()           
intro_game()        #Ahora desde la función intro_game se llama la función main y desde main se puede llamar el outro(por ahora con la tecla esc porque aun no se puede perder o ganar en el juego)                                                                    
