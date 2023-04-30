# We are going to DYNAMICALLY LOAD EVERYTHING
import pygame
from os import listdir
from os.path import isfile, join


pygame.init()

# Caption of the window
pygame.display.set_caption("Platformer")

BG_COLOR = (255,255,255)
w,h = 1090,1080

FPS = 60
PLAYER_vel = 5

# creating a window
window = pygame.display.set_mode((h, w))


# GAME'S ENTIRE EVENT LOOP
def main(window):
    clock = pygame.time.Clock()

    run = True

    while run:
        # clock.tick if we hover, you'll know that it takes FRAMERATE AS INPUT
        # Ensures that our while loop is gonna run 60FPS
        # This makes sure that the game would be of same speed 
        # in a 
        # |fast computer| or a |slow computer|
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)