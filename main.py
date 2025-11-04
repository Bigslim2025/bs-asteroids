# this allows us to use code from the open-source pygame library throughout this file
import pygame # imports pygame module
import constants # imports constants module
from constants import * # imports all variables from constants, used wildcard 

def main():
    pygame.init() # initialises pygame module on main
    print("Starting Asteroids!") # initialises message
    print(f"Screen width: {constants.SCREEN_WIDTH}") # shows screen width
    print(f"Screen height: {constants.SCREEN_HEIGHT}") # shows screen height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # sets a new GUI window

    # Creates a delta clock for capping the FPS
    delta_clock = pygame.time.Clock()
    dt = 0

    # Draws the game onto screen and stores the delta clock value onto a variable during runtime
    while True:
        pygame.display.flip() # displays a window with values declared into constats.py
        dt = delta_clock.tick(60) # caps the framerate to 60
        dt /= 1000 # converts it to miliseconds
        
        # Event Handling
        # Makes the window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

                                     
if __name__ == "__main__":
    main()
