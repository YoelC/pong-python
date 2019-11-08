import pygame


class Bar:
    vel = 10
    width, height = 20, 300

    def __init__(self, pos):
        self.x, self.y = pos
        self.score = 0

    def down(self):
        self.y += self.vel

    def up(self):
        self.y -= self.vel

    def check_collide(self, WINDOW_HEIGHT):
        collide = False
        if self.y < 0:
            self.y = 0
            collide = True

        if self.y + self.height > WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - self.height
            collide = True

        return collide

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.get_rect())
