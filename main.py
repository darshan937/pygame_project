import pygame

#inisilize the pygame
pygame.init()


#create the  screen
screen =  pygame.display.set_mode((500,600))

#title and icom
pygame.display.set_caption('Space Inveders')


icon = pygame.image.load("img.png")
pygame.display.set_icon(icon)





#gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #RGB
    screen.fill((255, 255, 255))
    pygame.display.update()

