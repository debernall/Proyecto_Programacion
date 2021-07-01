# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:09:11 2021

@author: Santiago Vasquez
"""
import pygame
def main():                      ################puntos
        
        #PROPIEDADES INICIALES PYGAME
        pygame.init()
        screen= pygame.display.set_mode((800,700))
        clock=pygame.time.Clock()
        bola=pygame.image.load("bolacañon.jpg")
        bolarect=bola.get_rect()
        running=True
        while(running):
         ns=clock.tick(30)                                                       #Periodo de recarga de imagen
         for event in pygame.event.get():            
            if event.type == pygame.QUIT:                                       #Permite salir del juego
                pygame.quit()
                quit()
            
            
            
        screen.blit(bola,(350,350))
        
main()