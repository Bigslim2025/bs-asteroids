import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
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