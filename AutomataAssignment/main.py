import pygame
from Mover import Mover

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Automata Assignment")
clock = pygame.time.Clock()
FPS = 60

bg_image = pygame.image.load("AutomataAssignment/assets/images/backgroundimage.jpg").convert_alpha()

RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 40)

def draw_bg():
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))

def draw_healthbar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-2, y-2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

def draw_win_screen(winner):
    screen.fill(BLACK)
    text = font.render(f"{winner} WINS!", True, WHITE)
    retry_text = small_font.render("Click to Retry", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2))

mover_1 = Mover(200, 310)
mover_2 = Mover(700, 310)

game_over = False
winner = ""

run = True
while run:
    clock.tick(FPS)
    
    if not game_over:
        draw_bg()

        draw_healthbar(mover_1.health, 20, 20)
        draw_healthbar(mover_2.health, 580, 20)

        mover_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, mover_2)
        
        mover_1.draw(screen)
        mover_2.draw(screen)

        if mover_1.health <= 0:
            game_over = True
            winner = "Player 2"
        elif mover_2.health <= 0:
            game_over = True
            winner = "Player 1"

    else:
        draw_win_screen(winner)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mover_1.health = 100
                mover_2.health = 100
                game_over = False
            if event.type == pygame.QUIT:
                run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()