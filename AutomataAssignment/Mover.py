import pygame

class Mover():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.action = 0
        self.health = 100
        
        
        self.image_idle = pygame.image.load("AutomataAssignment/assets/images/move1.jpg").convert_alpha()
        self.image_move = pygame.image.load("AutomataAssignment/assets/images/move2.jpg").convert_alpha()
        self.image_jump = pygame.image.load("AutomataAssignment/assets/images/jump1.jpg").convert_alpha()
        self.image_punch = pygame.image.load("AutomataAssignment/assets/images/punch1.jpg").convert_alpha()
        
        
        self.current_image = self.image_idle

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        dx = 0
        dy = 0
        GRAVITY = 1.5
        key = pygame.key.get_pressed()

        
        self.current_image = self.image_idle

        
        if key[pygame.K_a]:
            dx = -SPEED
            self.current_image = self.image_move

        
        if key[pygame.K_d]:
            dx = SPEED
            self.current_image = self.image_move
        if key[pygame.K_w] and not self.jump:
            self.vel_y = -35
            self.jump = True
            self.current_image = self.image_jump
        if key[pygame.K_r] or key[pygame.K_t]:
            self.attack(surface, target)
            self.current_image = self.image_punch 
            if key[pygame.K_r]:
                self.attack_type = 1
            if key[pygame.K_t]:
                self.attack_type = 2

        self.vel_y += GRAVITY
        dy += self.vel_y

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom


        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -=10
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        scaled_image = pygame.transform.scale(self.current_image, (self.rect.width, self.rect.height))
        surface.blit(scaled_image, (self.rect.x, self.rect.y))
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)
