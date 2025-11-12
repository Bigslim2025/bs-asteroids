import pygame
import constants
from circleshape import CircleShape
import shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # Snippet imported from boot.dev 'Build Asteroids using Python' - CH2L5
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.cooldown <= 0:
            new_shot = shot.Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
            new_shot.velocity = shot.pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED        
            self.cooldown = constants.PLAYER_SHOOT_COOLDOWN_SECONDS  # start cooldown, by Boots
    
    def draw(self, screen):
        # Overwritten from Parent Class
        pygame.draw.polygon(screen, pygame.Color("White"), self.triangle(), 2)

    def rotate(self, dt):
        # Increase the rotation on the player axis by the players turning speed times delta time
        self.rotation += constants.PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        # "This is a course on programming, not vector math, so we've done the math for you. 
        # All those words boil down to these two lines of code:"
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # calculates position and rotation
        self.position += forward * constants.PLAYER_SPEED * dt # updates position on screen

    def update(self, dt):
        # Overwritten from Parent Class
        self.cooldown = max(0, self.cooldown - dt)  # decrement and clamp, by Boots
        keys = pygame.key.get_pressed()
        # Maps the keys, using pygame module defaults
        if keys[pygame.K_a]:
            self.rotate(dt)  
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
