# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 19:25:30 2021

@author: Santiago Vasquez
"""

import pygame
import random
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
import codecs
import menu

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
letra_letreros=pygame.font.SysFont('Fonts/arial_narrow_7.ttf',35)    
letra_instrucciones= pygame.font.Font('Fonts/arial_narrow_7.ttf',35)

# UBICACIONES DE ARCHIVOS
lista_instrucciones=('Inst/instruccion1.txt','Inst/instruccion2.txt','Inst/instruccion3.txt','Inst/instruccion4.txt')
lista_imagenes_inst=("img/cañon7.png",0,'img/teclas_inst.png','img/ecuaciones.png')

imagenes={'intro':"img/fondo_intro.jpg",
          'bola':"img/bolacañonpequeña.png",
          'explosion':"img/explosion1.png",
          'objetivo':"img/objetivo1.png",
          'cañon':"img/cañon8.png",
          'base':"img/cañon9.png"}

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
    
    c_texto=codecs.open(instruccion,'r','utf-8').readlines()
    if numero_instruccion!=1:
        if numero_instruccion== 3:
            ancho=400
            
        else:
            ancho=200
        
        imagen_inst=pygame.transform.scale(pygame.image.load(lista_imagenes_inst[numero_instruccion]),[ancho,200])
        menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx-ancho/2,350,ancho,200,' ',letra_botones,white,black,None)
        screen_instrucciones.blit(imagen_inst,[screen_instrucciones.get_rect().centerx-ancho/2,350])
        
    else:
        menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx-350/2,450,350,50,'Ángulo:25°',letra_letreros,None,green,green)


    for i in range(len(c_texto)):
        menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx-400,100+40*i,800,40,str(c_texto[i].rstrip()),letra_instrucciones,black,green,None)

    menu.crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx-30,50,60,40,str(numero_instruccion+1)+'/4',letra_instrucciones,None,green,green)
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
                        
                elif boton_siguiente.collidepoint(pygame.mouse.get_pos()): 
                    if numero_instruccion+1 in range(len(lista_instrucciones)):
                        inst=False
                        instrucciones_juego(numero_instruccion+1)
                        
        menu.crear_boton(screen_instrucciones,boton_volver_intro,'volver a inicio',letra_botones ,green,yellow,blue,blue)
        menu.crear_boton(screen_instrucciones,boton_anterior,'Anterior',letra_botones ,green,yellow,blue,blue)   
        menu.crear_boton(screen_instrucciones,boton_siguiente,'Siguiente',letra_botones ,green,yellow,blue,blue) 
        menu.pygame.display.flip()


def intro_game():                                                                                                                   #Pantalla de intro
    intro=True
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    pygame.display.set_caption('Parabolic Shot')
    
    intro_background = pygame.image.load(imagenes['intro']) 
    screen.blit(intro_background,(0,0))
    menu.crear_cuadro_de_texto(screen,screen.get_rect().centerx-300,220-50,600,100,'ParaboliC',letra_titulos,None,blue,None) 
    menu.crear_cuadro_de_texto(screen,screen.get_rect().centerx-200,320-50,400,100,'ShoT',letra_titulos,None,blue,None) 
    sonidofondo=pygame.mixer.Sound(sonidos['fondo'])
    
    play=pygame.Rect(screen.get_rect().centerx-350/2,450,350,50)                                                                    #Figuras de los botones jugar y salir
    exit=pygame.Rect(screen.get_rect().centerx-350/2,650,350,50)
    instructions=pygame.Rect(screen.get_rect().centerx-350/2,550,350,50)
    sonidofondo.play()
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
    
def outro(titulo,estado):                                                                                                           # OUTRO MANTIENE AL JUGADOR EN UN NIVEL HASTA QUE PASE
    global nivel    
    global next_level

    pygame.init()
    game_over=True
    screen= pygame.display.set_mode((948,720))
    pygame.display.set_caption(titulo)
    
    intro_background = pygame.image.load(imagenes['intro']) 
    screen.blit(intro_background,(0,0))

    imagenTexto = letra_outro.render(estado,True,blue )                                                                           #Genera la imagen con el texto                             
    imagenTexto1 = letra_outro.render(str(puntos)+" puntos: "+"nivel "+str(nivel),True,blue )
    
    rectanguloTexto1 = imagenTexto1.get_rect()
    rectanguloTexto1.centerx = screen.get_rect().centerx                                                                            #Ubica el texto
    rectanguloTexto1.centery = 150
    rectanguloTexto = imagenTexto.get_rect()                 
    rectanguloTexto.centerx = screen.get_rect().centerx                                                                             #Ubica el texto
    rectanguloTexto.centery = 270
    screen.blit(imagenTexto, rectanguloTexto)                                                                                       #Pone la imagen con el texto en el programa
    screen.blit(imagenTexto1, rectanguloTexto1)

    replay=pygame.Rect(screen.get_rect().centerx-350/2,440,350,50.)    
    re_intro=pygame.Rect(screen.get_rect().centerx-350/2,510,350,50.)
    credits=pygame.Rect(screen.get_rect().centerx-350/2,580,350,50)
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
        
        
        menu.crear_boton(screen,replay,'volver a jugar',letra_botones ,green,yellow,blue,blue)                                           #Los botones se ponen dentro del while para que puedan cambiar de color cuando tienen el cursor encima
        menu.crear_boton(screen,exit1,'Salir',letra_botones ,green,yellow,blue,blue)
        menu.crear_boton(screen,credits,'Créditos',letra_botones ,green,yellow,blue,blue)
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
        self.escala=10/1 #10pixeles/1metros
        self.lista=[]
        self.lista1=[]
    
    def rotate(self,surface, angle):
        rotated_surface=pygame.transform.rotozoom(surface,angle,1)
        rotated_rect = rotated_surface.get_rect(center=(400,350))
        return rotated_surface,rotated_rect
    
    def nueva_pos(self,pos_inicial,v,t):
        if pos_inicial[0]==600.0:
            if v[1]!=0:
                self.lista.append(pos_inicial[1])
                self.lista1.append(t)
        pos_final=pos_inicial[0]-v[0]*(0.03317*self.escala),pos_inicial[1]-(v[1]*(0.03317*self.escala))-(0.5*self.g*t*0.022)
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
        bola=pygame.image.load(imagenes['bola'])                                                                                    #Imagen de bala
        cañon=pygame.image.load(imagenes['cañon'])                                                                                  #Imagen de cañon
        base=pygame.image.load(imagenes['base'])
        explosion=pygame.image.load(imagenes['explosion'])                                                                          #Imagen de la Explosón al disparar
        objetivo=pygame.image.load(imagenes['objetivo'])
        sonidoexplosión=pygame.mixer.Sound(sonidos['explosion'])
        sonidofondo=pygame.mixer.Sound(self.son_mundo)
        
        #POSICION DE IMAGENES Y VARIABLES A UTILIZAR
        x0,y0=400,350
        xf,yf=3440,1653                                                                                                             #Limites de la imagen de fondo    
        
        posobjetivo= random.randrange(200,xf-50), random.randrange(200,yf-50)
        xobj,yobj = posobjetivo[0],posobjetivo[1]
        posobjetivo=(x0+xobj,y0-yobj)
        posplano=x0-400,y0-1650
        pos_canon=(x0-64,y0-64)

        running=True                                                                                                                #Variable que mantiene activo el juego
        posimg=x0,y0
        distancia=((posobjetivo[0]-posimg[0])/self.escala),-((posobjetivo[1]-posimg[1])/self.escala)
        pos_bola= -x0,-y0                                                                                                           #Declaración de posición inicial de la bala
        pos_expl= -x0,-y0                                                                                                           #Posición de la explosión antes de disparar
        step= 0,0                                                                                                                   #vector velocidad
        angle=0                                                                                                                     #Declaración de variable ángulo del cañon
        speedangle=0                                                                                                                #Variable que almacena la rotación del cañon                                         
        n=0
        v0=1                                                                                                                        #Velocidad inicial
        vi=1
        speedv0=0
        t=0  
        t1=0                                                                                                                        #Variable de tiempo

        colision=False
        disparo=False
        gameover=False
        image_alpha=254
        
        sonidofondo.play() 
        while(running):
            ns=clock.tick(30)
                                                                                                                                    #Periodo de recarga de imagen
            for event in pygame.event.get():            
                if event.type == pygame.QUIT:                                                                                       #Permite salir del juego
                    pygame.quit()
                    quit()
                
                #INTERACCIONES POR MEDIO DE TECLADO EN EL JUEGO
                elif event.type == pygame.KEYDOWN:                                                                                  #Evento presionar tecla
                    if event.key==pygame.K_SPACE:                                                                                   #Tecla espacio 
                        if colision==True:
                            step=(0,0)
                            
                        elif disparo==False:
                            v_x0=vi*np.cos(np.radians(angle))                                                                       #Velocidad inicial en x
                            v_y0=-vi*np.sin(np.radians(angle))                                                                      #Velocidad inicial en y(Es negativa porque el pixel (0,0) se encuentra en la esquina sup izq)           
                            step=v_x0,v_y0                                                                                          #Tras presionar la tecla espacio 
                            n=1
                            pos_bola=(x0,y0)  
                            pos_expl=(x0+50,y0-100)                                                                                      #posición de la explosión al disparar
                            disparo=True
                            sonidoexplosión.play()
                            speedv0=0 
                            
                    elif event.key==pygame.K_UP and disparo==False:                                                                 #Tecla izquierda rotación en sentido positivo
                        speedv0=1
                   
                    elif event.key==pygame.K_DOWN and disparo==False:                                                               #Tecla derecha rotación en sentido negativo
                        speedv0=-1
                       
                    elif (event.key==pygame.K_LEFT and disparo==False):                                                               #Tecla izquierda rotación en sentido positivo
                        speedangle=1
                    
                    elif event.key==pygame.K_RIGHT and disparo==False:                                                              #Tecla derecha rotación en sentido negativo
                        speedangle=-1
                        
                    elif event.key==pygame.K_a and colision==True:
                        puntos+=1
                        nivel+=1
                        return True
   
                    elif event.key==pygame.K_a and gameover==True:
                        nivel+=1
                        puntos+=0
                        return True
                    elif event.key==pygame.K_s and gameover==True:
                        nivel+=0
                        puntos+=0
                        return True    
                    elif event.key==pygame.K_ESCAPE:                                                                                #Tecla escape sale del juego
                        running = False
                        sonidofondo.stop()
                        return False      
                                                                                                                                    #   AQUI HAY UNA SALIDA 
                elif event.type == pygame.KEYUP:                                                                                    #Eventos dejar de presionar tecla
                    if event.key==pygame.K_UP and disparo==False:                                                                   #Tecla izquierda rotación en sentido positivo
                        speedv0=0
                        
                    elif event.key==pygame.K_DOWN and disparo==False:                                                               #Tecla derecha rotación en sentido negativo
                        speedv0=0   
                        
                    elif event.key==pygame.K_LEFT and disparo==False:                                                               #Dejar de presionar tecla izquierda detiene la rotación
                        speedangle=0
                        
                    elif event.key==pygame.K_RIGHT and disparo==False:                                                              #Dejar de presionar tecla derecha detiene la rotación
                        speedangle=0
            
            
            #ROTACION DEL CAÑON
            angle=angle+speedangle                                                                                                  #Incrementa el ángulo del cañon de acuerdo a las teclas presionadas
            #LIMITES DE ROTACION DEL CAÑON
            if angle>=90:
                angle=90
                
            elif angle<=0:
                angle=0
                
            v0=v0 + speedv0
            vi=vi + speedv0
            if v0>=self.vlimt:
                v0=self.vlimt
            if vi>=self.vlimt:
                vi=self.vlimt
            if v0<=1:
                v0=1                 
            
            image2_rotated , image2_rotated_rect = self.rotate(cañon,angle)
            explosion_rotated , explosion_rotated_rect = self.rotate(explosion,angle)                                                         #Rota el cañon
            cc = (pos_canon[0]+63-int(image2_rotated.get_width()//2),pos_canon[1]+63-int(image2_rotated.get_height()//2))
            cd = (pos_expl[0]-50-int(explosion_rotated.get_width()//2),pos_expl[1]+100-int(explosion_rotated.get_height()//2))
            pos_base=(pos_canon[0]-35,pos_canon[1]-35)
            
            if image_alpha>0 and disparo==True:
                image_alpha-=5
                
            explosion_rotated.set_alpha(image_alpha)
            pos_bola1=(pos_bola[0]-8,pos_bola[1]-8)
            posobjetivo1=(posobjetivo[0]-50,posobjetivo[1]-50)
            
            #DIBUJAR EN PANTALLA LAS DIFERENTES IMAGENES
            self.dibujar_img(((plano,posplano),(objetivo,posobjetivo1),(bola,pos_bola1),(explosion_rotated,cd),(image2_rotated,cc),(base,pos_base)))        
            
            #OBTENCION DE COLISION OBJETIVO-BOLA
            objetivorect=objetivo.get_rect(center=posobjetivo)
            bolarect=bola.get_rect(center=pos_bola)
            a=objetivorect.center
            b=bolarect.center
            r=((((a[0]-b[0])**2)+((a[1]-b[1])**2))**(0.5))
            
            t=t+n
            t1+=n
            
            # CONDICION DE IMPACTO
            if r<50:
                step=(0,0)
                t=0
                colision=True
                sonidofondo.stop()
            
            # ESTADOS DEL JUEGO
            if colision==True:
                menu.crear_cuadro_de_texto(screen,250,350,350,50,'¡Buen tiro, presiona A para avanzar!',letra_letreros,None,red,None)
                
            if gameover==True:
                menu.crear_cuadro_de_texto(screen,250,350,350,50,'¡Fallaste, presiona A para continuar!',letra_letreros,None,red,None)
                t=0
                
            # REBOTES DE LA BOLA
            if posplano[0]<-xf or posplano[0]>= x0 :
                step=(0,0)
                sonidofondo.stop()
                gameover=True                                                                                                      #   AQUI HAY UNA SALIDA SI SE IMPACTA CON LAS PAREDES    
            
            # CALCULO DE NUEVAS POSICIONES
            posplano=self.nueva_pos(posplano,step,t) 
            posobjetivo=self.nueva_pos(posobjetivo,step,t)       
            pos_expl=self.nueva_pos(pos_expl,step,t)
            pos_canon=self.nueva_pos(pos_canon,step,t)  
            
            # REBOTES DE LA BOLA CUANDO IMPACTA CONTRA EL PISO
            horizonte_rect=plano.get_rect(center=(posplano[0]+1900,posplano[1]+2750))                                               #1900 Y 2750 CORRESPONDEN AL DESPLAZAMIENTO DEL RECTANGULO IMAGEN HACIA LA PARTE INFERIOR PARA QUE SIRVA DE REFERENCIA AL CHOQUE BOLA-PISO
            
            if bolarect.colliderect(horizonte_rect) and t>0.3:                                                                      #t>0.3 evita rebotes debidos a una lectura anomala 
                if (step[1]>-0.001 and step[1]<0) or (step[0]<0.1):
                    step=(0,0)
                    sonidofondo.stop()
                    gameover = True                                                                                                #   AQUI HAY UNA SALIDA SI REBOTA 
                    
                else:
                    t=0
                    step=self.f_rebote(step,self.perdida)

            # LIMITE SUPERIOR
            if posplano[1]>y0:
                step=(0,0)
                sonidofondo.stop()                                                                                                  #   AQUI HAY UNA SALIDA SI SE IMPACTA EL TECHO
                gameover=True
            
            print(horizonte_rect, pospl)
            #CUADROS DE TEXTO
            menu.crear_cuadro_de_texto(screen,0,0,350,50,'Ángulo:'+str(angle)+"°",letra_letreros,None,red,None)                       #Agrega un cuadro de texto con el angulo.
            menu.crear_cuadro_de_texto(screen,0,50,350,50,'Velocidad incial:'+str(v0)+"m/s",letra_letreros,None,red,None)
            menu.crear_cuadro_de_texto(screen,0,100,350,50,'Objetivo(x,y): ('+str(distancia[0])+"m,"+str(distancia[1])+"m)",letra_letreros,None,red,None)
            menu.crear_cuadro_de_texto(screen,650,0,150,50,str(puntos)+' puntos',letra_letreros,None,red,None)  
            menu.crear_cuadro_de_texto(screen,650,50,150,50,'Nivel '+str(nivel),letra_letreros,None,red,None)
            menu.crear_cuadro_de_texto(screen,650,100,150,50,str(int(t1*0.03317))+'s',letra_letreros,None,red,None)
            pygame.display.flip()                                                                                                   #Hace visibles las imagenes cargadas
            
###############################   VARIABLES Y CREACION DE MUNDOS    ##################################     
p_space={'g':0,
          
          'im_fondo': "img/fondo0.jpg",
          'son_mundo':"sound/sonidofondo0.wav",
          'factor_perdida':0,
          'nombre_planeta':'ESPACIO',
          'vlimt':100}

p_tierra={'g':9.8,
          
          'im_fondo': "img/pradera1.jpg",
          'son_mundo':"sound/sonidofondo1.wav",
          'factor_perdida':3,
          'nombre_planeta':'TIERRA',
          'vlimt':57}
p_luna={'g':1.6,
          
          'im_fondo': "img/luna.jpg",
          'son_mundo':"sound/sonidofondo1.wav",
          'factor_perdida':1.4,
          'nombre_planeta':'LUNA',
          'vlimt':23}
luna=mundo(list(p_luna.values()))
space=mundo(list(p_space.values()))
tierra=mundo(list(p_tierra.values()))


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
                jugar_outro=mundo.main(tierra)
            elif nivel==2:
                jugar_outro=mundo.main(luna)

            else:
                jugar_outro=False
                
        jugar_outro=outro('Menú','intentalo de nuevo')           