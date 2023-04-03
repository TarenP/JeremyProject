
import pygame

#create the screen
pygame.init()
screen = pygame.display.set_mode((1000,1000))
screen.fill((250,250,250))

#the stuff to be displayed

can = pygame.image.load("Images/trash.png")
can = pygame.transform.scale(can, (300,300))
person = pygame.image.load("Images/person.png")
person = pygame.transform.scale(person, (300,400))
paper = pygame.image.load("Images/paper.png")
paper = pygame.transform.scale(paper, (100,100))
pygame.mixer.init()

#create variable to store the papers position
paper_x = 500
paper_y = 500
init_vx = 20
init_vy = 10
time_increment = 1
time = 1
acceleration = 1
#there's a few ways we could do this, generate all the x and y values first and iteratre thru list or calc real time
#y_coord = []
#x_coord = []

it = True
while it:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            it=False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                time += time_increment
                paper_x = init_vx*time
                paper_y = init_vy*time + .5*acceleration*time**2

    screen.fill((250, 250, 250))
    screen.blit(can, (800,500))
    screen.blit(person, (0, 300))
    if paper_x and paper_y:
        screen.blit(paper,(paper_x, paper_y))
    pygame.display.flip()

pygame.quit()