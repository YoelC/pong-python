import pygame
import sys
from classes.aibar import AIBar
from classes.bar import Bar
from classes.ball import Ball
from classes.line import Line

pygame.init()

font = pygame.sysfont.SysFont('Arial', 80)

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 800
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ball = Ball((WINDOW_HEIGHT/2, WINDOW_WIDTH/2))
bar1 = Bar((50, WINDOW_HEIGHT/2 - Bar.height/2))
bar2 = AIBar((WINDOW_WIDTH - 50, WINDOW_HEIGHT/2 - Bar.height/2), ball)
line = Line(WINDOW_WIDTH)

while True:
    clock.tick(30)
    if pygame.QUIT in [event.type for event in pygame.event.get()]:
        sys.exit(0)

    keys = pygame.key.get_pressed()

    # Move bar1
    if keys[pygame.K_w]:
        bar1.up()

    if keys[pygame.K_s]:
        bar1.down()

    bar1.check_collide(WINDOW_HEIGHT)

    # Move bar2
    bar2.move()
    bar2.check_collide(WINDOW_HEIGHT)

    # Ball collisions (bars)
    bar1_rect = bar1.get_rect()
    bar1_rect.x -= 1000
    bar1_rect.width += 1000

    if ball.get_rect().colliderect(bar1_rect):
        ball.x = bar1.x + bar1.width
        ball.x_vel = -ball.x_vel
        ball.increase_vel()

    bar2_rect = bar2.get_rect()
    bar2_rect.width += 1000
    if ball.get_rect().colliderect(bar2_rect):
        ball.x_vel = -ball.x_vel
        ball.x = bar2.x - ball.width
        ball.increase_vel()

    if ball.x > WINDOW_WIDTH:
        ball.x = WINDOW_WIDTH/2 - ball.width/2
        ball.y = WINDOW_HEIGHT/2 - ball.height/2
        ball.reset_vel()
        bar1.y = WINDOW_HEIGHT/2 - bar1.height/2
        bar2.y = bar1.y

        bar1.score += 1

    if ball.x + ball.width < 0:
        ball.x = WINDOW_WIDTH/2 - ball.width/2
        ball.y = WINDOW_HEIGHT/2 - ball.height/2
        ball.reset_vel()
        ball.x_vel = -ball.x_vel
        bar1.y = WINDOW_HEIGHT/2 - bar1.height/2
        bar2.y = bar1.y

        bar2.score += 1

    # Check ball collisions (window)
    if ball.y + ball.height > WINDOW_HEIGHT:
        ball.y = WINDOW_HEIGHT - ball.height
        ball.y_vel = -ball.y_vel

    if ball.y < 0:
        ball.y = 0
        ball.y_vel = -ball.y_vel

    ball.move()

    win.fill(0)

    ball.draw(win)
    bar1.draw(win)
    bar2.draw(win)

    font1 = font.render(f'{bar1.score}', True, (255, 255, 255))
    font1_width, font1_height = font1.get_width(), font1.get_height()

    font2 = font.render(f'{bar2.score}', True, (255, 255, 255))
    font2_width, font2_height = font2.get_width(), font2.get_height()

    win.blit(font1, (WINDOW_WIDTH/4 - font1_width/2, WINDOW_HEIGHT/4))
    win.blit(font2, (WINDOW_WIDTH - WINDOW_WIDTH/4 - font1_width/2, WINDOW_HEIGHT/4))

    line.draw(win)

    pygame.display.flip()
