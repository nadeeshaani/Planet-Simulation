import pygame
import math
pygame.init()

# Using Capital letters here because these are constants
WIDTH, HEIGHT = 800, 800

# Setting up the window
# by taking up the coordinates for the size of the window
# We are passing the coordinates as a tuple here
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# This will give us a pygame surface

# Setting up the title for the window
pygame.display.set_caption("Planet Simulation")

# Defining some colours
WHITE = (255, 255, 255)

def main():
    run = True

    # Now we are setting up a clock
    #  will set the frame rate of our game, so that it won't go past a certain value
    # This synchronizes our game
    # If we don't set this clock, the game will just at the speed of our computer
    clock = pygame.time.Clock()

    # Creating the pygame event loop
    # It's an infinite loop that will keep on running all the time
    while run:
        # maximum frames per second this will be updated
        clock.tick(60)

        #Let's draw something on the screen
        #WIN.fill(WHITE)

        #updating the display
        #pygame.display.update()

        # Following will give us a list of all the events that will occur
        # events e.g., key presses, mouse movements etc.
        # In our game the only event that we will be handling is
        # the user pressing the "X" button to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
