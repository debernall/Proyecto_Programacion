
import pygame
def main():
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    clock=pygame.time.Clock()
    image = pygame.image.load("plano.jpg")
    image1=pygame.image.load("pelota2.png")
    image2=pygame.image.load("cañon2.png")
    screen.blit(image,(0,0))
    screen.blit(image2,(0,400))
    pygame.display.flip()
    running=True
    pos= 200,400
    step= 50,-100
    a=0
    while(running):
        ns=clock.tick(5)
        print(ns)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = false
        screen.blit(image,(0,0))
        screen.blit(image2,(0,400))
        screen.blit(image1,pos)
        pos=pos[0]+step[0],pos[1]+step[1]+(5*(a**2))
        a=a+1
        pygame.display.flip()
        
        
main()
