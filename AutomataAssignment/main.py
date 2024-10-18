import pygame
from Mover import Mover

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Automata Assignment")
clock = pygame.time.Clock()
FPS = 60


bg_images = [
    pygame.image.load("AutomataAssignment/assets/images/background1.jpg").convert_alpha(),
    pygame.image.load("AutomataAssignment/assets/images/background2.jpg").convert_alpha(),
    pygame.image.load("AutomataAssignment/assets/images/background3.jpg").convert_alpha(),
    pygame.image.load("AutomataAssignment/assets/images/background4.jpg").convert_alpha()
]

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 40)

def draw_healthbar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

def draw_bg(bg_image):
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))

def get_background_index(mover):
    if mover.rect.x < SCREEN_WIDTH // 4:
        return 0
    elif mover.rect.x < SCREEN_WIDTH // 2:
        return 1
    elif mover.rect.x < 3 * SCREEN_WIDTH // 4:
        return 2
    else:
        return 3

def draw_start_screen():
    screen.fill(BLACK)
    text_line1 = font.render("Welcome to Mga Uyab ni Kyle", True, WHITE)
    text_line2 = font.render("as Background", True, WHITE)
    subtext_line1 = small_font.render("#AutomataAssignment - Press any key to start", True, WHITE)
    subtext_line2 = small_font.render("Keep moving so you can see all the Backgrounds!", True, WHITE)
    screen.blit(text_line1, (SCREEN_WIDTH // 2 - text_line1.get_width() // 2, SCREEN_HEIGHT // 2 - 150))
    screen.blit(text_line2, (SCREEN_WIDTH // 2 - text_line2.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(subtext_line1, (SCREEN_WIDTH // 2 - subtext_line1.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(subtext_line2, (SCREEN_WIDTH // 2 - subtext_line2.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

    pygame.display.update()


def draw_win_screen():
    screen.fill(BLACK)
    text = font.render("Thank you for playing", True, WHITE)
    subtext = small_font.render("Mga Uyab ni Kyle as Background game", True, WHITE)
    retry_text = small_font.render("Click to Retry", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(subtext, (SCREEN_WIDTH // 2 - subtext.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
    pygame.display.update()

mover_1 = Mover(200, 310)
mover_2 = Mover(700, 310)

game_over = False
winner = ""
game_started = False

run = True
while run:
    clock.tick(FPS)
    
    if not game_started:
        draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                game_started = True
    else:
        if not game_over:
            bg_index = get_background_index(mover_1)
            draw_bg(bg_images[bg_index])
            draw_healthbar(mover_1.health, 20, 20)
            draw_healthbar(mover_2.health, 580, 20)
            mover_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, mover_2)
            mover_1.draw(screen)
            mover_2.draw(screen)
            if mover_2.health <= 0:
                game_over = True

        else:
            draw_win_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mover_1.health = 100
                    mover_2.health = 100
                    game_over = False
                    game_started = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
