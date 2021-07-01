import pygame
def main():
    pygame.init()
    screen= pygame.display.set_mode((948,720))
    clock=pygame.time.Clock()
    image2=pygame.image.load("bolacañon.png")
    image2_rect=image2.get_rect(center=(350+32,350+32))
    running=True
   
    while(running):
        ns=clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill((255,255,255))
       
      
     
        screen.blit(image2,(350,350))
        pygame.draw.rect(screen,(0,0,0),image2_rect)
        print(image2_rect)
        pygame.display.flip()
main()
