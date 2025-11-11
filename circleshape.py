import pygame

# Pasted from boot.dev 'Build Asteroids using Python' - CH2L4
# Code below not touched by the pupil

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    # Verifies if the asteroid object collides with the player object
    def collides_with(self, other):
        distance = self.position.distance_to(other.position) # defines the distance between objects as a variable  
        return distance <= (self.radius + other.radius) # checks the condition to return a collision
        