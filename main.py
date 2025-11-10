# this allows us to use code from the open-source pygame library throughout this file
import pygame # imports pygame module
import constants # imports constants module
import player # imports player module
import asteroid #
import asteroidfield #
from logger import log_state


def main():
    pygame.init() # initialises pygame module on main
    print("Starting Asteroids!") # initialises message
    print(f"Screen width: {constants.SCREEN_WIDTH}") # shows screen width, needs 'constants.' to import
    print(f"Screen height: {constants.SCREEN_HEIGHT}") # shows screen height, needs 'constants.' to import
    # The Group class is a container that holds and manages objects
    updatable = pygame.sprite.Group() # updatable objects are conteinarased here
    drawable = pygame.sprite.Group() # drawable objects are conteinarased here
    asteroids = pygame.sprite.Group() #

    #
    asteroidfield.AsteroidField.containers = (updatable) 

    #
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    
    # Adds instances of a Player in the groups 'updatable' and 'drawable'
    player.Player.containers = (updatable, drawable) # module.Class.function (try to remember!)
    
    # Sets a new GUI window
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)) 
    # Creates a Player instance and calls for its rendering in the screen
    player_instance = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    # Creates a delta clock for capping the FPS
    delta_clock = pygame.time.Clock()
    dt = 0

    asteroidfield.AsteroidField()

    # Draws the game onto screen and stores the delta clock value onto a variable during runtime
    while True:
        dt = delta_clock.tick(60) # caps the framerate to 60
        dt /= 1000 # converts it to miliseconds
        # Hooks the update method into the loop, uses Group in-built pygame class
        updatable.update(dt) # added by feature-group branch, to be reviewed 
        screen.fill("black") # clears the trail from past frames
        # asteroidfield.AsteroidField()
        # Renders the player on the screen each frame, iterates over Group in-built pygame class 
        for d in drawable:
            d.draw(screen)
        pygame.display.flip() # displays a window with values declared into 'constats.py'
        # Event Handling and Logging
        log_state() # adds and prints a log file, added by lesson updates at boot.dev
        # Makes the window close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

                                     
if __name__ == "__main__":
    main()
