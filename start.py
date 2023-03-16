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
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

FONT = pygame.font.SysFont("comicsans", 16)


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

        self.x_vel = 0
        self.y_vel = 0

# A method to draw the planet of the screen
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2  # Adding this, because we're drawing these in the middle
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

# Force of attraction between two objects
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        # force of attraction - straight line force
        force = self.G * self.mass * other.mass / distance ** 2

        # atan2 takes 2 sides and gives arctan of that, that means theta
        theta = math.atan2(distance_y, distance_x)

        # x force
        force_x = math.cos(theta) * force

        # y force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        # fx - force x, fy - force y
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        # using F = ma
        # using a = v / t
        # F = mv/t
        # v = Ft / m
        self.x_vel += total_fx * self.TIMESTEP / self.mass
        self.y_vel += total_fy * self.TIMESTEP / self.mass

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))





def main():
    run = True

    # Now we are setting up a clock
    #  will set the frame rate of our game, so that it won't go past a certain value
    # This synchronizes our game
    # If we don't set this clock, the game will just at the speed of our computer
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10 ** 23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    # Creating the pygame event loop
    # It's an infinite loop that will keep on running all the time
    while run:

        # maximum frames per second this will be updated
        clock.tick(60)

        # Let's draw something on the screen
        WIN.fill((0, 0, 0))

        # updating the display


        # Following will give us a list of all the events that will occur
        # events e.g., key presses, mouse movements etc.
        # In our game the only event that we will be handling is
        # the user pressing the "X" button to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()
