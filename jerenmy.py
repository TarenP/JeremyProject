
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

can = pygame.image.load("Images/trash1.png")
can = pygame.transform.scale(can, (200,200))
person = pygame.image.load("Images/BackThrow.png")
person = pygame.transform.scale(person, (300,400))
paper = pygame.image.load("Images/paper.png")
paper = pygame.transform.scale(paper, (50,50))
pygame.mixer.init()

#create variable to store the papers position
init_v = -70

#create variable to store the papers position
paper_x = 10
paper_y = Y_Size * .35
<<<<<<< Updated upstream
init_v = -20
angle_deg = 2
#init_vx = math.cos(angle)*init_v
#init_vy = math.sin(angle)*init_v

=======
angle = 0
init_vx = math.cos(angle)*init_v
init_vy = math.sin(angle)*init_v
>>>>>>> Stashed changes
time_increment = 1
time = 1
acceleration = 1
p1X = 70
p1Y = 370
p2X = 150
p2Y = 370
touched = False
p1fX = 70
p1fY = 370
p2fX = 150
p2fY = 370


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
            elif event.key == pygame.K_a:
<<<<<<< Updated upstream
                angle_deg +=10
                arrow = pygame.transform.rotate(arrow, angle)
                angle_deg += 1 % 360  # Value will reapeat after 359. This prevents angle to overflow.
                rect = arrow.get_rect()
                rect.center = (10, Y_Size * .35)  # Put the new rect's center at old center.
=======
                touched = True
                angle -= 10
                #point 1
                d1 = math.sqrt((p1X-paper_x)**2 + (p1Y-paper_y)**2)
                p1fX = d1*math.cos(math.radians(angle))
                p1fY = d1*math.sin(math.radians(angle))
                #point 2
                d2 = math.sqrt((p2X-paper_x)**2 + (p2Y-paper_y)**2)
                p2fX = d2*math.cos(math.radians(angle))
                p2fY = d2*math.sin(math.radians(angle))

>>>>>>> Stashed changes
            elif event.key == pygame.K_d:
                touched = True
                angle += 10
                #point 1
                d1 = math.sqrt((p1X-paper_x)**2 + (p1Y-paper_y)**2)
                print(math.radians(angle))
                p1fX = d1*math.cos(math.radians(angle))
                p1fY = d1*math.sin(math.radians(angle))
                #point 2
                d2 = math.sqrt((p2X-paper_x)**2 + (p2Y-paper_y)**2)
                print(math.radians(angle))
                p2fX = d2*math.cos(math.radians(angle))
                p2fY = d2*math.sin(math.radians(angle))

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
        angle = angle_deg*math.pi/180

        init_vx = math.cos(angle) * init_v
        init_vy = math.sin(angle) * init_v
        paper_x = (init_vx*time)
        paper_y = int((0.5*(time * time)) + init_vy*time + Y_Size * .35)
        sleep(.015)
        # print("X: ", paper_x)
        # print("Y: ", paper_y)


    screen.fill((250, 250, 250))
    screen.blit(person, (10, 300))
    screen.blit(can, (800,500))
    if touched and not inMotion:
        pygame.draw.line(screen,(255, 0, 0), (p1fX + paper_x + 20, p1fY + paper_y + 20), (p2fX + paper_x + 20, p2fY + paper_y + 20), 10)
    elif not inMotion:
        pygame.draw.line(screen,(255, 0, 0), (p1fX, p1fY), (p2fX, p2fY), 10)
    # screen.blit(arrow, rect)
    screen.blit(paper,(paper_x, paper_y))
    pygame.display.update()
