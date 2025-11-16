import random
import pygame
import constants
from circleshape import CircleShape
from logger import log_event

# Inherits the Circle Shape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius): # gives the construct the requested signature
        super().__init__(x, y, radius) 

    def draw(self, screen):
        # Overrides abstract functions on Circle Shape module
        # Draws a circle object using positional arguments from pygame draw, function circle 
        pygame.draw.circle(screen, pygame.Color("White"), self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        # Overrides abstract functions on Circle Shape module
        # Updates the position on screen (Window)
        self.position += (self.velocity * dt)

    def split(self):
        # Splits the Asteroid killing itself and generating None or smaller asteroids (see below)
        self.kill()
        # Destrois Asteroid if too small to be splited 
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split") # logs event: Asteroid Split
        
        # Sends the split Asteroids to a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50) 
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle) # oposite direction
        
        # Computes the new radius of the smallers asteroids 'new_a' and 'new_b'
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2 # creates Asteroid from 'a' and sets its velocity
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2 # creates Asteroid from 'b' and sets its velocity