
import pygame

import math
import random
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

can_x = 400
can_y = 400

def reset():
    global person
    global inThrow
    global inMotion
    global time
    global num
    global paper_x
    global paper_y
    global init_v
    global angle
    global time_increment
    global acceleration
    global p1X
    global p1Y
    global p2X
    global p2Y
    global p1fX
    global p1fY
    global p2fX
    global p2fY
    global touched
    global d1
    global d2

    paper_x = 10
    paper_y = Y_Size * .35
    person = pygame.image.load("Images/BackThrow.png")
    person = pygame.transform.scale(person, (300, 400))
    inThrow = False
        
    inMotion = False
    time = 1
    num = 0

    init_v = 20
    angle = 0
    #init_vx = math.cos(angle)*init_v
    #init_vy = math.sin(angle)*init_v

    time_increment = 1
    time = 1
    acceleration = 1
    p1X = 70
    p1Y = 370
    p2X = 150
    p2Y = 370
    touched = True
    p1fX = 70
    p1fY = 370
    p2fX = 150
    p2fY = 370

    d1 = math.sqrt((p1X-paper_x)**2 + (p1Y-paper_y)**2)
    d2 = math.sqrt((p2X-paper_x)**2 + (p2Y-paper_y)**2)

    angle = 0
    #point 1
    p1fX = d1*math.cos(math.radians(angle))
    p1fY = d1*math.sin(math.radians(angle))
    #point 2
    p2fX = d2*math.cos(math.radians(angle))
    p2fY = d2*math.sin(math.radians(angle))

def score():
    global paper_x
    global paper_y
    global can_x
    global can_y


    if paper_x>can_x and paper_x<can_x+can.get_width():
        if paper_y == can_y:
            can_x = random.randrange(200, 800)
            can_y = random.randrange(200, 800)
    reset()
    


    

reset()
while True:
    
    if paper_x > 1000:
        reset()
        

    elif paper_y > 1000:
        reset()

    if paper_x>can_x - 30 and paper_x<can_x and paper_y >= (can_y) and paper_y <= (can_y + int(can.get_height() + 30)):
        reset()
        print("bad")
        
    if paper_x>can_x and paper_x<(can_x+int(can.get_width())) and paper_y >= can_y and paper_y <= (can_y + int(can.get_height())):
        print("scored")
        can_x = random.randrange(200, 800)
        can_y = random.randrange(500, 800)
        reset() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                inThrow = True
            elif event.key == pygame.K_a:
                if -90 < angle and angle < 90:
                    touched = True
                    angle -= 10
                    #point 1
                    p1fX = d1*math.cos(math.radians(angle))
                    p1fY = d1*math.sin(math.radians(angle))
                    #point 2
                    p2fX = d2*math.cos(math.radians(angle))
                    p2fY = d2*math.sin(math.radians(angle))

            elif event.key == pygame.K_d:
                if -90 < angle and angle < 90:
                    touched = True
                    angle += 10
                    #point 1
                    p1fX = d1*math.cos(math.radians(angle))
                    p1fY = d1*math.sin(math.radians(angle))
                    #point 2
                    p2fX = d2*math.cos(math.radians(angle))
                    p2fY = d2*math.sin(math.radians(angle))

            elif event.key == pygame.K_w:
                init_v += 1
                d2 += 5
                p2fX = d2*math.cos(math.radians(angle))
                p2fY = d2*math.sin(math.radians(angle))
            elif event.key == pygame.K_s:
                init_v -= 1
                d2 -= 5
                p2fX = d2*math.cos(math.radians(angle))
                p2fY = d2*math.sin(math.radians(angle))
            elif event.key == pygame.K_r:
                reset()

                #create variable to store the papers position
                


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

        init_vx = math.cos(math.radians(angle)) * init_v
        init_vy = math.sin(math.radians(angle)) * init_v
        paper_x = (init_vx*time)
        paper_y = int((0.5*(time * time)) + init_vy*time + Y_Size * .35)
        sleep(.015)
        # print("X: ", paper_x)
        # print("Y: ", paper_y)
    
    # score()


    screen.fill((250, 250, 250))
    screen.blit(person, (10, 300))
    screen.blit(can, (can_x,can_y))
    pygame.draw.line(screen,(255, 0, 0), (can_x, can_y), (can_x + can.get_width(), can_y), 10)
    if touched and not inMotion:
        pygame.draw.line(screen,(255, 0, 0), (p1fX + paper_x + 20, p1fY + paper_y + 20), (p2fX + paper_x + 20, p2fY + paper_y + 20), 10)
    elif not inMotion:
        pygame.draw.line(screen,(255, 0, 0), (p1fX, p1fY), (p2fX, p2fY), 10)
    # screen.blit(arrow, rect)
    screen.blit(paper,(paper_x, paper_y))
    pygame.display.update()
