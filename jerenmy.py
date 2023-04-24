
import pygame

import math
import random
import time

#create the screen
pygame.init()

# initializing pygame
pygame.font.init()
 
# check whether font is initialized
# or not
pygame.font.get_init()

X_Size = 1000
Y_Size = 1000
screen = pygame.display.set_mode((X_Size,Y_Size))
screen.fill((250,250,250))

#the stuff to be displayed

can = pygame.image.load("Images/trash1.png")
can = pygame.transform.scale(can, (200,200))
person = pygame.image.load("Images/BackThrow.png")
person = pygame.transform.scale(person, (300,400))
happy = pygame.image.load("Images/Happy.png")
happy = pygame.transform.scale(happy, (500,600))
sad = pygame.image.load("Images/Sad.png")
sad = pygame.transform.scale(sad, (300,400))
paper = pygame.image.load("Images/paper.png")
paper = pygame.transform.scale(paper, (50,50))
pygame.mixer.init()

font1 = pygame.font.SysFont('chalkduster.ttf', 100)
# Render the texts that you want to display
text1 = font1.render('Scored!?!?', True, (255, 0, 0))
textRect1 = text1.get_rect()
# setting center for the first text
textRect1.center = (500, 250)

text2 = font1.render('Miss!', True, (255, 0, 0))
textRect2 = text2.get_rect()
# setting center for the first text
textRect2.center = (500, 250)

can_x = 400
can_y = 400

def reset():
    global finish
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
    global score
    global miss

    
    miss = False
    score = False
    finish = False
    inThrow = False
    inMotion = False
    touched = True



    paper_x = 10
    paper_y = Y_Size * .35
    person = pygame.image.load("Images/BackThrow.png")
    person = pygame.transform.scale(person, (300, 400))
    num = 0
    init_v = 20
    angle = 0

    time_increment = .25
    Time = 1
    acceleration = 1
    p1X = 70
    p1Y = 370
    p2X = 150
    p2Y = 370
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



    

reset()
while True:
    
    if paper_x > 1000 and not score:
        miss = True
        startTime = time.time()
        

    elif paper_y > 1000 and not score:
        miss = True
        startTime = time.time()

    if paper_x>can_x - 30 and paper_x<can_x and paper_y >= (can_y) and paper_y <= (can_y + int(can.get_height() + 30)) and not score:
        miss = True
        # print("bad")
    if miss ==True and time.time() >= startTime + 5:
        reset()
        
    if paper_x>can_x and paper_x<(can_x+int(can.get_width())) and paper_y >= can_y and paper_y <= (can_y + int(can.get_height())):
        # print("scored")
        score = True
        finish = False
        startTime = time.time()
        #wait 5 seconds from score
    if score ==True and time.time() >= startTime + 5:
        can_x = random.randrange(200, 800)
        can_y = random.randrange(500, 800)
        reset() 
        #Allow for key presses

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not inMotion:
                inThrow = True
            elif event.key == pygame.K_a and not inMotion:
                if -90 < angle and angle < 90:
                    touched = True
                    angle -= 10
                    #point 1
                    p1fX = d1*math.cos(math.radians(angle))
                    p1fY = d1*math.sin(math.radians(angle))
                    #point 2
                    p2fX = d2*math.cos(math.radians(angle))
                    p2fY = d2*math.sin(math.radians(angle))

            elif event.key == pygame.K_d and not inMotion:
                if -90 < angle and angle < 90:
                    touched = True
                    angle += 10
                    #point 1
                    p1fX = d1*math.cos(math.radians(angle))
                    p1fY = d1*math.sin(math.radians(angle))
                    #point 2
                    p2fX = d2*math.cos(math.radians(angle))
                    p2fY = d2*math.sin(math.radians(angle))

            elif event.key == pygame.K_w and not inMotion:
                init_v += 1
                d2 += 5
                p2fX = d2*math.cos(math.radians(angle))
                p2fY = d2*math.sin(math.radians(angle))
            elif event.key == pygame.K_s and not inMotion:
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

                finish = True
                person1= pygame.image.load("Images/FinishThrow.png")
                person1 = pygame.transform.scale(person1, (350,450))
                Time = 1
                inThrow = False
                inMotion = True

    elif inMotion:

        Time += time_increment

        init_vx = math.cos(math.radians(angle)) * init_v
        init_vy = math.sin(math.radians(angle)) * init_v
        paper_x = (init_vx*Time)
        paper_y = int((0.5*(Time * Time)) + init_vy*Time + Y_Size * .35)
        # sleep(.015)
        # print("X: ", paper_x)
        # print("Y: ", paper_y)
    
    
    



    screen.fill((250, 250, 250))
    if finish:
        screen.blit(person1, (10,300))    
    elif score:
        screen.blit(happy, (10,300))
        screen.blit(text1, textRect1)
    elif miss:
        screen.blit(sad, (10,300))
        screen.blit(text2, textRect2)
    else:
        screen.blit(person, (10, 300))
    
    
        
    if score == False:
        screen.blit(can, (can_x,can_y))
    # pygame.draw.line(screen,(255, 0, 0), (can_x, can_y), (can_x + can.get_width(), can_y), 10)
    if touched and not inMotion and score == False:
        pygame.draw.line(screen,(255, 0, 0), (p1fX + paper_x + 20, p1fY + paper_y + 20), (p2fX + paper_x + 20, p2fY + paper_y + 20), 10)
    elif not inMotion and score == False:
        pygame.draw.line(screen,(255, 0, 0), (p1fX, p1fY), (p2fX, p2fY), 10)
    # screen.blit(arrow, rect)
    if score == False:
        screen.blit(paper,(paper_x, paper_y))
    
    pygame.display.update()
