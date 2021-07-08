#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:28:45 2021

@author: debernal
"""
import pygame


def crear_boton(pantalla,boton,palabra,fuente,color_fondo1,color_fondo2,color_texto,color_borde):                                   #Función para crear botones como los de la intro
    if boton.collidepoint(pygame.mouse.get_pos()):                                                                                  #Cambia el color del boton si el cursor está sobre él  
        pygame.draw.rect(pantalla,color_fondo2,boton,0)
        
    else:
        pygame.draw.rect(pantalla,color_fondo1,boton,0) 
                                                                                                                                    #Dibuja el boton cuando el cursor no está encima
    pygame.draw.rect(pantalla,color_borde,boton,3)
    texto=fuente.render(palabra,True,color_texto)                                                                                   #Genera el texto del botón
    pantalla.blit(texto,(boton.x+(boton.width-texto.get_width())/2,boton.y+(boton.height-texto.get_height())/2))                    #Pone el botón en la pantalla y centra el texto.


def crear_cuadro_de_texto(pantalla,posx,posy,ancho,alto,texto,fuente,color_fondo,color_texto,color_borde):                          #Funcion para realizar cualquier tipo de cuadro de texto
    cuadro=pygame.Rect(posx-ancho/2,posy-alto/2,ancho,alto)                                                                                        #Si se quiere que un cuadro de texto sea transparente o no tenga borde, se pone None en el color de fondo para que sea transparente y None en el color del borde para que no tenga borde
    if color_fondo!=None:
        pygame.draw.rect(pantalla,color_fondo,cuadro,0)
        
    if color_borde!=None:
        pygame.draw.rect(pantalla,color_borde,cuadro,3)
        
    txt=fuente.render(texto,True,color_texto)
    pantalla.blit(txt,(cuadro.x+(cuadro.width-txt.get_width())/2,cuadro.y+(cuadro.height-txt.get_height())/2))
    
