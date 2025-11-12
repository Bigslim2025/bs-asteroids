# this allows us to use code from the open-source pygame library throughout this file
import sys # imports exit event
import pygame # imports pygame module
import constants # imports constants module
import player # imports player module
import asteroid # imports asteroid object module
import shot # imports shot object module
import asteroidfield # asteroid field module
from logger import log_state
from logger import log_event


def main():
    pygame.init() # initialises pygame module on main
    print("Starting Asteroids!") # initialises message
    print(f"Screen width: {constants.SCREEN_WIDTH}") # shows screen width, needs 'constants.' to import
    print(f"Screen height: {constants.SCREEN_HEIGHT}") # shows screen height, needs 'constants.' to import
    # The Group class is a container that holds and manages objects
    updatable = pygame.sprite.Group() # updatable objects are conteinarased here
    drawable = pygame.sprite.Group() # drawable objects are conteinerised here
    asteroids = pygame.sprite.Group() # asteroids objects are conteinerised here
    shots = pygame.sprite.Group() # shots objects are conteinerised here

    # Adds instances of the Asteroid Field in the 'updatable' gorup
    asteroidfield.AsteroidField.containers = (updatable) 

    # Adds instances of the Asteroids in the 'updatable', 'drawable' and 'asteroid' gorup
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)

    # Adds instances of the Shots in the 'updatable', 'drawable' and 'asteroid' group
    shot.Shot.containers = (shots, drawable, updatable)
    
    # Adds instances of a Player in the groups 'updatable' and 'drawable'
    player.Player.containers = (updatable, drawable) # module.Class.function (try to remember!)
    
    # Sets a new GUI window
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)) 
    # Creates a Player instance and calls for its rendering in the screen
    player_instance = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    # Creates a delta clock for capping the FPS
    delta_clock = pygame.time.Clock()
    dt = 0
    # Creates the Asteroid Field, spawns and move the asteroids in the screen (AsteroidField.py from boot.dev) 
    asteroidfield.AsteroidField()

    # Draws the game onto screen and stores the delta clock value onto a variable during runtime
    while True:
        dt = delta_clock.tick(60) # caps the framerate to 60
        dt /= 1000 # converts it to miliseconds
        # Hooks the update method into the loop, uses Group in-built pygame class
        updatable.update(dt) # added by feature-group branch, to be reviewed

        # Kills the asteroid and the "bullet"
        for a in asteroids: 
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot") # logs if the asteroid object is shot (game_events.jsonl)
                    pygame.sprite.Sprite.kill(a) # kills asteroid
                    pygame.sprite.Sprite.kill(s) # kills "bullet"

        # Checks if has collision between player object and asteroid object 
        for a in asteroids:
            if a.collides_with(player_instance):
                # Logs a collision and terminates the loop
                log_event("player_hit") # logs if the player object is hit (game_events.jsonl)
                print("Game Over!") # displays a feedback on the game fail state
                sys.exit() # exits the game on fail state

        screen.fill("black") # clears the trail from past frames
        
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
