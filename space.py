import pygame, sys

pygame.init() # initiate pygame
screen = pygame.display.set_mode((1280,720)) #Create display surface
clock = pygame.time.Clock() # Crete clock object

while True: # Game loop
    for event in pygame.event.get(): # Check for events / Player input
        if event.type == pygame.QUIT: # Close the game
            pygame.quit()
            sys.exit()
    screen.fill((40,30,51))
    pygame.display.update() # Draw frame
    clock.tick(120) # Control the framerate
