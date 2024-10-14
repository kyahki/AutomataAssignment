import pygame
from Mover import Mover

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Automata Assignment")
clock = pygame.time.Clock()
FPS = 60

bg_image = pygame.image.load("AutomataAssignment/assets/images/background.jpg").convert_alpha()


def draw_bg():
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scale_bg,(0,0))

mover_1 = Mover(200,310)
mover_2 = Mover(700,310)


run = True
while run:
    
    clock.tick(FPS)
    draw_bg()
    mover_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,mover_2)
    mover_1.draw(screen)
    mover_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()