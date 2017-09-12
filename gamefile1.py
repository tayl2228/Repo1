import pygame

import time

import random

#Initiate pygame
pygame.init()

#Setting game window resolution
display_width = 1024

display_height = 768

theDisplay = pygame.display.set_mode((display_width,display_height))

#Defining colors (RGB)

black = (0,0,0)

white = (255,255,255)

red = (255,0,0)

green = (0,255,0)

blue = (0,0,255)

#Defining size of character in pixels

character_width = 87

#Defining character image
char_img = pygame.image.load(('stickguy2.png'))

#Defining Boxes

def dodge_me(x_location,y_location,width,height,color):
    pygame.draw.rect(theDisplay,color,[x_location, y_location, width, height])
    

#Naming game window
pygame.display.set_caption("Dodge The Boxes")

#Setting game clock
clock = pygame.time.Clock()

#Defining Character Function
def character(x,y):
    theDisplay.blit(char_img,(x,y))

#Displaying Messages on Screen
def display_message(text):
    bigText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects(text,bigText)
    TextRect.center = ((display_width/2),(display_height/2))
    theDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def wall_death():
    display_message('You ran off course!')

def box_crush():
    display_message('Crushed by a box!')

#Player Score
def player_score(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: "+str(score), True, black)
    theDisplay.blit(text, (0,0))


#Game Loop
def game_loop():
    x = (display_width * 0.45)

    y = (display_height * 0.75)

    x_change = 0

    box_start_x = random.randrange(0, display_width)

    box_start_y = -500

    box_height = 90

    box_width = 90

    box_speed = 15

    score = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                elif event.key == pygame.K_RIGHT:
                    x_change = 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                                    
        x += x_change

        theDisplay.fill(white)
        
        dodge_me(box_start_x, box_start_y, box_width, box_height, blue)

        box_start_y += box_speed

        character(x,y)

        player_score(score)
        
        if x > display_width - character_width or x < 0:
            wall_death()

        if box_start_y > display_height:
            box_start_y = 0 - box_height
            box_start_x = random.randrange(0,display_width)
            score += 100

        if y < box_start_y + box_height:
            if x > box_start_x and x < box_start_x + box_width or x + box_width > box_start_x and x + box_width < box_start_x + box_width:
                box_crush()
        
        pygame.display.update()

        clock.tick(60)

game_loop()

pygame.quit()

quit()
    

        

    
