import pygame
pygame.init()
import time
screen = pygame.display.set_mode((600,400))

list_keys = [False,False,False,False]
stitch = pygame.image.load("stitch.png")
space = pygame.image.load("space.png")
stitch_x = 300
stitch_y = 300
font = pygame.font.SysFont("Arial", 30)
while stitch_y < 600:
    space = pygame.transform.scale(space, (600, 400))
    screen.blit(space, (0, 0))
    screen.blit(stitch,(stitch_x,stitch_y))
    text = font.render("Press Arrow keys to move stitch", True, (0,0,255))
    screen.blit(text,(50,200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                list_keys[0] = True
            if event.key == pygame.K_RIGHT:
                list_keys[1] = True
            if event.key == pygame.K_UP:
                list_keys[2] = True
            if event.key == pygame.K_DOWN:
                list_keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                list_keys[0] = False
            if event.key == pygame.K_RIGHT:
                list_keys[1] = False
            if event.key == pygame.K_UP:
                list_keys[2] = False
            if event.key == pygame.K_DOWN:
                list_keys[3] = False
    if list_keys[0]:
        stitch_x = stitch_x - 1
    if list_keys[1]:
        stitch_x = stitch_x + 1
    if list_keys[2]:
        stitch_y = stitch_y - 1
    if list_keys[3]:
        stitch_y = stitch_y + 1
    stitch_y = stitch_y + 0.5
text = font.render("HA you lost", True, (0,0,255))
screen.blit(text,(100,100))
print("HA you lost")
pygame.display.update()
time.sleep(2)    