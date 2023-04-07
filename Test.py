
import pygame
from time import sleep
import math

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
# arrow = pygame.image.load("Images/arrow.png")
# arrow = pygame.transform.scale(arrow, (100,100))
pygame.mixer.init()

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

#create variable to store the papers position
paper_x = 10
paper_y = Y_Size * .35
init_vx = 10
init_vy = 0
time_increment = 1
time = 1
acceleration = 1
angle = 0
aInit_X = 70
aInit_Y = 370
aFin_X = 150
aFin_Y = 370

inThrow = False
inMotion = False
num = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                inThrow = True
            elif event.key == pygame.K_a:
                angle =- 10
                ogInit_X = 70
                ogInit_Y = 370
                ogFin_X = 150
                ogFin_Y = 370
                aInit_X = ogInit_X*math.cos(math.radians(angle)) - ogInit_Y*math.sin(math.radians(angle))
                aInit_Y = ogInit_Y*math.cos(math.radians(angle)) + ogInit_X*math.sin(math.radians(angle))
                aFin_X = ogFin_X*math.cos(math.radians(angle)) - ogFin_Y*math.sin(math.radians(angle))
                aFin_Y = ogFin_Y*math.cos(math.radians(angle)) + ogFin_X*math.sin(math.radians(angle))
                

            # elif event.key == pygame.K_d:

            # elif event.key == pygame.K_w:
            #     #Adjust initial velocity up
            # elif event.key == pygame.K_s:
            #     #Adjust initial velocity down
    if inThrow:
            num += 1
            if num == 1:
                person = pygame.image.load("Images/BackThrow.png")
                person = pygame.transform.scale(person, (300,400))
            elif num == 2:
                # sleep(.2)
                person = pygame.image.load("Images/FinishThrow.png")
                person = pygame.transform.scale(person, (350,450))
                inThrow = False
                inMotion = True
    elif inMotion:
        if paper_x > X_Size - 70:
            inMotion = False
            num = 0
            #Lose
        elif paper_y > 900:
            inMotion = False
            num = 0
            #Lose
        time += time_increment
        paper_x = (init_vx*time)
        paper_y = int((0.5*(time * time)) + init_vy*time + Y_Size * .35)
        sleep(.015)
        # print("X: ", paper_x)
        # print("Y: ", paper_y)

    screen.fill((250, 250, 250))
    screen.blit(person, (10, 300))
    screen.blit(can, (800,500))
    screen.blit(paper,(paper_x, paper_y))
    pygame.draw.line(screen,(255, 0, 0), (aInit_X, aInit_Y), (aFin_X, aFin_Y), 10)
    pygame.display.update()
    pygame.display.flip()