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
YELLOW = (255, 255, 0)


# Creating a class to implement plants
# x, y are the positions of the planets on the screen
class Planet:
    # Astronomical Units = (approx.) distance of the earth to the sun
    AU = 149.6e6 * 1000  # 149.6 to the exponent 6 in km --> then we convert it into m by * 1000

    # Gravitational constant
    G = 6.67428e-11

    # We are scaling the planet movement speeds
    SCALE = 250 / AU  # 1AU = 100 pixels

    TIMESTEP = 3600 * 24  # Simulating 1 day in planet's movement

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_velocity = 0
        self.y_velocity = 0

# A method to draw the planet of the screen
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2  # Adding this, because we're drawing these in the middle
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)


def main():
    run = True

    # Now we are setting up a clock
    #  will set the frame rate of our game, so that it won't go past a certain value
    # This synchronizes our game
    # If we don't set this clock, the game will just at the speed of our computer
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    planets = [sun]

    # Creating the pygame event loop
    # It's an infinite loop that will keep on running all the time
    while run:
        # maximum frames per second this will be updated
        clock.tick(60)

        # Let's draw something on the screen
        # WIN.fill(WHITE)

        # updating the display


        # Following will give us a list of all the events that will occur
        # events e.g., key presses, mouse movements etc.
        # In our game the only event that we will be handling is
        # the user pressing the "X" button to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()
