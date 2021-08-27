# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:14:16 2021

@author: GRUPO 3
"""

import pygame
import random
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
import codecs
import menu
import mov
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
letra_creditos1=pygame.font.Font('Fonts/Starjedi.ttf',18)
# UBICACIONES DE ARCHIVOS
lista_instrucciones=('Inst/instruccion1.txt',
                     'Inst/instruccion2.txt',
                     'Inst/instruccion3.txt',
                     'Inst/instruccion4.txt',
                     'Inst/instruccion5.txt',
                     'Inst/instruccion7.txt',
                     'Inst/instruccion8.txt',
                     'Inst/instruccion9.txt')
lista_imagenes_inst=("img/cañon7.png",
                     'img/letrero_inst.png',
                     'img/teclas_inst.png',
                     'img/ecuaciones.png',
                     'img/imagen_mapa.png',
                     'img/rover.png',
                     'img/r.png',
                     'img/ecuaciones2.png')
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
          'cuadros':"img/cuadros.jpg",
          'cuadro1':"img/cuadros1.jpg"}

sonidos={'fondo':"sound/sonidofondo.wav",
         'explosion':"sound/sonexp.wav"}

lista_canciones=('luna:main theme, hans zimmer',
                 'marte:gymnopedie no.1, erik satie',
                 'tritón:1812 overture, thaikovsky ',
                 'próxima b:arrival of the birds & transformation,the cinematic orchesta',
                 'trappist-1d:claire de lune, debussy',
                 'ganimedes:nocturne op.9,chopin',
                 'espacio:daylight, teremock')
lista_paginas_imagenes=('wall.alphacoders.com/search.php?search=planeta&lang=Spanish',
                        'www.nasa.gov/multimedia/imagegallery/index.html',
                        'www.freepik.es/fotos-vectores-gratis/png')

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

    if numero_instruccion== 3 :
        ancho=400
    elif numero_instruccion==4:
        ancho=300
        alto=250
    elif numero_instruccion==7:
        ancho=800
    else:
        ancho=200

    imagen_inst=pygame.transform.scale(pygame.image.load(lista_imagenes_inst[numero_instruccion]),[ancho,alto])
    menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx,450,ancho,200,' ',letra_botones,white,black,None)
    screen_instrucciones.blit(imagen_inst,[screen_instrucciones.get_rect().centerx-ancho/2,350])



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
                        instrucciones_juego(numero_instruccion=len(lista_instrucciones)-1)

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

    sonidofondo=pygame.mixer.Sound(sonidos['fondo'])
    menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,50,600,100,'Créditos',letra_outro,None,blue,None)
    menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,120,600,100,'Producción',letra_botones,None,blue,None)

    for i in range(len(lista_integrantes)):
        menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,150+20*i,600,100,lista_integrantes[i],letra_creditos1,None,green,None)

    menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,280,100,100,'Música',letra_botones,None,blue,None)

    for i in range(len(lista_canciones)):
        menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,310+20*i,100,100,lista_canciones[i],letra_creditos1,None,green,None)

    menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,480,100,100,'imágenes',letra_botones,None,blue,None)

    for i in range(len(lista_paginas_imagenes)):
         menu.crear_cuadro_de_texto(screen_creditos,screen_creditos.get_rect().centerx,510+20*i,100,100,lista_paginas_imagenes[i],letra_creditos1,None,green,None)



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
        self.g=parametros["g"]
        self.mplano=parametros["im_fondo"]
        self.son_mundo=parametros["son_mundo"]
        self.perdida=parametros["factor_perdida"]
        self.planet=parametros["nombre_planeta"]
        self.vlimt=parametros["vlimt"]
        self.mmini=parametros["im_min"]
        self.xp=parametros["px"]
        self.yp=parametros["py"]
        self.yi=parametros["yi"]
        self.yf=parametros["yf"]
        self.mountain=parametros["mountain"]
        self.little_mountain=parametros["little_mountain"]
        self.rover=parametros["im_objetivo"]
        self.rovertierra=parametros["im_objetivo1"]
        self.phoenix=parametros["im_objetivo2"]
        self.roversito=parametros["im_roversito"]
        self.rovertierrita=parametros["im_rovertierrita"]
        self.fenixito=parametros["im_fenixito"]
        self.yp2=parametros["py2"]
        self.lim_angle=parametros["lim_angle"]
        self.vinf=parametros["vinf"]
        self.piedra=parametros["im_piedra"]
        self.little_piedra=parametros["piedrita"]
        self.lim_anglesup=parametros["lim_anglesup"]
        self.b=parametros["b"]
        self.tipo=parametros["tipo"]
        self.nobjmov=parametros["n_obj_mov"]
        self.escala=10/1 #10pixeles/1metros
        self.lista=[]
        self.lista1=[]

    def rotate(self,surface, angle,g):
        rotated_surface=pygame.transform.rotozoom(surface,angle,1)
        rotated_rect = rotated_surface.get_rect(center=g)
        return rotated_surface,rotated_rect

    def nueva_pos(self,pos_inicial,v,t,escala,sentido,correccion,vobstaculo):
        if pos_inicial[0]==600.0:
            if v[1]!=0:
                self.lista.append(pos_inicial[1])
                self.lista1.append(t)
        pos_final=pos_inicial[0]-v[0]*(0.03317*escala)+vobstaculo[0],pos_inicial[1]-(v[1]*(0.03317*escala))-((sentido)*(0.5*self.g*t*correccion))-vobstaculo[1]

        return pos_final

    def pos_obstaculo(self,pos_inicial,radio,cx,cy):
        angulo = np.arctan2(cy-pos_inicial[1],cx-pos_inicial[0])+0.04     
        xx = cx-radio * np.cos(angulo)
        yy = cy-radio * np.sin(angulo)
        pos_final=xx,yy
        return pos_final

    def dibujar(self,screen,list_img):
        for i in list_img:
            screen.blit(i[0],i[1])
        return

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
        cuadros1=pygame.image.load(imagenes['cuadro1'])
        navecita=pygame.image.load('img/navemini.png')
        nave=pygame.image.load("img/nave.png")

        #DIBUJAR MONTAÑA
        if self.mountain!=1:
            mountain=pygame.image.load(self.mountain)
            little_mountain=pygame.image.load(self.little_mountain)
        elif self.mountain==1:
              mountain=1
        #DIBUJAR PIEDRA
        if self.piedra!=1:
            piedra=pygame.image.load(self.piedra)
            little_piedra=pygame.image.load(self.little_piedra)
        elif self.piedra==1:
              piedra=1
        #DIBUJAR OBSTACULOS QUE EXPLOTAN
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

        #CARGA DE SONIDOS
        sonidoexplosión=pygame.mixer.Sound(sonidos['explosion'])
        sonidofondo=pygame.mixer.Sound(self.son_mundo)
        sonidofondo.set_volume(0.8)
        sonidofondo.play(-1)

        #POSICION DE IMAGENES Y VARIABLES A UTILIZAR
        x0,y0=400,350
        posimg=x0,y0
        xf=3600                                                                                     #Limites de la imagen de fondo
        
        #POSICION DE OBJETIVO
        if nivel==6:
            posobjetivo= random.randrange(1800,xf-200), -1200
        elif nivel==3:
            posobjetivo= random.randrange(1800,xf-200), 980
        elif nivel==1 or nivel==4:
            posobjetivo= random.randrange(3000,xf-100), 0
        else:
            posobjetivo= random.randrange(200,xf-100), random.randrange(self.yi,self.yf-100)            #Posición aleatoria del objetivo

        xo=x0+posobjetivo[0]
        yo=y0-posobjetivo[1]
        posobjetivo=(xo,yo)
        distancia=((posobjetivo[0]-posimg[0])/self.escala),-((posobjetivo[1]-posimg[1])/self.escala)
        
        #POSICIONES DE OTROS ELEMENTOS
        posplano=self.xp,self.yp
        pos_canon=(x0-64,y0-64)
        pos_bola= -x0,-y0
        pos_expl= -x0,-y0                                                                               #Posición de la explosión antes de disparar

        pos_canonsito=(20,400+(self.yf*0.05))
        pos_expli= -x0,-y0
        posobjetivito=(15+(distancia[0]*0.5),395+(self.yf*0.05)-(distancia[1]*0.5))                     #Distancia al objetivo
        pos_bolita=-x0,-y0                                                                              #Declaración de posición inicial de la bala

        pos_rover=[xo-300,yo-300]#[1500,-2000]
        pos_rovertierra=400,250
        pos_phoenix=1000,-1000
        distanciarover=pos_rover[0]-x0, pos_rover[1]-y0
        distanciarovertierra=pos_rovertierra[0]-x0
        distanciaphoenix=pos_phoenix[0]-x0,pos_phoenix[1]-y0

        if nivel == 10:
            Naves=[]
            for i in range(self.nobjmov):
                vv=True
                while vv:
                    xn,yn=x0+random.randrange(200,xf-200), y0-random.randrange(self.yi,self.yf-200)
                    pos_nave=xn,yn
                    distancia_n=((xn-posimg[0])/self.escala),-((yn-posimg[1])/self.escala)
                    v=np.sqrt(((xo-xn)**2)+((yn-yo)**2))
                    if v>500:
                        vv=False
                        pos_navecita=(20+(distancia_n[0]*0.5)-7.5,400+(self.yf*0.05)-(distancia_n[1]*0.5)-7.5)
                        Naves.append(((xn,yn),(pos_navecita)))               
                
            pos_nave=[]
            for i in range(self.nobjmov):
                pos_nave.append([Naves[i][0][0],Naves[i][0][1]])  
            pos_nave=np.array(pos_nave)    

        #VARIABLES DE INICIALIZACION DEL JUEGO
        step= 0,0                                                                                       #vector velocidad
        angle=0                                                                                         #Declaración de variable ángulo del cañon
        speedangle=0                                                                                    #Variable que almacena la rotación del cañon
        dt=0
        v0=self.vinf                                                                                           #Velocidad inicial
        vi=self.vinf
        vr=10
        vrt=10
        vrpy=10
        vrpx=10
        speedv0=0
        t=0
        t1=0                                                                                           #Variable de tiempo
        image_alpha=254
        fino=False
        colision=False
        disparo=False
        gameover=False
        pseg=True
        running=True                                                                                    #Variable que mantiene activo el juego

        while(running):

            clock.tick(30)                                                                          #Periodo de recarga de imagen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                                                          #Permite salir del juego
                    pygame.quit()
                    quit()

                #INTERACCIONES POR MEDIO DE TECLADO EN EL JUEGO
                elif event.type == pygame.KEYDOWN:                                                     #Evento presionar tecla
                    if event.key==pygame.K_SPACE:                                                      #Tecla espacio
                        if colision==True:                                                             #NO TIENE EFECTO
                            step=(0,0)

                        if disparo==False:
                            v_x0=vi*np.cos(np.radians(angle))                                         #Velocidad inicial en x
                            v_y0=-vi*np.sin(np.radians(angle))                                                                      #Velocidad inicial en y(Es negativa porque el pixel (0,0) se encuentra en la esquina sup izq)
                            step=v_x0,v_y0                                                                                          #Tras presionar la tecla espacio
                            dt=1
                            pos_bola=(x0,y0)
                            pos_bolita=(20,400+(self.yf*0.05))
                            pos_expl=(x0+50,y0-100)                                                                                      #posición de la explosión al disparar
                            pos_expli=(20,400+(self.yf*0.05))
                            disparo=True

                            speedv0=0
                            speedangle=0
                            ESCALA=self.escala

                            X0=int(x0/ESCALA)
                            Y0=4000+self.yp-y0
                            Y0=int(Y0/ESCALA)
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
                            IMPACTOS=[(X0+(xo-x0)/10,YOBJ,5,True)]
                            MAX_REBOTES=10
                            if self.nobjmov!=0:
                                for i in range(self.nobjmov):
                                    IMPACTOS.append((X0+(Naves[i][0][0]-x0)/10,int((4000+self.yp-Naves[i][0][1])/ESCALA),20,False))
                            B=self.b
                            TIPO=self.tipo
                            aa=mov.calc_vect(X0,Y0,THETA0,V0,G,E,XLIM,YLIM,YLIMINF,EPSILON,IMPACTOS,MAX_REBOTES,B,TIPO)
                            sonidofondo.set_volume(0.5)
                            sonidoexplosión.play()

                    elif event.key==pygame.K_UP and disparo==False:                                     #Tecla izquierda rotación en sentido positivo
                        if fino==True and pseg==True:
                            speedv0=0.1
                        elif fino==False and pseg==True:
                            speedv0=1

                    elif event.key==pygame.K_DOWN and disparo==False:                                   #Tecla derecha rotación en sentido negativo
                        if fino==True:
                            speedv0=-0.1
                        elif fino==False:
                            speedv0=-1

                    elif (event.key==pygame.K_LEFT and disparo==False):                                 #Tecla izquierda rotación en sentido positivo
                        if fino==True and pseg==True:
                            speedangle=0.1
                        elif fino==False and pseg==True:
                            speedangle=1

                    elif event.key==pygame.K_RIGHT and disparo==False:                                  #Tecla derecha rotación en sentido negativo
                        if fino==True:
                            speedangle=-0.1
                        elif fino==False:
                            speedangle=-1

                    elif event.key==pygame.K_n and disparo==False:                                  #Tecla derecha rotación en sentido negativo
                        sonidofondo.stop()
                        gameover=True
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

                    elif event.key==pygame.K_r and disparo==False:
                        fino=True

                    elif event.key==pygame.K_t and disparo==False:
                        fino=False

            if disparo==True and gameover==False:
                k2=t1*0.03317
                k1=aa[2].flat[np.abs(aa[2]-k2).argmin()]
                k=np.where(aa[2]==k1)[0][0]
            
            pseg=mov.parabolaseguridad(int(x0/self.escala),int((4000+self.yp-y0)/self.escala),np.radians(angle),v0,self.g,int(4000/self.escala),int(4000/self.escala),0.1,self.b,self.tipo)

            if self.g<0.1:
                pseg=True

            if pseg==False and self.g>0.1:
                angle=angle-1
                v0=v0-1
                pseg=True

            #ROTACION DEL CAÑON
            angle=angle+speedangle
                                                                      #Incrementa el ángulo del cañon de acuerdo a las teclas presionadas
            #LIMITES DE ROTACION DEL CAÑON
            if angle>=self.lim_anglesup:
                angle=self.lim_anglesup

            elif angle<=self.lim_angle:
                angle=self.lim_angle

            v0=v0 + speedv0
            vi=vi + speedv0
            if v0>=self.vlimt:
                v0=self.vlimt
            if vi>=self.vlimt:
                vi=self.vlimt
            if v0<=self.vinf:
                v0=self.vinf
            if vi<=self.vlimt:
                vi=self.vlimt

            image2_rotated , image2_rotated_rect = self.rotate(cañon,angle,posimg)
            image3_rotated , image3_rotated_rect = self.rotate(cañonsito,angle,pos_canonsito)

            explosion_rotated , explosion_rotated_rect = self.rotate(explosion,angle,posimg)                                                         #Rota el cañon
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
            if mountain==1 and rover==1 and piedra==1:
                self.dibujar(screen,((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base)))
                if self.nobjmov!=0:
                    pos_nave1=pos_nave-200
                    for i in range(self.nobjmov):
                        screen.blit(nave,pos_nave1[i])
                    
                    self.dibujar(screen,((mini,(0,400)),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito)))
                    for i in range(self.nobjmov):
                        screen.blit(navecita,Naves[i][1])
                else:
                    self.dibujar(screen,(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito))))
            elif mountain!=1:
                self.dibujar(screen,(((plano,posplano),(cuadros,(0,0)),(mountain,(pos_base[0]-500,pos_base[1]-250)),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(little_mountain,(pos_basesita[0]-10,pos_basesita[1]+3)))))
            elif rover!=1:
                self.dibujar(screen,(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(fenixito,distanciaphoenix),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(roversito,pos_roversito),(rover,pos_rover),(rovertierra,pos_rovertierra),(phoenix,pos_phoenix),(rovertierrita,(distanciarovertierra,550)))))
            elif piedra!=1:
                self.dibujar(screen,(((plano,posplano),(cuadros,(0,0)),(piedra,(pos_base[0]+1300,pos_base[1]-1000)),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(little_piedra,(pos_basesita[0]+60,pos_basesita[1]-40)))))

            #OBTENCION DE COLISION OBJETIVO-BOLA
            bolarect=bola.get_rect(center=pos_bola)
            b=bolarect.center

            #COLISION CON ROVER, PHOENIX Y ROVERTIERRA
            c=pos_rover[0]+100,pos_rover[1]+65
            d=pos_rovertierra[0]+100,pos_rovertierra[1]+88
            e=pos_phoenix[0]+100,pos_phoenix[1]+35
            if self.rover!=1 and ((((c[0]-b[0])**2)+((c[1]-b[1])**2))**(0.5))<100:
                self.dibujar(screen,(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(explosion,(pos_rover[0]-220,pos_rover[1]-100)),(bola,pos_bola1),(explosion_rotated,pos_rover),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(fenixito,distanciaphoenix),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(roversito,distanciarover),(rovertierra,pos_rovertierra),(phoenix,pos_phoenix))))#,(rovertierrita,(distanciarovertierra,550))))
                step=(0,0)
                vr=0
                vrt=0
                vrpx=0
                vrpy=0
                sonidofondo.stop()
                gameover=True

                #CHOQUE CON ROVERTIERRA
            if self.rover!=1 and ((((d[0]-b[0])**2)+((d[1]-b[1])**2))**(0.5))<100:
                self.dibujar(screen,(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(explosion,(pos_bola1[0]-220,pos_bola1[1]-120)),(bola,pos_bola1),(explosion_rotated,pos_rover),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(fenixito,distanciaphoenix),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(roversito,distanciarover),(phoenix,pos_phoenix),(rovertierrita,(distanciarovertierra,550)))))
                step=(0,0)

                vr=0
                vrt=0
                vrpx=0
                vrpy=0
                sonidofondo.stop()
                gameover=True
                sonidofondo.stop()
            if self.rover!=1 and ((((e[0]-b[0])**2)+((e[1]-b[1])**2))**(0.5))<50:
                self.dibujar(screen,(((plano,posplano),(cuadros,(0,0)),(objetivo,posobjetivo1),(explosion,(pos_bola1[0]-220,pos_bola1[1]-120)),(bola,pos_bola1),(explosion_rotated,pos_rover),(image2_rotated,cc),(base,pos_base),(mini,(0,400)),(fenixito,distanciaphoenix),(bolita,pos_bolita),(image3_rotated,cc1),(basesita,pos_basesita),(explosionsita_rotated,cd1),(objetivito,posobjetivito),(roversito,distanciarover),(rovertierra,pos_rovertierra),(rovertierrita,(distanciarovertierra,550)))))
                sonidofondo.stop()
                step=(0,0)
                vr=0
                vrt=0
                vrpx=0
                vrpy=0
                sonidofondo.stop()
                gameover=True
            if self.piedra!=1 and (pos_base[0]+1600)<b[0]<pos_base[0]+1300 +1000 and pos_base[1]-900<b[1]<pos_base[1]+91:
                step=(0,0)
                sonidofondo.stop()
                gameover=True
            if nivel==3 and (pos_base[0]+2100)<b[0] and pos_base[1]-700<b[1]<pos_base[1]+91 :
                step=(0,0)
                sonidofondo.stop()
                gameover=True
            t=t+dt
            t1+=dt

            # CONDICION DE IMPACTO
            if colision==True:
                menu.crear_cuadro_de_texto(screen,425,375,450,35,'¡Buen tiro, presiona A para avanzar!',letra_letreros,black,blue,blue)

            if gameover==True and colision==False:
                menu.crear_cuadro_de_texto(screen,425,375,470,37,'¡Fallaste, presiona A para continuar ó s para repetir el nivel!',letra_letreros,black,blue,blue)
                t=0

            # CALCULO DE NUEVAS POSICIONES
            if disparo==True:
                posplano=x0-10*aa[0][k],y0-4000+10*(aa[1][k])
                posobjetivo=x0+xo-10*aa[0][k],y0+yo-4000-self.yp+10*(aa[1][k])
                pos_expl=x0+450-10*(aa[0][k]),y0-3750-self.yp+10*(aa[1][k])
                pos_canon=x0+336-10*(aa[0][k]),-3364-self.yp+10*(aa[1][k])
                pos_bolita=0.5*(aa[0][k]),595-0.5*(aa[1][k])
                if self.nobjmov!=0:
                    for i in range(self.nobjmov):
                        pos_nave[i]=(x0+Naves[i][0][0]-10*(aa[0][k]),y0+Naves[i][0][1]-4000-self.yp+10*(aa[1][k]))

                if (k+4)>len(aa[0]):
                    sonidofondo.stop()
                    step=(0,0)
                    t=0
                    if aa[4]==True:
                        colision=True
                    else:
                        gameover=True
                        colision=False

            if rover!=1 and not(nivel==7):
             pos_rover=self.nueva_pos(pos_rover,step,t,10,1,0.022,(vr,0))
             pos_rovertierra=self.nueva_pos(pos_rovertierra,step,t,10,1,0.022,(vrt,0))
             pos_phoenix=self.nueva_pos(pos_phoenix,step,t,10,1,0.022,(vrpx,vrpy))

            if rover!=1 and nivel==7:
                pos_rover=self.pos_obstaculo(pos_rover,300,posobjetivo[0]-100,posobjetivo[1]-65)
                pos_rovertierra=self.nueva_pos(pos_rovertierra,step,t,10,1,0.022,(vrt,0))
                pos_phoenix=self.nueva_pos(pos_phoenix,step,t,10,1,0.022,(2*vrpx,2*vrpy))
                                             
            distanciarover=9+(pos_rover[0]-pos_base[0])*0.05,560+ (pos_rover[1]-pos_base[1])*0.05 
            distanciarovertierra=(pos_rovertierra[0]-pos_base[0])*0.05
            distanciaphoenix=(pos_phoenix[0]-pos_base[0])*0.05,560+(pos_phoenix[1]-pos_base[1])*0.05

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

            menu.crear_cuadro_de_texto(screen,87,45,175,50,'Ángulo',letra_letreros,None,white,None)                       #Agrega un cuadro de texto con el angulo.
            menu.crear_cuadro_de_texto(screen,87,70,175,50,str("{0:.1f}".format(angle))+'º',letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,270,45,250,50,'Velocidad inicial',letra_letreros,None,white,None)
            menu.crear_cuadro_de_texto(screen,270,70,250,50,str("{0:.1f}".format(v0))+"m/s",letra_letreros,None,white,None)
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
            if self.b>0 and self.tipo!=0:
                screen.blit(cuadros1,(625,500))
                menu.crear_cuadro_de_texto(screen,715,550,175,50,'Coef de arrastre',letra_letreros,None,white,None)
                menu.crear_cuadro_de_texto(screen,715,570,175,50,str(self.b)+"N*s/m",letra_letreros,None,white,None)
              
            pygame.display.flip()                                                                                                   #Hace visibles las imagenes cargadas
            screen.fill((black))
            
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
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':4,
          'vinf':10,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0,
          'tipo':0,
          'n_obj_mov':0
          }

p_tierra={'g':9.8,
          'im_fondo': "img/pradera (2).jpg",
          'son_mundo':"sound/sonidofondo1.wav",
          'factor_perdida':0.2,
          'nombre_planeta':'TIERRA',
          'vlimt':300,
          'im_min':"img/mpradera.jpg",
          'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':0,
          'vinf':10,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0.01,
          'tipo':1,
          'n_obj_mov':0}
p_luna={'g':1.6,
          'im_fondo': "img/luna1.jpg",
          'son_mundo':"sound/sonidofondo2.wav",
          'factor_perdida':0.4,
          'nombre_planeta':'LUNA',
          'vlimt':320,
          'im_min':"img/mluna.jpg",
          'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':0,
          'vinf':10,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0,
          'tipo':0,
          'n_obj_mov':0}
p_marte={'g':3.721,
          'im_fondo': "img/marte.jpg",
          'son_mundo':"sound/sonidofondo3.wav",
          'factor_perdida':0.2,
          'nombre_planeta':'MARTE',
          'vlimt':49,
          'im_min':"img/mmarte.jpg",
          'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,'mountain':1,
          'little_mountain':1,
          'im_objetivo':"img/rover.png",
          'im_objetivo1':"img/rovertierra.png",
          'im_objetivo2':"img/phoenix.png",
          'im_roversito':"img/roversito.png",
          'im_rovertierrita':"img/rovertierrita.png",
          'im_fenixito':"img/fenixito.png",
          'py2':-3000,
          'lim_angle':0,
          'vinf':10,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0,
          'tipo':0,
          'n_obj_mov':0}
p_triton={'g':0.78,
          'im_fondo': "img/triton.jpg",
          'son_mundo':"sound/sonidofondo4.wav",
          'factor_perdida':0.3,
          'nombre_planeta':'TRITON',
          'vlimt':2200,
          'im_min':"img/tritonsito.jpg",
          'px':0,
          'py':-1000,
          'yi':-1850,
          'yf':1350,'mountain':"img/montaña.png",
          'little_mountain':"img/montañita.png",
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':-0,
          'vinf':8,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':0,
          'b':0,
          'tipo':0,
          'n_obj_mov':0}


p_ganimedes={'g':1.46,
          'im_fondo': "img/ganimed.jpg",
          'son_mundo':"sound/nocturne.wav",
          'factor_perdida':0.2,
          'nombre_planeta':'GANIMEDES',
          'vlimt':31,
          'im_min':"img/mganimed.jpg",'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':"img/rover.png",
          'im_objetivo1':"img/rovertierra.png",
          'im_objetivo2':"img/phoenix.png",
          'im_roversito':"img/roversito.png",
          'im_rovertierrita':"img/rovertierrita.png",
          'im_fenixito':"img/fenixito.png",
          'py2':-3000,
          'lim_angle':0,
          'vinf':10,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0,
          'tipo':0,
          'n_obj_mov':0}

p_proximab={'g':int(626*10**(-1.5)),
          'im_fondo': "img/proximab.jpg",
          'son_mundo':"sound/sonproximab.wav",
          'factor_perdida':0.01,
          'nombre_planeta':'PRÓXIMA B',
          'vlimt':11500,
          'im_min':"img/mproximab.jpg",'px':0,
          'py':-3150,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3220,
          'lim_angle':0,
          'vinf':50,
          'im_piedra':'img/piedra.png',
          'piedrita':'img/piedrita.png',
          'lim_anglesup':90,
          'b':0,
          'tipo':0,
          'n_obj_mov':0
          }
p_ross={'g':57*10**(-1),
          'im_fondo': "img/ross.jpg",
          'son_mundo':"sound/clair.wav",
          'factor_perdida':0.1,
          'nombre_planeta':'TRAPPIST-1D',
          'vlimt':6100,
          'im_min':"img/mross.jpg",'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':0,
          'vinf':10,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0,
          'tipo':0,
          'n_obj_mov':0
          }
p_gliese={'g':17.39,
          'im_fondo': "img/plan.jpg",
          'son_mundo':"sound/Giorni.wav",
          'factor_perdida':0.8,
          'nombre_planeta':'GLIESE 581-C',
          'vlimt':30000,
          'im_min':"img/mplan.jpg",'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':0,
          'vinf':50,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0,
          'tipo':0,
          'n_obj_mov':0
          }
p_kepler={'g':20,
          'im_fondo': "img/Kepler22b.jpg",
          'son_mundo':"sound/Mattina.wav",
          'factor_perdida':0.8,
          'nombre_planeta':'KEPLER 22b',
          'vlimt':3000,
          'im_min':"img/Kepler22bmini.jpg",'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':1,
          'py2':-3000,
          'lim_angle':0,
          'vinf':50,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0.3,
          'tipo':1,
          'n_obj_mov':0
          }
p_tokio={'g':9.8,
          'im_fondo': "img/tokio.jpg",
          'son_mundo':"sound/tokio.wav",
          'factor_perdida':0.8,
          'nombre_planeta':'INVASIÓN ALIEN',
          'vlimt':3000,
          'im_min':"img/tokiomini.jpg",'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':"img/nave.png",
          'py2':-3000,
          'lim_angle':0,
          'vinf':50,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0.01,
          'tipo':1,
          'n_obj_mov':5
          }
luna=mundo(p_luna)
space=mundo(p_space)
tierra=mundo(p_tierra)
marte=mundo(p_marte)
triton=mundo(p_triton)
ganimedes=mundo(p_ganimedes)
ross=mundo(p_ross)
proximab=mundo(p_proximab)
gliese=mundo(p_gliese)
kepler=mundo(p_kepler)
tokio=mundo(p_tokio)

###############################         EJECUCION DEL JUEGO         ##################################
jugar=True
jugar_outro=True
intro_game()

while jugar:

        nivel=0
        puntos=0
        while jugar_outro:
            if nivel==0:
                jugar_outro=mundo.main(space)
            elif nivel==1:
                jugar_outro=mundo.main(luna)
            elif nivel==2:
                jugar_outro=mundo.main(gliese)
            elif nivel==3:
                jugar_outro=mundo.main(ross)
            elif nivel==4:
                jugar_outro=mundo.main(proximab)
            elif nivel==5:
                jugar_outro=mundo.main(marte)
            elif nivel==6:
                jugar_outro=mundo.main(triton)
            elif nivel==7:
                jugar_outro=mundo.main(ganimedes)
            elif nivel==8:
                jugar_outro=mundo.main(tierra)
            elif nivel==9:
                jugar_outro=mundo.main(kepler)
            elif nivel==10:
                jugar_outro=mundo.main(tokio)
            else:
                jugar_outro=False

        jugar_outro=outro('Menú','intentalo de nuevo')
