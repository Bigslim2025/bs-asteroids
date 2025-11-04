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

    # Draws the game onto screen
    while True:
        pygame.display.flip()

        # Event Handling
        # Makes the window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

                                     
if __name__ == "__main__":
    main()
