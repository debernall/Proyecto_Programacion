# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:14:16 2021

@author: ANDRES
"""

import pygame
import random
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
import codecs
import menu
import posiciones
import math

###############################      DECLARACIONES INICIALES        ##################################
# COLORES
yellow=(245, 245, 66)
green=(22,234,72)
blue=(2,50,207)
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)

pygame.init()

# TIPOS DE LETRAS
letra_botones = pygame.font.Font('Fonts/Starjedi.ttf', 30)
letra_titulos=pygame.font.Font('Fonts/Starjedi.ttf', 100)
letra_outro=pygame.font.Font('Fonts/Starjedi.ttf', 75)
letra_letreros=pygame.font.Font('Fonts/arial_narrow_7.ttf',18)
letra_instrucciones= pygame.font.Font('Fonts/arial_narrow_7.ttf',35)
letra_creditos=pygame.font.Font('Fonts/Starjedi.ttf',40)
# UBICACIONES DE ARCHIVOS
lista_instrucciones=('Inst/instruccion1.txt',
                     'Inst/instruccion2.txt',
                     'Inst/instruccion3.txt',
                     'Inst/instruccion4.txt',
                     'Inst/instruccion5.txt',
                     'Inst/instruccion7.txt')
lista_imagenes_inst=("img/cañon7.png",0,'img/teclas_inst.png','img/ecuaciones.png','img/imagen_mapa.png','img/rover.png')
lista_integrantes=('brian santiago vasquez sarin',
                   'jeisson andres abril masmelas',
                   'daniel eduardo bernal lozano',
                   'nelson andres rodriguez mora',
                   'sebastian augusto ojeda franco')
imagenes={'intro':"img/fondo_intro.jpg",
          'bola':"img/bolacañonpequeña.png",
          'bolita':"img/redsita1.png",
          'explosion':"img/explosion1.png",
          'explosionsita':"img/explosion1sita.png",
          'objetivo':"img/objetivo1.png",
          'objetivito':"img/objetivito.png",
          'cañon':"img/cañon8.png",
          'base':"img/cañon9.png",
          'cañonsito':"img/cañon8sito.png",
          'basesita':"img/cañon9sito.png",
          'cuadros':"img/cuadros.jpg"}

sonidos={'fondo':"sound/sonidofondo.wav",
         'explosion':"sound/sonexp.wav"}

# VARIABLES GLOBALES
puntos=0
nivel=0
next_level=False


###############################             FUNCIONES               ##################################
def instrucciones_juego(numero_instruccion):
    instruccion=lista_instrucciones[numero_instruccion]
    inst=True
    pygame.init()
    screen_instrucciones=pygame.display.set_mode((948,720))
    intro_background = pygame.image.load(imagenes['intro'])

    screen_instrucciones.blit(intro_background,(0,0))
    boton_volver_intro=pygame.Rect(screen_instrucciones.get_rect().centerx-150,610,300,100)
    boton_siguiente=pygame.Rect(948-260,610,250,100)
    boton_anterior=pygame.Rect(10,610,250,100)
    alto=200

    c_texto=codecs.open(instruccion,'r','utf-8').readlines()
    if numero_instruccion!=1:
        if numero_instruccion== 3 :
            ancho=400
        elif numero_instruccion==4:
            ancho=300
            alto=250

        else:
            ancho=200

        imagen_inst=pygame.transform.scale(pygame.image.load(lista_imagenes_inst[numero_instruccion]),[ancho,alto])
        menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx,450,ancho,200,' ',letra_botones,white,black,None)
        screen_instrucciones.blit(imagen_inst,[screen_instrucciones.get_rect().centerx-ancho/2,350])

    else:
        menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx,450,350,50,'Ángulo:25°',letra_letreros,None,green,green)


    for i in range(len(c_texto)):
        menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx,120+40*i,800,40,str(c_texto[i].rstrip()),letra_instrucciones,black,green,None)

    menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx,70,60,40,str(numero_instruccion+1)+'/'+str(len(lista_instrucciones)),letra_instrucciones,None,green,green)
                                                                                                                                    #Crea el cuadro que dice el numero de instruccion

    while (inst):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    quit()

            elif event.type==MOUSEBUTTONDOWN and event.button==1:
                if boton_volver_intro.collidepoint(pygame.mouse.get_pos()):
                    inst=False
                    intro_game()

                elif boton_anterior.collidepoint(pygame.mouse.get_pos()):
                    if numero_instruccion-1 in range(len(lista_instrucciones)):
                        inst=False
                        instrucciones_juego(numero_instruccion-1)
                    elif numero_instruccion-1 not in range(len(lista_instrucciones)):
                        inst=False
                        instrucciones_juego(numero_instruccion=5)

                elif boton_siguiente.collidepoint(pygame.mouse.get_pos()):
                    if numero_instruccion+1 in range(len(lista_instrucciones)):
                        inst=False
                        instrucciones_juego(numero_instruccion+1)
                    elif numero_instruccion+1 not in range(len(lista_instrucciones)):
                        inst=False
                        instrucciones_juego(numero_instruccion=0)

        menu.crear_boton(screen_instrucciones,boton_volver_intro,'volver a inicio',letra_botones ,green,yellow,blue,blue)
        menu.crear_boton(screen_instrucciones,boton_anterior,'Anterior',letra_botones ,green,yellow,blue,blue)
        menu.crear_boton(screen_instrucciones,boton_siguiente,'Siguiente',letra_botones ,green,yellow,blue,blue)
        menu.pygame.display.flip()


def intro_game():                                                                                                         #Pantalla de intro
    intro=True
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    pygame.display.set_caption('Parabolic Shot')

    intro_background = pygame.image.load(imagenes['intro'])
    screen.blit(intro_background,(0,0))
    menu.crear_cuadro_de_texto(screen,screen.get_rect().centerx,220,600,100,'ParaboliC',letra_titulos,None,blue,None)
    menu.crear_cuadro_de_texto(screen,screen.get_rect().centerx,320,400,100,'ShoT',letra_titulos,None,blue,None)
    sonidofondo=pygame.mixer.Sound(sonidos['fondo'])

    play=pygame.Rect(screen.get_rect().centerx-350/2,450,350,50)                                                                    #Figuras de los botones jugar y salir
    exit=pygame.Rect(screen.get_rect().centerx-350/2,650,350,50)
    instructions=pygame.Rect(screen.get_rect().centerx-350/2,550,350,50)
    sonidofondo.set_volume(0.2)
    sonidofondo.play(-1)
    while(intro):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :                                                                                          #Permite salir del juego desde la intro
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            elif event.type==MOUSEBUTTONDOWN and event.button==1:                                                                   #Si se hace click izquierdo:
                if play.collidepoint(pygame.mouse.get_pos()):                                                                       #Si el click se hizo sobre el botón jugar, continuar con el juego
                    intro=False
                    sonidofondo.stop()
                    return True

                elif instructions.collidepoint(pygame.mouse.get_pos()):
                    intro=False
                    sonidofondo.stop()
                    instrucciones_juego(0)

                elif exit.collidepoint(pygame.mouse.get_pos()):                                                                     #Si el click se hizo en salir...
                    pygame.quit()
                    quit()

        menu.crear_boton(screen,play,'Jugar',letra_botones ,green,yellow,blue,blue)                                                      #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima
        menu.crear_boton(screen,exit,'Salir',letra_botones ,green,yellow,blue,blue)
        menu.crear_boton(screen,instructions,'instrucciones',letra_botones ,green,yellow,blue,blue)
        pygame.display.flip()

def creditos():                                                                                                                   #Pantalla de intro
    credits=True
    pygame.init()
    screen_creditos= pygame.display.set_mode((948,720))
    pygame.display.set_caption('Créditos')

    intro_background = pygame.image.load(imagenes['intro'])
    screen_creditos.blit(intro_background,(0,0))
    menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,80,600,100,'Créditos',letra_titulos,None,blue,None)
    sonidofondo=pygame.mixer.Sound(sonidos['fondo'])

    for i in range(len(lista_integrantes)):
        menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,200+70*i,600,100,lista_integrantes[i],letra_creditos,None,green,None)
    exit_creditos=pygame.Rect(screen_creditos.get_rect().centerx-350/2,650,350,50)
    return_creditos=pygame.Rect(screen_creditos.get_rect().centerx-350/2,580,350,50)
    sonidofondo.set_volume(0.2)
    sonidofondo.play(-1)
    while(credits):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :                                                                                          #Permite salir del juego desde la intro
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            elif event.type==MOUSEBUTTONDOWN and event.button==1:                                                                   #Si se hace click izquierdo:
                if exit_creditos.collidepoint(pygame.mouse.get_pos()):                                                                       #Si el click se hizo sobre el botón jugar, continuar con el juego
                    pygame.quit()
                    quit()

                elif return_creditos.collidepoint(pygame.mouse.get_pos()):
                    sonidofondo.stop()
                    credits=False
                    intro_game()


        menu.crear_boton(screen_creditos,exit_creditos,'salir',letra_botones ,green,yellow,blue,blue)
        menu.crear_boton(screen_creditos,return_creditos,'volver a inicio',letra_botones ,green,yellow,blue,blue)                                         #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima

        pygame.display.flip()
def outro(titulo,estado):                                                                                                           # OUTRO MANTIENE AL JUGADOR EN UN NIVEL HASTA QUE PASE
    global nivel
    global next_level

    pygame.init()
    game_over=True
    screen= pygame.display.set_mode((948,720))
    pygame.display.set_caption(titulo)

    intro_background = pygame.image.load(imagenes['intro'])
    screen.blit(intro_background,(0,0))
    menu.crear_cuadro_de_texto(screen,screen.get_rect().centerx ,270,700,200,estado,letra_outro,None,blue,None)                                                                           #Genera la imagen con el texto
    menu.crear_cuadro_de_texto(screen,screen.get_rect().centerx ,150,700,200,str(puntos)+" puntos: "+"nivel "+str(nivel),letra_outro,None,blue,None)


    replay=pygame.Rect(screen.get_rect().centerx-350/2,440,350,50.)
    re_intro=pygame.Rect(screen.get_rect().centerx-350/2,510,350,50.)
    credits1=pygame.Rect(screen.get_rect().centerx-350/2,580,350,50)
    exit1=pygame.Rect(screen.get_rect().centerx-350/2,650,350,50)

    while(game_over):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :                                                                                          #Permite salir del juego desde la outro
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:                                                                                      #Tecla  esc sale del juego (NO ESTÁ FUNCIONANDO)
                    pygame.quit()
                    quit()

            elif event.type==MOUSEBUTTONDOWN and event.button==1:                                                                   #Si se hace click derecho:
                if replay.collidepoint(pygame.mouse.get_pos()):                                                                     #Si el click se hizo sobre el botón volver a  jugar, vuelve a la intro
                    game_over=False
                    return True

                elif exit1.collidepoint(pygame.mouse.get_pos()):                                                                    #Si el click se hiz en salir...
                    pygame.quit()
                    quit()

                elif re_intro.collidepoint(pygame.mouse.get_pos()):
                    game_over=False
                    intro_game()

                elif credits1.collidepoint(pygame.mouse.get_pos()):
                    game_over=False
                    creditos()


        menu.crear_boton(screen,replay,'volver a jugar',letra_botones ,green,yellow,blue,blue)                                           #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima
        menu.crear_boton(screen,exit1,'Salir',letra_botones ,green,yellow,blue,blue)
        menu.crear_boton(screen,credits1,'Créditos',letra_botones ,green,yellow,blue,blue)
        menu.crear_boton(screen,re_intro,"volver a inicio",letra_botones,green,yellow,blue,blue)
        pygame.display.flip()


###############################            CLASE MUNDO              ##################################
class mundo:

    def __init__(self,parametros):
        self.g=parametros[0]
        self.mplano=parametros[1]
        self.son_mundo=parametros[2]
        self.perdida=parametros[3]
        self.planet=parametros[4]
        self.vlimt=parametros[5]
        self.mmini=parametros[6]
        self.xp=parametros[7]
        self.yp=parametros[8]
        self.yi=parametros[9]
        self.yf=parametros[10]
        self.mountain=parametros[11]
        self.little_mountain=parametros[12]
        self.rover=parametros[13]
        self.rovertierra=parametros[14]
        self.phoenix=parametros[15]
        self.roversito=parametros[16]
        self.rovertierrita=parametros[17]
        self.fenixito=parametros[18]
        self.yp2=parametros[19]
        self.lim_angle=parametros[20]

        self.escala=10/1 #10pixeles/1metros
        self.lista=[]
        self.lista1=[]

    
    def rotate(self,surface, angle,g):
        rotated_surface=pygame.transform.rotozoom(surface,angle,1)
        rotated_rect = rotated_surface.get_rect(center=g)
        return rotated_surface,rotated_rect
    
    def nueva_pos(self,pos_inicial,v,t,escala,sentido,correccion,vobstaculo):
        #if nivel=!5:
        if pos_inicial[0]==600.0:
            if v[1]!=0:
                self.lista.append(pos_inicial[1])
                self.lista1.append(t)
        pos_final=pos_inicial[0]-v[0]*(0.03317*escala)+vobstaculo[0],pos_inicial[1]-(v[1]*(0.03317*escala))-((sentido)*(0.5*self.g*t*correccion))-vobstaculo[1]
        #else:
            
        return pos_final

    def pos_obstaculo(self,pos_inicial,radio,cx,cy):#,escala,correccion):
        #if nivel==5:
        #num_segmentos = 20
        #rad = 300
        #if k==0:
         #   posobjetivo=[0,0]
          #  pos_final=pos_inicial
           # return pos_final
        #posobjetivoo= random.randrange(200,xf-100), random.randrange(self.yi,self.yf-100)
        #cx = posobjetivo[0]
        #cy = posobjetivo[1]
        angulo = math.atan((pos_inicial[1]-cy)/(pos_inicial[0]-cx))     # np.linspace(0, 2*np.pi, num_segmentos+1)           
        xx = radio * np.cos(angulo+0.1) + cx
        yy = radio * np.sin(angulo+0.1) + cy      
        pos_final=xx,yy 
       # if k==0:
        #    pos_final=pos_inicial
        return pos_final

    def dibujar_img(self,list_img):
        screen= pygame.display.set_mode((800,700))
        for i in list_img:
            screen.blit(i[0],i[1])
        return

    def f_rebote(self,step,r):
        step_nuevo=(step[0]/(r),step[1]/(r))
        return step_nuevo


    def main(self):                      ################puntos
        global puntos
        global nivel
        global next_level

        #PROPIEDADES INICIALES PYGAME
        pygame.init()
        screen= pygame.display.set_mode((800,700))
        clock=pygame.time.Clock()
        pygame.display.set_caption(self.planet)

        #CARGA DE IMAGENES
        plano = pygame.image.load(self.mplano)                                                                                      #Imagen de fondo
        mini = pygame.image.load(self.mmini)
        bola=pygame.image.load(imagenes['bola'])
        bolita=pygame.image.load(imagenes['bolita'])
        cañonsito=pygame.image.load(imagenes['cañonsito'])                                                                        #Imagen de bala
        basesita=pygame.image.load(imagenes['basesita'])
        cañon=pygame.image.load(imagenes['cañon'])                                                                                  #Imagen de cañon
        base=pygame.image.load(imagenes['base'])
        explosion=pygame.image.load(imagenes['explosion'])                                                                          #Imagen de la Explosón al disparar
        explosionsita=pygame.image.load(imagenes['explosionsita'])
        objetivo=pygame.image.load(imagenes['objetivo'])
        objetivito=pygame.image.load(imagenes['objetivito'])
        cuadros=pygame.image.load(imagenes['cuadros'])
        sonidoexplosión=pygame.mixer.Sound(sonidos['explosion'])

        #CARGA DE SONIDO DE FONDO
        sonidofondo=pygame.mixer.Sound(self.son_mundo)

        #DIBUJAR MONTAÑA
        if self.mountain!=1:
            mountain=pygame.image.load(self.mountain)
            little_mountain=pygame.image.load(self.little_mountain)
        elif self.mountain==1:
              mountain=1

        #DIBUJAR OBSTACULOS
        if self.rover!=1:
            rover=pygame.image.load(self.rover)
            rovertierra=pygame.image.load(self.rovertierra)
            phoenix=pygame.image.load(self.phoenix)
            roversito=pygame.image.load(self.roversito)
            rovertierrita=pygame.image.load(self.rovertierrita)
            fenixito=pygame.image.load(self.fenixito)
        elif self.rover==1:
              rover=1
              rovertierra=1
              phoenix=1

  #      if self.rover!=1:
   #        rover=pygame.image.load(self.rover)
    #       roversito=pygame.image.load(self.roversito)
     #   if self.rovertierra!=1:
      ##    rovertierrita=pygame.image.load(self.rovertierrita)
      #  if self.phoenix!=1:
       #     phoenix=pygame.image.load(self.phoenix)
        #    fenixito=pygame.image.load(self.fenixito)

        #POSICION DE IMAGENES Y VARIABLES A UTILIZAR
        x0,y0=400,350
        xf=3600                                                                                     #Limites de la imagen de fondo
        if nivel==1:
            posobjetivo= random.randrange(200,xf-100), 0
        elif nivel!=1:
              posobjetivo= random.randrange(200,xf-100), random.randrange(self.yi,self.yf-100)            #Posición aleatoria del objetivo
              
        xo=x0+posobjetivo[0]
        yo=y0-posobjetivo[1]
        if yo>(-(((1/2)*self.g*(xo)**2)/(self.vlimt)**2)+(((1/2)*(self.vlimt)**2)/(self.g))) and nivel!=1:          #Parece ser un ajuste a la parabola de seguridad
            yo=yo+400
        #xo=x0+200
        #yo=y0-200
        posobjetivo=(xo,yo)

        posplano=self.xp,self.yp
        pos_canona=(x0,y0)
        pos_canon=(x0-64,y0-64)

        pos_canonsito=(20,400+(self.yf*0.05))
        pos_bolita=(20,400+(self.yf*0.05))


        running=True                                                                                    #Variable que mantiene activo el juego
        posimg=x0,y0
        distancia=((posobjetivo[0]-posimg[0])/self.escala),-((posobjetivo[1]-posimg[1])/self.escala)
        posobjetivito=(20+(distancia[0]*0.5),400+(self.yf*0.05)-(distancia[1]*0.5))                     #Distancia al objetivo
        pos_bola= -x0,-y0
        pos_bolita=-x0,-y0                                                                              #Declaración de posición inicial de la bala
        pos_expl= -x0,-y0                                                                               #Posición de la explosión antes de disparar
        pos_expli= -x0,-y0
        step= 0,0                                                                                       #vector velocidad
        angle=0                                                                                         #Declaración de variable ángulo del cañon
        speedangle=0                                                                                    #Variable que almacena la rotación del cañon
        n=0
        v0=1                                                                                            #Velocidad inicial
        vi=1
        vr=10
        vrt=10
        vrpy=10
        vrpx=10
        speedv0=0
        t=0
        t1=0                                                                                           #Variable de tiempo
        pos_rover=[xo-300,yo-300]#[1500,-2000]
        pos_rovertierra=400,250
        pos_phoenix=1000,-1000
        distanciarover=pos_rover[0]-x0, pos_rover[1]-y0
        distanciarovertierra=pos_rovertierra[0]-x0
        distanciaphoenix=pos_phoenix[0]-x0,pos_phoenix[1]-y0

        #def pos_obstaculo(self,pos_inicial,radio):#,escala,correccion):
        #if nivel==5:
         #   num_segmentos = 20
        #rad = 300
         #   posobjetivo= random.randrange(200,xf-100), random.randrange(self.yi,self.yf-100)
 #       cx = posobjetivo[0]
  #      cy = posobjetivo[1]
   #     angulo = math.atan((pos_rover[1]-cy)/(pos_rover[0]-cx))     # np.linspace(0, 2*np.pi, num_segmentos+1)           
    #    xx = 300 * np.cos(angulo+0.5) + cx
     #   yy = 300 * np.sin(angulo+0.5) + cy      
        #pos_final=xx,yy 
            #return pos_final




        colision=False
        disparo=False
        gameover=False
        image_alpha=254

        sonidofondo.set_volume(0.8)
        sonidofondo.play(-1)

        while(running):


            ns=clock.tick(30)                                                                          #Periodo de recarga de imagen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                                                          #Permite salir del juego
                    pygame.quit()
                    quit()

                #INTERACCIONES POR MEDIO DE TECLADO EN EL JUEGO
                elif event.type == pygame.KEYDOWN:                                                     #Evento presionar tecla
                    if event.key==pygame.K_SPACE:                                                      #Tecla espacio
                        if colision==True: #and choque==False:                                        #NO TIENE EFECTO
                            step=(0,0)

                        if disparo==False:
                            v_x0=vi*np.cos(np.radians(angle))                                         #Velocidad inicial en x
                            v_y0=-vi*np.sin(np.radians(angle))                                                                      #Velocidad inicial en y(Es negativa porque el pixel (0,0) se encuentra en la esquina sup izq)
                            step=v_x0,v_y0                                                                                          #Tras presionar la tecla espacio
                            n=1
                            pos_bola=(x0,y0)
                            pos_bolita=(20,400+(self.yf*0.05))
                            pos_expl=(x0+50,y0-100)                                                                                      #posición de la explosión al disparar
                            pos_expli=(20,400+(self.yf*0.05))
                            disparo=True
                            sonidofondo.set_volume(0.5)
                            sonidoexplosión.play()
                            speedv0=0
                            speedangle=0
                            ESCALA=self.escala

                            X0=int(x0/ESCALA)
                            Y0=4000+self.yp-y0
                            Y0=int(Y0/ESCALA)
                            #print(Y0)
                            YOBJ=4000+self.yp-yo
                            YOBJ=int(YOBJ/ESCALA)
                            THETA0=np.radians(angle)
                            V0=v0
                            G=self.g
                            E=self.perdida                                                              #Debe ser un numero entre 0 y 1
                            XLIM=4000
                            XLIM=int(XLIM/ESCALA)
                            YLIM=int(4000/ESCALA)
                            YLIMINF=4000+self.yp2-y0-20
                            YLIMINF=int(YLIMINF/ESCALA)
                            EPSILON=0.01                                                              #ESPACIAMIENTO DEL VECTOR TIEMPO
                            IMPACTOS=[]
                            IMPACTOS.append((X0+(xo-x0)/10,YOBJ,5,True))
                            MAX_REBOTES=10
                            #print(X0,Y0,THETA0,V0,G,E,XLIM,YLIM,YLIMINF,EPSILON,IMPACTOS,MAX_REBOTES)

                            aa=posiciones.posiciones(X0,Y0,THETA0,V0,G,E,XLIM,YLIM,YLIMINF,EPSILON,IMPACTOS,MAX_REBOTES)
                            #posiciones.graficar(aa[3],aa[0],aa[1])
                            #print(aa[2])
                            #for u in aa[2]:
                                #print(u)
                            #print('adsdasd',aa[2])
                            #AQUÍ SE EJECUTA LA FUNCION CALCULAR VECTORES X,Y

                    elif event.key==pygame.K_UP and disparo==False:                                     #Tecla izquierda rotación en sentido positivo
                        speedv0=1

                    elif event.key==pygame.K_DOWN and disparo==False:                                   #Tecla derecha rotación en sentido negativo
                        speedv0=-1

                    elif (event.key==pygame.K_LEFT and disparo==False):                                 #Tecla izquierda rotación en sentido positivo
                        speedangle=1

                    elif event.key==pygame.K_RIGHT and disparo==False:                                  #Tecla derecha rotación en sentido negativo
                        speedangle=-1

                    elif event.key==pygame.K_a and colision==True:                                      #Tecla a permite avanzar de nivel y sumar puntos tras choque
                        puntos+=1
                        nivel+=1
                        return True

                    elif event.key==pygame.K_a and gameover==True:                                      #Tecla a permite avanzar de nivel y no sumar puntos sin choque
                        nivel+=1
                        puntos+=0
                        return True

                    elif event.key==pygame.K_s and gameover==True:                                      #Tecla s permite avanzar de nivel y no sumar puntos
                        nivel+=0
                        puntos+=0
                        return True

                    elif event.key==pygame.K_ESCAPE:                                                    #Tecla escape sale del juego
                        running = False
                        sonidofondo.stop()
                        return False

                elif event.type == pygame.KEYUP:                                                        #Eventos dejar de presionar tecla
                    if event.key==pygame.K_UP and disparo==False:                                       #Tecla izquierda rotación en sentido positivo
                        speedv0=0

                    elif event.key==pygame.K_DOWN and disparo==False:                                   #Tecla derecha rotación en sentido negativo
                        speedv0=0

                    elif event.key==pygame.K_LEFT and disparo==False:                                   #Dejar de presionar tecla izquierda detiene la rotación
                        speedangle=0

                    elif event.key==pygame.K_RIGHT and disparo==False:                                  #Dejar de presionar tecla derecha detiene la rotación
                        speedangle=0

                    elif event.key==pygame.K_UP and disparo==True:                                      #Tecla derecha rotación en sentido negativo
                        ns=clock.tick(60)

            if disparo==True and gameover==False:
                k2=t1*0.03317
                k1=aa[2].flat[np.abs(aa[2]-k2).argmin()]
                k=np.where(aa[2]==k1)[0][0]
                #print(k2,k1,k)


            #ROTACION DEL CAÑON
            angle=angle+speedangle                                                                      #Incrementa el ángulo del cañon de acuerdo a las teclas presionadas
            #LIMITES DE ROTACION DEL CAÑON
            if angle>=90:
                angle=90

            elif angle<=self.lim_angle:
                angle=self.lim_angle

            v0=v0 + speedv0
            vi=vi + speedv0
            if v0>=self.vlimt:
                v0=self.vlimt
            if vi>=self.vlimt:
                vi=self.vlimt
            if v0<=1:
                v0=1


            image2_rotated , image2_rotated_rect = self.rotate(cañon,angle,pos_canona)
            image3_rotated , image3_rotated_rect = self.rotate(cañonsito,angle,pos_canonsito)

            explosion_rotated , explosion_rotated_rect = self.rotate(explosion,angle,pos_canona)                                                         #Rota el cañon
            explosionsita_rotated , explosionsita_rotated_rect = self.rotate(explosionsita,angle,pos_canonsito)

            cc = (pos_canon[0]+63-int(image2_rotated.get_width()//2),pos_canon[1]+63-int(image2_rotated.get_height()//2))
            cc1 = (pos_canonsito[0]-int(image3_rotated.get_width()//2),pos_canonsito[1]-int(image3_rotated.get_height()//2))

            cd = (pos_expl[0]-50-int(explosion_rotated.get_width()//2),pos_expl[1]+100-int(explosion_rotated.get_height()//2))
            cd1 = (pos_expli[0]-int(explosionsita_rotated.get_width()//2),pos_expli[1]-int(explosionsita_rotated.get_height()//2))

            pos_base=(pos_canon[0]-35,pos_canon[1]-35)
            pos_basesita=(pos_canonsito[0]-15,pos_canonsito[1]-15)

            if image_alpha>0 and disparo==True:
                image_alpha-=5

            explosion_rotated.set_alpha(image_alpha)
            explosionsita_rotated.set_alpha(image_alpha)
            pos_bola1=(pos_bola[0]-8,pos_bola[1]-8)
            posobjetivo1=(posobjetivo[0]-50,posobjetivo[1]-50)
            pos_roversito=distanciarover

            #DIBUJAR EN PANTALLA LAS DIFERENTES IMAGENES
            if mountain==1 and rover==1:
             self.dibujar_img(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito)))
            elif mountain!=1:
             self.dibujar_img(((plano,posplano),(cuadros,(0,0)),(mountain,(pos_base[0]-500,pos_base[1]-250)),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(little_mountain,(pos_basesita[0]-10,pos_basesita[1]+3))))
            elif rover!=1:
             self.dibujar_img(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(fenixito,distanciaphoenix),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(roversito,pos_roversito),(rover,pos_rover),(rovertierra,pos_rovertierra),(phoenix,pos_phoenix),(rovertierrita,(distanciarovertierra,550))))
             #self.dibujar_img(((roversito,(distanciarover,450)),(fenixito,distanciaphoenix)))

            #OBTENCION DE COLISION OBJETIVO-BOLA
            objetivorect=objetivo.get_rect(center=posobjetivo)
            bolarect=bola.get_rect(center=pos_bola)
            a=objetivorect.center
            b=bolarect.center
            r=((((a[0]-b[0])**2)+((a[1]-b[1])**2))**(0.5))

           # COLISION CON ROVER, PHOENIX Y ROVERTIERRA
            c=pos_rover[0]+100,pos_rover[1]+65
            d=pos_rovertierra[0]+100,pos_rovertierra[1]+88
            e=pos_phoenix[0]+100,pos_phoenix[1]+35
            if self.rover!=1 and ((((c[0]-b[0])**2)+((c[1]-b[1])**2))**(0.5))<50:
                self.dibujar_img(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(explosion,(pos_rover[0]-220,pos_rover[1]-100)),(bola,pos_bola1),(explosion_rotated,pos_rover),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(fenixito,distanciaphoenix),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(roversito,distanciarover),(rovertierra,pos_rovertierra),(phoenix,pos_phoenix)))#,(rovertierrita,(distanciarovertierra,550))))
                step=(0,0)
                vr=0
                vrt=0
                vrpx=0
                vrpy=0
                sonidofondo.stop()
                #self.dibujar_img(explosion,pos_rover)
                
                gameover=True
                #t=0
                #CHOQUE CON ROVERTIERRA
            if self.rover!=1 and ((((d[0]-b[0])**2)+((d[1]-b[1])**2))**(0.5))<100:
                self.dibujar_img(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(explosion,(pos_bola1[0]-220,pos_bola1[1]-120)),(bola,pos_bola1),(explosion_rotated,pos_rover),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(fenixito,distanciaphoenix),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(roversito,distanciarover),(phoenix,pos_phoenix),(rovertierrita,(distanciarovertierra,550))))
                step=(0,0)
                
                vr=0
                vrt=0
                vrpx=0
                vrpy=0
                sonidofondo.stop()
                gameover=True
                #t=0
                sonidofondo.stop()
            if self.rover!=1 and ((((e[0]-b[0])**2)+((e[1]-b[1])**2))**(0.5))<200:
                self.dibujar_img(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(explosion,(pos_bola1[0]-220,pos_bola1[1]-120)),(bola,pos_bola1),(explosion_rotated,pos_rover),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(fenixito,distanciaphoenix),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(roversito,distanciarover),(rovertierra,pos_rovertierra),(rovertierrita,(distanciarovertierra,550))))
                sonidofondo.stop()
                step=(0,0)
                vr=0
                vrt=0
                vrpx=0
                vrpy=0
                sonidofondo.stop()
                gameover=True
                #step=(0,0)
                #menu.crear_cuadro_de_texto(screen,425,375,450,37,'¡Fallaste, presiona A para continuar!',letra_letreros,black,blue,blue)
                #t=0
            t=t+n
            t1+=n
            #if t1>9:
            #    ns=clock.tick(60)
            # CONDICION DE IMPACTO
            if r<50:
                step=(0,0)
                t=0
                colision=True
                sonidofondo.stop()
            # ESTADOS DEL JUEGO
            if colision==True:
                menu.crear_cuadro_de_texto(screen,425,375,450,35,'¡Buen tiro, presiona A para avanzar!',letra_letreros,black,blue,blue)

            if gameover==True and colision==False:
                menu.crear_cuadro_de_texto(screen,425,375,450,37,'¡Fallaste, presiona A para continuar!',letra_letreros,black,blue,blue)
                t=0
                #step=(0,0)

            # REBOTES DE LA BOLA
            # if posplano[0]<-(xf-20) or posplano[0]>= x0 :
            #     step=(0,0)
            #     sonidofondo.stop()
            #     gameover=True                                                                                                      #   AQUI HAY UNA SALIDA SI SE IMPACTA CON LAS PAREDES

            #********************************** USO DE LA FUNCION POSICIONES *******************************


            ##################  COLOCAR LAS CONDICIONES INICIALES DEL LANZAMIENTO EN S.I.
            # x0=0                            #POSICION INICIAL DE LA BALA EN X
            # y0=0                            #POSICION INICIAL DE LA BALA EN Y
            # theta0=1.6*math.pi/4            #ANGULO DE LANZAMIENTO
            # v0=16                           #MAGNITUD DE VELOCIDAD INICIAL
            # g=9.8                           #GRAVEDAD
            # e=0.8                           #FACTOR DE PERDIDA DE VELOCIDAD
            # xlim=100                        #LONGITUD MAXIMA DEL TABLERO EN X
            # ylim=10000                      #LONGITUD MAXIMA DEL TABLERO EN Y
            # epsilon=0.0001                  #ESPACIAMIENTO DEL VECTOR TIEMPO
            # impactos=((20,3,1.1,False),(35,8,2,True),(10,8,2,False))    #VECTOR DE OBSTACULOS Y OBJETIVO: (X_CENTRO,Y_CENTRO,RADIO,TRUE:OBJETIVO/FALSE:OBSTACULO)
            # max_rebotes=10                  #PERMITE ESTABLECER UN MAXIMO DE REBOTES

            ################   FUNCION QUE DA COMO RESULTA UN 4 VECTORES: X(t), Y(t), t y de nuevo devuelve impactos
            #(x,y,t,impactos)=posiciones.posiciones(x0,y0,theta0,v0,g,e,xlim,ylim,epsilon,impactos,max_rebotes)
            #posiciones.graficar(a[3],a[0],a[1])

            ################    LOS VECTORES ENCONTRADOS DEFINEN LA TRAYECTORIA DE LA BALA
            ################    para obtener el efecto de desplazamiento se deben aplicar transformaciones
            ################    1. Las reflexiones en x,y se obtienen con x'=-x, y'=-y
            ################    2. Las traslaciones permiten ubicar cada elemento en un posicion primada
            ################    3. Aplicar un escalado de los puntos que esta relacionado por la proporcion metros/pixel

            ################    UN CONJUNTO DE VECTORES DETERMINAN EL DESPLAZAMIENTO TOTAL DEL SISTEMA
            ################    no es necesario calcular repetidamente dicho vector, se debe calcular una sola vez
            ################    teniendo en cuenta que x,y son funciones de t. Las coordenadas en un tiempo dado
            ################    deben calcularse asi:
            ################    1. Establecer un t1(s) en el bucle principal del juego
            ################    2. Buscar con k=np.where(t>t1)[0] la posicion del elemento del vector que cumple la condicion
            ################    3. La posicion obtenida (x,y) para un t1 dado será: (x[k],y[k])
            ################    4. Aplicar las transformaciones necesarias
            ################    Conviene definir un origen en la parte inferior derecha (traslacion1)
            ################    Luego calcular las posiciones de los objetos respecto a dicho nuevo origen (traslacion2)
            ################    Aplicar una reflexión sobre el sistema de puntos para obtener el efecto de desplazamiento
            ################    Aplicar el escalado de los puntos
            ################    El minimapa puede ser obtenido de manera similar pero con un segundo escalado

            
            # CALCULO DE NUEVAS POSICIONES
            if disparo==True:
                #print(posplano,-10*(aa[0][k]-40),self.yp+10*(aa[1][k]-65))
                #print(posobjetivo,self.yp+10*(aa[1][k]+35)+yo,k)

                posplano=x0-10*(aa[0][k]),self.yp+10*(aa[1][k]-65)-3000-self.yp
                #print(posplano,x0-10*(aa[0][k]),self.yp+10*(aa[1][k]-65)-3000-self.yp,-3000-self.yp)
                posobjetivo=(-10*(aa[0][k]-40)+xo,10*(aa[1][k]+35)+yo-4000-self.yp)
                #print(posobjetivo,10*(aa[1][k]+35)+yo-4000-self.yp,YOBJ,yo-4000-self.yp)
                pos_expl=850-10*(aa[0][k]),10*(aa[1][k]-65)+y0-100-(3000+self.yp)
                #print(pos_expl[1],10*(aa[1][k]-65)+y0-100-(3000+self.yp),3000+self.yp,y0-100)
                pos_canon=336-10*(aa[0][k]-40),250+10*(aa[1][k]-65+3.6)-3000-self.yp
                #print(pos_canon,336-10*(aa[0][k]-40),250+10*(aa[1][k]-65+3.6)-3000-self.yp)
                #print(len(aa[0]),k)
                #print(pos_bolita,(0.5*(aa[0][k])),-self.yp-0.5*(aa[1][k])-1400)
                pos_bolita=0.5*(aa[0][k]),-self.yp-0.5*(aa[1][k])-1400+2000+self.yp
                #print(pos_bolita,0.5*(aa[0][k]),-self.yp-0.5*(aa[1][k])-1400+2000+self.yp,2000+self.yp)

             #   print(pos_canon,10*(aa[1][k]+35+13.6)+yo-4000-self.yp)


                if (k+4)>len(aa[0]):
                    sonidofondo.stop()
                    gameover=True

            #print(posplano)
            #posplano=self.nueva_pos(posplano,step,t,10,1,0.022,(0,0))
            #posobjetivo=self.nueva_pos(posobjetivo,step,t,10,1,0.022,(0,0))
            #pos_expl=self.nueva_pos(pos_expl,step,t,10,1,0.022,(0,0))
            #pos_canon=self.nueva_pos(pos_canon,step,t,10,1,0.022,(0,0))

            #pos_bolita=self.nueva_pos(pos_bolita,(-step[0],-step[1]),t,0.5,-1,0.0011,(0,0))
            if rover!=1:
             pos_rover=self.nueva_pos(pos_rover,step,t,10,1,0.022,(vr,0))
             pos_rovertierra=self.nueva_pos(pos_rovertierra,step,t,10,1,0.022,(vrt,0))
             pos_phoenix=self.nueva_pos(pos_phoenix,step,t,10,1,0.022,(vrpx,vrpy))
             


            if rover!=1 and nivel==5:
                pos_rover=self.pos_obstaculo(pos_rover,300,posobjetivo[0],posobjetivo[1])
                #pos_rover=self.nueva_pos(pos_rover,step,t,10,1,0.022,(vr,0))
                pos_rovertierra=self.nueva_pos(pos_rovertierra,step,t,10,1,0.022,(vrt,0))
                pos_phoenix=self.nueva_pos(pos_phoenix,step,t,10,1,0.022,(2*vrpx,2*vrpy))

            if rover!=1 and nivel>4:
             pos_rover=self.nueva_pos(pos_rover,step,t,10,1,0.022,(2*vr,0))
             pos_rovertierra=self.nueva_pos(pos_rovertierra,step,t,10,1,0.022,(2*vrt,0))
             pos_phoenix=self.nueva_pos(pos_phoenix,step,t,10,1,0.022,(2*vrpx,2*vrpy))

            # REBOTES DE LA BOLA CUANDO IMPACTA CONTRA EL PISO
            # horizonte_rect=plano.get_rect(center=(posplano[0]+2000,posplano[1]+5370))                                               #1900 Y 2750 CORRESPONDEN AL DESPLAZAMIENTO DEL RECTANGULO IMAGEN HACIA LA PARTE INFERIOR PARA QUE SIRVA DE REFERENCIA AL CHOQUE BOLA-PISO
            distanciarover=(pos_rover[0]-pos_base[0])*0.05 , 560+ (pos_rover[1]-pos_base[1])*0.05
            distanciarovertierra=(pos_rovertierra[0]-pos_base[0])*0.05
            distanciaphoenix=(pos_phoenix[0]-pos_base[0])*0.05,560+(pos_phoenix[1]-pos_base[1])*0.05
            # if bolarect.colliderect(horizonte_rect) and t>0.3:                                                                      #t>0.3 evita rebotes debidos a una lectura anomala
            #     if (step[1]>-0.001 and step[1]<0) or (step[0]<0.1):
            #         step=(0,0)
            #         sonidofondo.stop()
            #         gameover = True                                                                                                #   AQUI HAY UNA SALIDA SI REBOTA

            #     else:
            #         t=0
            #         step=self.f_rebote(step,self.perdida)

            # LIMITE SUPERIOR
            # if posplano[1]>(y0-50):
            #     step=(0,0)
            #     sonidofondo.stop()                                                                                                  #   AQUI HAY UNA SALIDA SI SE IMPACTA EL TECHO
            #     gameover=True
            #print(distanciaphoenix)

            if pos_rover[0]>=posplano[0]+4000:
                vr=-vr
            if pos_rover[0]<=posplano[0]:
                vr=-vr
            if pos_rovertierra[0]>=posplano[0]+4000:
                vrt=-vrt
            if pos_rovertierra[0]<=posplano[0]:
                vrt=-vrt
            if pos_phoenix[0]>=posplano[0]+4000:
                vrpx=-vrpx
            if pos_phoenix[0]<=posplano[0]:
                vrpx=-vrpx
            if pos_phoenix[1]>=posplano[1]+4000:
                vrpy=-vrpy
            if pos_phoenix[1]<=posplano[1]:
                vrpy=-vrpy
            #CUADROS DE TEXTO
            print(explosion,angle,pos_canon)
            #print(cd,pos_expl,(int(explosion_rotated.get_width()//2),int(explosion_rotated.get_height()//2)))
            menu.crear_cuadro_de_texto(screen,87,45,175,50,'Ángulo',letra_letreros,None,white,None)                       #Agrega un cuadro de texto con el angulo.
            menu.crear_cuadro_de_texto(screen,87,70,175,50,str(angle)+'º',letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,270,45,250,50,'Velocidad inicial',letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,270,70,250,50,str(v0)+"m/s",letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,470,45,250,50,'Objetivo(x,y)',letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,470,70,250,50,'('+str(distancia[0])+"m,"+str(distancia[1])+"m)",letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,680,45,150,50,'Gravedad',letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,680,70,150,50,str(self.g)+'m/s^2',letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,87,130,175,50,'Nivel',letra_creditos,None,blue,None)
            menu.crear_cuadro_de_texto(screen,87,180,175,50,str(nivel),letra_creditos,None,blue,None)     
            menu.crear_cuadro_de_texto(screen,700,130,175,50,'Puntos',letra_creditos,None,blue,None)      
            menu.crear_cuadro_de_texto(screen,700,180,175,50,str(puntos),letra_creditos,None,blue,None)      
            menu.crear_cuadro_de_texto(screen,100,370,150,50,'mapa',letra_creditos,None,blue,None)
            menu.crear_cuadro_de_texto(screen,101,500,200,200,"",letra_botones,None,green,blue)
            menu.crear_cuadro_de_texto(screen,screen.get_rect().centerx ,650,700,200,self.planet.lower(),letra_outro,None,blue,None)
            pygame.display.flip()                                                                                                   #Hace visibles las imagenes cargadas

###############################   VARIABLES Y CREACION DE MUNDOS    ##################################
p_space={'g':0.0001,

          'im_fondo': "img/nebula.png",
          'son_mundo':"sound/sonidofondo0.wav",
          'factor_perdida':1,
          'nombre_planeta':'ESPACIO',
          'vlimt':100,
          'im_min':"img/mmnebula.png",
          'px':0,
          'py':-2000,
          'yi':500,
          'yf':2350,
          'mountain':1,'little_mountain':1,'im_objetivo':1,
          'im_objetivo':1,'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':-23}                          #ESTA POSICION 2 SIRVE PARA SEÑALAR LA ALTURA DEL SUELO CUANDO EL CAÑON ESTA EN LA MONTAÑA

p_tierra={'g':9.8,

          'im_fondo': "img/pradera (2).jpg",
          'son_mundo':"sound/sonidofondo1.wav",
          'factor_perdida':0.9,
          'nombre_planeta':'TIERRA',
          'vlimt':81,
          'im_min':"img/mpradera.jpg",
          'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,'little_mountain':1,'im_objetivo':1,'im_objetivo':1,'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':0}
p_luna={'g':1.6,
          'im_fondo': "img/luna1.jpg",
          'son_mundo':"sound/sonidofondo2.wav",
          'factor_perdida':0.9,
          'nombre_planeta':'LUNA',
          'vlimt':32,
          'im_min':"img/mluna.jpg",'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,'mountain':1,'little_mountain':1,'im_objetivo':1,'im_objetivo':1,'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':0}
p_marte={'g':3.721,
          'im_fondo': "img/marte.jpg",
          'son_mundo':"sound/sonidofondo3.wav",
          'factor_perdida':0.9,
          'nombre_planeta':'MARTE',
          'vlimt':51,
          'im_min':"img/mmarte.jpg",
          'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,'mountain':1,
          'little_mountain':1,
          'im_objetivo':"img/rover.png",'im_objetivo1':"img/rovertierra.png",
          'im_objetivo2':"img/phoenix.png",
          'im_roversito':"img/roversito.png",
          'im_rovertierrita':"img/rovertierrita.png",
          'im_fenixito':"img/fenixito.png",
          'py2':-3000,
          'lim_angle':0}
p_triton={'g':0.78,
          'im_fondo': "img/triton.jpg",
          'son_mundo':"sound/sonidofondo4.wav",
          'factor_perdida':0.9,
          'nombre_planeta':'TRITON',
          'vlimt':22,
          'im_min':"img/tritonsito.jpg",
          'px':0,
          'py':-1000,
          'yi':-1850,
          'yf':1350,'mountain':"img/montaña.png",
          'little_mountain':"img/montañita.png",
          'im_objetivo':1,'im_objetivo':1,'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-2000,
          'lim_angle':-89}


p_ganimedes={'g':1.46,
          'im_fondo': "img/ganim.png",
          'son_mundo':"sound/sonidofondo4.wav",
          'factor_perdida':0.6,
          'nombre_planeta':'Ganimedes',
          'vlimt':35,
          'im_min':"img/ganimini.png",'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,'mountain':1,'little_mountain':1,
#          'px':0,
 #         'py':-2000,
  #        'yi':200,
   #       'yf':2350,'mountain':1,
    #      'little_mountain':1,
          'im_objetivo':"img/rover.png",'im_objetivo1':"img/rovertierra.png",
          'im_objetivo2':"img/phoenix.png",
          'im_roversito':"img/roversito.png",
          'im_rovertierrita':"img/rovertierrita.png",
          'im_fenixito':"img/fenixito.png",
          'py2':-3000,
          'lim_angle':0}



luna=mundo(list(p_luna.values()))
space=mundo(list(p_space.values()))
tierra=mundo(list(p_tierra.values()))
marte=mundo(list(p_marte.values()))
triton=mundo(list(p_triton.values()))

ganimedes=mundo(list(p_ganimedes.values()))


###############################         EJECUCION DEL JUEGO         ##################################
jugar=True
jugar_outro=True
intro_game()

while jugar:

        nivel=0
        puntos=0
        while jugar_outro:
            if nivel==0:
                jugar_outro=mundo.main(marte)
            elif nivel==1:
                jugar_outro=mundo.main(luna)
            elif nivel==2:
                jugar_outro=mundo.main(marte)
            elif nivel==3:
                jugar_outro=mundo.main(triton)
            elif nivel==4:
                jugar_outro=mundo.main(tierra)
            elif nivel==5:
                jugar_outro=mundo.main(ganimedes)
         
            else:
                jugar_outro=False

        jugar_outro=outro('Menú','intentalo de nuevo')