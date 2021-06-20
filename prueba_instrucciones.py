from proyecto import intro_game
import pygame
import random
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
import codecs

#Archivo de prueba para elaborar las instrucciones
yellow=(245, 245, 66)
green=(22,234,72)
blue=(2,12,207)
black=(0,0,0)
white=(255,255,255)
pygame.init()
letra_botones = pygame.font.SysFont('ravie', 30) 
letra_titulos=pygame.font.SysFont('ravie', 80)  
letra_letreros=pygame.font.SysFont('arial',30)   
letra_instrucciones= pygame.font.SysFont('comicsansms',30)
lista_instrucciones=('instruccion1.txt','instruccion2.txt','instruccion3.txt','instruccion4.txt')
lista_imagenes_inst=("cañon5.png","objetivop.png",0,'ecuaciones.png')

def crear_cuadro_de_texto(pantalla,posx,posy,ancho,alto,texto,fuente,color_fondo,color_texto):      #Funcion para realizar cualquier tipo de cuadro de texto
    cuadro=pygame.Rect(posx,posy,ancho,alto)
    pygame.draw.rect(pantalla,color_fondo,cuadro,0)
    txt=fuente.render(texto,True,color_texto)
    pantalla.blit(txt,(cuadro.x+(cuadro.width-txt.get_width())/2,cuadro.y+(cuadro.height-txt.get_height())/2))

def crear_boton(pantalla,boton,palabra,fuente,color_fondo1,color_fondo2,color_texto):                #Función para crear botones como los de la intro

    if boton.collidepoint(pygame.mouse.get_pos()):                              #Cambia el color del boton si el cursor está sobre él  
        pygame.draw.rect(pantalla,color_fondo2,boton,0)
    else:
        pygame.draw.rect(pantalla,color_fondo1,boton,0)                         #Dibuja el boton cuando el cursor no está encima
    texto=fuente.render(palabra,True,color_texto)                               #Genera el texto del botón
    pantalla.blit(texto,(boton.x+(boton.width-texto.get_width())/2,boton.y+(boton.height-texto.get_height())/2))    #Pone el botón en la pantalla y centra el texto.


def instrucciones_juego(numero_instruccion):
    instruccion=lista_instrucciones[numero_instruccion]
    inst=True
    pygame.init()
    screen_instrucciones=pygame.display.set_mode((948,720))
    intro_background = pygame.image.load("fondo_intro.jpg")

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
        crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx-ancho/2,350,ancho,200,' ',letra_botones,white,black)
        screen_instrucciones.blit(imagen_inst,[screen_instrucciones.get_rect().centerx-ancho/2,350])
        
    else:
        crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx-350/2,450,350,50,'Ángulo:25°',letra_letreros,white,black)

    for i in range(len(c_texto)):
        crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx-400,100+40*i,800,40,str(c_texto[i].rstrip()),letra_instrucciones ,blue,green)

    crear_cuadro_de_texto(screen_instrucciones,screen_instrucciones.get_rect().centerx-30,50,60,40,str(numero_instruccion+1)+'/4',letra_instrucciones,blue,green)   #Crea el cuadro que dice el numero de instruccion

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
                    #intro_game()
                
                elif boton_anterior.collidepoint(pygame.mouse.get_pos()):
                    
                    if numero_instruccion-1 in range(len(lista_instrucciones)):
                        inst=False
                        instrucciones_juego(numero_instruccion-1)
                elif boton_siguiente.collidepoint(pygame.mouse.get_pos()): 
                    if numero_instruccion+1 in range(len(lista_instrucciones)):
                        inst=False
                        instrucciones_juego(numero_instruccion+1)               
        crear_boton(screen_instrucciones,boton_volver_intro,'Volver a inicio',letra_botones ,green,yellow,blue)
        crear_boton(screen_instrucciones,boton_anterior,'Anterior',letra_botones ,green,yellow,blue)   
        crear_boton(screen_instrucciones,boton_siguiente,'Siguiente',letra_botones ,green,yellow,blue) 
        pygame.display.flip()  

intro_game(0)