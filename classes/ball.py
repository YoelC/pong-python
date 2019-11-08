import pygame


class Ball:
    width, height = 20, 20

    def __init__(self, pos):
        self.x, self.y = pos
        self.x_vel = 0.707 * 10
        self.y_vel = 0.707 * 10

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def increase_vel(self):
        increase = 1.05
        self.x_vel *= increase
        self.y_vel *= increase

    def reset_vel(self):
        self.x_vel = 0.707 * 10
        self.y_vel = 0.707 * 10

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.get_rect())
