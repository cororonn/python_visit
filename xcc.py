import pygame
import random

w = 600
h = 480
b = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((w,h))
myclock = pygame.time.Clock()

class Spclass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = \
            pygame.image.load("man.png").convert()
        colorkey = self.image.get_at((0,0))

        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(w)
        self.rect.centery = random.randrange(h)
        self.x1 = random.randrange(-3,3)
        self.y1 = random.randrange(-3,3)

    def update(self):
        self.rect.centerx += self.x1
        self.rect.centery += self.y1
        if self.rect.centerx >= \
            w or self.rect.centerx < 0:
            self.x1 = -self.x1

allgroup = pygame.sprite.Group()
for i in range(100):
    allgroup.add(Spclass())
endflag = 0

while endflag ==0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: endflag = 1
        
    screen.fill(b)

    allgroup.update()
    allgroup.draw(screen)
    myclock.tick(60)
    pygame.display.flip()
pygame.quit()