import pygame
from pygame.draw import *

# variable
WHITE = (0, 0, 0)
DARKGREEN = (128, 128, 0)
GREY =  (128, 128, 128)
CLARET =  (128, 0, 0)
SHARPYELLOW = (255, 255, 0)
MILDGREY = (211,211,211)
MILDERGREY = (190, 190, 190)
STRONGGREY = (255, 255, 255)
MILDESTGREY = (100, 100, 100)
AVERAGEGREY = (140, 140, 140)
CYAN = (173, 216, 230)

def house(canvas, x, y, size:{(0, 1)}):
    '''Drawing house, there sets screen, x, y, size'''
    rect(canvas, WHITE, (x + 250*size, y + 95*size, 35*size, 55*size))
    rect(canvas,DARKGREEN, (x + 50*size, y + 200*size, 350*size, 500*size))
    polygon(canvas, WHITE, ((x + 25*size, y + 200*size),
                                (x + 425*size, y + 200*size),
                                (x + 375*size, y + 150*size),
                                (x + 75*size, y + 150*size)))
    rect(canvas,GREY, (x + 25*size, y + 375*size, 400*size, 50*size))
    rect(canvas,CLARET, (x + 75*size, y + 225*size, 300*size, 125*size))
    rect(canvas,CLARET, (x + 75*size, y + 475*size, 80*size, 125*size))
    rect(canvas, SHARPYELLOW, (x + 275*size, y + 475*size, 80*size, 125*size))
    rect(canvas,CLARET, (x + 175*size, y + 475*size, 80*size, 125*size))
    rect(canvas, WHITE, (x + 150*size, y + 85*size, 20*size, 80*size))
    rect(canvas,GREY, (x + 30*size, y + 310*size, 390*size, 10*size))
    for i in range(5):
        rect(canvas,GREY, (x + 60*size + 72*size * i, y + 320*size, 40*size,
                           80*size))
    return


def ghost(canvas, x, y, size: {(0, 1)}):
    '''Drawing ghost, there sets screen, x, y, size'''
    circle(canvas, MILDGREY, (x + 75*size, y + 50*size), 30*size)
    circle(canvas, CYAN, (x + 63*size, y + 47*size), 7*size)
    circle(canvas, WHITE, (x + 63*size, y + 47*size), 2*size)
    circle(canvas, CYAN, (x + 82*size, y + 43*size), 7*size)
    circle(canvas, WHITE, (x + 82*size, y + 43*size), 2*size)
    polygon(canvas, MILDGREY, ((x + 75*size, y + 50*size), (x + 50*size,
                                                            y + 60*size),
                                      (x + 45*size, y + 90*size), (x + 60*size,
                                                                   y + 130*size),
                                      (x + 40*size, y + 170*size), (x + 80*size,
                                                                    y + 150*size),
                                      (x + 100*size, y + 165*size), (x + 125*size,
                                                                     y + 145*size),
                                      (x + 140*size, y + 150*size), (x + 160*size,
                                                                     y + 130*size),
                                      (x + 140*size, y + 100*size), (x + 120*size,
                                                                     y + 80*size),
                                      (x + 105*size, y + 50*size)))
    return


def reverse_ghost(canvas, x, y, size):
    '''Drawing reversed ghost, there sets screen, x, y, size'''

    circle(canvas, MILDGREY, (x - 75*size, y + 50*size), 30*size)
    circle(canvas, CYAN, (x - 63*size, y + 47*size), 7*size)
    circle(canvas, WHITE, (x - 63*size, y + 47*size), 2*size)
    circle(canvas, CYAN, (x - 82*size, y + 43*size), 7*size)
    circle(canvas, WHITE, (x - 82*size, y + 43*size), 2*size)
    polygon(canvas, MILDGREY, ((x - 75*size, y + 50*size), (x - 50*size, y + 60*size),
                                      (x - 45*size, y + 90*size), (x - 60*size,
                                                                   y + 130*size),
                                      (x - 40*size, y + 170*size), (x - 80*size,
                                                                    y + 150*size),
                                      (x - 100*size, y + 165*size), (x - 125*size,
                                                                     y + 145*size),
                                      (x - 140*size, y + 150*size), (x - 160*size,
                                                                     y + 130*size),
                                      (x - 140*size, y + 100*size), (x - 120*size,
                                                                     y + 80*size),
                                      (x - 105*size, y + 50*size)))
    return

def draw_ghost(canvas, color, alpha, x, y, size, X, Y):
    '''Drawing ghost on screen, there sets subscreen, color, x, y, alpha, size, X, Y'''
    canvas.set_colorkey(color)
    canvas.set_alpha(alpha)
    ghost(canvas, x, y, size)
    screen.blit(canvas, (X, Y))
def draw_reversed_ghost(canvas, color, alpha, x, y, size, X, Y):
    '''Drawing reversed ghost on screen, there sets subscreen, color, x, y, alpha, size, X, Y'''
    canvas.set_colorkey(color)
    canvas.set_alpha(alpha)
    reverse_ghost(canvas, x, y, size)
    screen.blit(canvas, (X, Y))
def draw_house(canvas, x, y, size, X , Y, color = (0,0,0), alpha = 0):
    '''Drawing reversed house on screen, there sets subscreen, color, x, y, alpha, size, X, Y'''
    canvas.set_colorkey(color)
    canvas.set_alpha(alpha)
    house(canvas, x, y, size)
    screen.blit(canvas, (X, Y))
def draw_cloud(canvas, color, color_cloud, alpha, x, y, a, b, X , Y):
    canvas.set_colorkey(color)
    canvas.set_alpha(alpha)
    ellipse(canvas, color_cloud, (x ,y ,a ,b ))
    screen.blit(canvas, (X, Y))
pygame.init()

FPS = 30
screen = pygame.display.set_mode((720, 1080))

rect(screen, MILDERGREY, (0, 0, 720, 540))
rect(screen, WHITE, (0, 540, 720, 540))


draw_cloud(screen, WHITE, STRONGGREY, 0, 600, 150, 70, 70, 0, 0)
draw_cloud(screen,WHITE, MILDESTGREY, 0, 250 , 175, 500, 100, 0, 0)
draw_cloud(screen, WHITE, GREY, 0 , 100, 220, 600, 75, 0, 0)
draw_cloud(screen, WHITE, AVERAGEGREY, 0, 500 , 100 , 600 ,75, 0, 0)

draw_house(screen, 250, 520, 0.4, 0, 0)

surface_for_cloud1 = pygame.Surface((600, 150))
draw_cloud(surface_for_cloud1,WHITE,MILDESTGREY,200,0,0,600,100,50,700)

draw_house(screen, 500, 275, 0.5, 0, 0)
surface_for_house3 = pygame.Surface((400, 600))
draw_house(surface_for_house3,0,0,0.6,0,600,WHITE,255)

surface_for_cloud2 = pygame.Surface((600, 150))
draw_cloud(surface_for_cloud2,WHITE,MILDESTGREY, 200, 0, 0,600,100,300,550)

surface_for_ghost1 = pygame.Surface((200, 200))
draw_ghost(surface_for_ghost1,WHITE,100,0,0,1,500,600)

surface_for_ghost2 = pygame.Surface((200, 200))
draw_ghost(surface_for_ghost2,WHITE,200,0,0,1,450,650)

surface_for_reversed_ghost1 = pygame.Surface((300, 300))
draw_reversed_ghost(surface_for_reversed_ghost1,WHITE,100,200,0,1,150,900)

surface_for_reversed_ghost2 = pygame.Surface((400, 400))
draw_reversed_ghost(surface_for_reversed_ghost2,WHITE,200,400,0,2,200,800)

surface_for_cloud3 = pygame.Surface((600, 150))
draw_cloud(surface_for_cloud2,WHITE,MILDESTGREY,150, 0 , 0,
           500, 75, 200, 300)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
