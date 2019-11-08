import pygame


class Line:
    width = 10

    def __init__(self, WINDOW_WIDTH):
        self.x = 0
        self.y = 0

        self.lines = []

        x = WINDOW_WIDTH/2 - self.width/2
        y = -40
        height = 80
        for i in range(6):
            self.lines.append(pygame.Rect(x, y, self.width, height))
            y += height*2

    def draw(self, surface):
        for line in self.lines:
            pygame.draw.rect(surface, (255, 255, 255), line)