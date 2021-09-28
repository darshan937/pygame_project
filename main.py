import pygame

#inisilize the pygame
pygame.init()


#create the  screen
screen =  pygame.display.set_mode((500,600))

#gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



