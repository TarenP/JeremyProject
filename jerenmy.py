
import pygame

import math
from time import sleep

#create the screen
pygame.init()
X_Size = 1000
Y_Size = 1000
screen = pygame.display.set_mode((X_Size,Y_Size))
screen.fill((250,250,250))

#the stuff to be displayed

can = pygame.image.load("Images/trash.png")
can = pygame.transform.scale(can, (200,200))
person = pygame.image.load("Images/BackThrow.png")
person = pygame.transform.scale(person, (300,400))
paper = pygame.image.load("Images/paper.png")
paper = pygame.transform.scale(paper, (50,50))
arrow = pygame.image.load("Images/arrow.png")
arrow = pygame.transform.scale(arrow, (100,100))
pygame.mixer.init()

#create variable to store the papers position
paper_x = 10
paper_y = Y_Size * .35
init_v = -70
angle = 3
init_vx = math.cos(angle)*init_v
init_vy = math.sin(angle)*init_v

time_increment = 1
time = 1
acceleration = 1
angle = 2
#there's a few ways we could do this, generate all the x and y values first and iteratre thru list or calc real time
#y_coord = []
#x_coord = []

inThrow = False
inMotion = False
num = 0



while True:

    if paper_x > 1000:

        paper_x = 10
        paper_y = Y_Size * .35

        # screen.blit(paper, (10 , Y_Size*.35))
        person = pygame.image.load("Images/BackThrow.png")
        person = pygame.transform.scale(person, (300, 400))
        inThrow = False
        inMotion = False
        time = 1
        num = 0

    elif paper_y > 1000:

        paper_x = 10
        paper_y = Y_Size * .35

        # screen.blit(paper, (10 , Y_Size*.35))
        person = pygame.image.load("Images/BackThrow.png")
        person = pygame.transform.scale(person, (300, 400))
        inThrow = False
        inMotion = False
        time = 1
        num = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                inThrow = True
                # d[event.unicode] += 1
                # if inThrow:
                #     pass
                # else:
                #     inThrow = True
            elif event.key == pygame.K_a:
                angle +=10
                arrow = pygame.transform.rotate(arrow, angle)
                angle += 1 % 360  # Value will reapeat after 359. This prevents angle to overflow.
                rect = arrow.get_rect()
                rect.center = (10, Y_Size * .35)  # Put the new rect's center at old center.
            elif event.key == pygame.K_d:
                print('cheese')

            elif event.key == pygame.K_w:
                init_v -= 10
            elif event.key == pygame.K_s:
                init_v += 10

            elif event.key == pygame.K_r:

                paper_x = 10
                paper_y = Y_Size * .35

                # screen.blit(paper, (10 , Y_Size*.35))
                person = pygame.image.load("Images/BackThrow.png")
                person = pygame.transform.scale(person, (300, 400))
                inThrow = False
                inMotion = False
                time = 1
                num = 0


    if inThrow:
            num += 1
            if num == 1:
                person = pygame.image.load("Images/BackThrow.png")
                person = pygame.transform.scale(person, (300,400))
            elif num == 2:
                # sleep(.2)
                person = pygame.image.load("Images/FinishThrow.png")
                person = pygame.transform.scale(person, (350,450))
                time = 1
                inThrow = False
                inMotion = True

    elif inMotion:

        time += time_increment
        paper_x = (init_vx*time)
        paper_y = int((0.5*(time * time)) + init_vy*time + Y_Size * .35)
        sleep(.015)
        # print("X: ", paper_x)
        # print("Y: ", paper_y)

    print(paper_x, paper_y )

    screen.fill((250, 250, 250))
    screen.blit(person, (10, 300))
    screen.blit(can, (800,500))
    # screen.blit(arrow, rect)
    screen.blit(paper,(paper_x, paper_y))
    pygame.display.update()
