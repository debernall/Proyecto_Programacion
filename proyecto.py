# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
def rotate(surface, angle):
    rotated_surface=pygame.transform.rotozoom(surface,angle,1)
    rotated_rect = rotated_surface.get_rect(center=(64,537))
    return rotated_surface,rotated_rect
def main():
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    clock=pygame.time.Clock()
    image = pygame.image.load("plano.jpg")
    image1=pygame.image.load("bolacañon.png")
    image2=pygame.image.load("cañonx.png")
    image2_rect=image2.get_rect(center=(64,537))
    screen.blit(image,(0,0))
    screen.blit(image2,(0,473))
    pygame.display.flip()
    running=True
    pos= 110,460
    step= 0,0
    angle=0
    speedangle=0
    a=0
    n=0
    while(running):
        ns=clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
               if event.key==pygame.K_SPACE:
                   step=25,-40
                   n=0.2
               if event.key==pygame.K_LEFT:
                   speedangle=-1
               if event.key==pygame.K_RIGHT:
                   speedangle=1
            if event.type == pygame.KEYUP:
               if event.key==pygame.K_LEFT:
                   speedangle=0
               if event.key==pygame.K_RIGHT:
                   speedangle=0
            
                   
        screen.blit(image,(0,0))
       
        angle=angle+speedangle
      
        image2_rotated , image2_rotated_rect = rotate(image2,angle)
        screen.blit(image2_rotated,image2_rotated_rect)
        
        
        screen.blit(image1,pos)
        pos=pos[0]+step[0],pos[1]+step[1]+(5*(a**2))
        a=a+n
        print(angle)
       
                   
                   
        
        pygame.display.flip()

        
        
main()#ahora si
