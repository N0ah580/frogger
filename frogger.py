# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Import functions for drawing gridlines and using sprites
from pygame_grid import make_grid
from ucc_sprite import Sprite

### SET UP GLOBAL CONSTANTS HERE
WIDTH = 640
HEIGHT = 480
BACKGROUND_COLOR = "#444444"
FONT_COLOR = "#6aa84f"
GAME_OVER_COLOR = "crimson"
START_TIME = 30

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("Frogger")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.LayeredUpdates()

### SET UP YOUR GAME HERE

# Load the images

background_image = pygame.image.load("streets.png")

start_button_image = pygame.image.load("start.png")
start_button_image = pygame.transform.rotozoom(start_button_image, 0, 0.75)
pause_button_image = pygame.image.load("pause.png")
pause_button_image = pygame.transform.rotozoom(pause_button_image, 0, 0.75)
exit_button_image = pygame.image.load("exit.png")
exit_button_image = pygame.transform.rotozoom(exit_button_image, 0, 0.75)

bus_image = pygame.image.load("bus.png")
bus_image = pygame.transform.rotozoom(bus_image, 0, 0.3)
car_image = pygame.image.load("redcar.png")
car_image = pygame.transform.rotozoom(car_image, 0, 0.3)
cruiser_image = pygame.image.load("police.png")
cruiser_image = pygame.transform.rotozoom(cruiser_image, 0, 0.12)
taxi_image = pygame.image.load("taxi.png")
taxi_image = pygame.transform.rotozoom(taxi_image, 0, 0.3)

frog_image = pygame.image.load("frog.png")


# Sprites for the vehicles
vehicles = pygame.sprite.Group()

bus = Sprite(bus_image)
bus.center = (WIDTH / 2, 186)
bus.speed = 1
bus.add(all_sprites, vehicles)

# Sprite which displays the time remaining
baloo_font_small = pygame.font.Font("Baloo.ttf", 36)
time_left = START_TIME
timer = Sprite(baloo_font_small.render(f"{time_left}", True, FONT_COLOR))
timer.center = (2 * WIDTH / 3, 30)
timer.add(all_sprites)

# Sprite with GAME OVER message
baloo_font_large = pygame.font.Font("Baloo.ttf", 72)
game_over = Sprite(baloo_font_large.render("GAME OVER", True, GAME_OVER_COLOR))
game_over.center = (WIDTH / 2, HEIGHT / 2)


### DEFINE HELPER FUNCTIONS



# Main Loop
running = True
while running:
    # Set the frame rate to 60 frames per second
    clock.tick(60)

    for event in pygame.event.get():
        # Check if the quit (X) button was clicked
        if event.type == QUIT:
            running = False

        ### MANAGE OTHER EVENTS SINCE THE LAST FRAME
        


    ### MANAGE GAME STATE FRAME-BY-FRAME
    
    

    # Update the sprites' locations
    all_sprites.update()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)
    screen.blit(background_image, (0, 60))

    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    # screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()

# End the program
pygame.quit()