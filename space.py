import pygame, sys


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self,path,x_pos,y_pos,speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()

    def screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <= 0:
            self.rect.left = 0

class Meteor(pygame.sprite.Sprite):
    def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))

pygame.init() # initiate pygame
screen = pygame.display.set_mode((1280,720)) #Create display surface
clock = pygame.time.Clock() # Crete clock object

spaceship = SpaceShip('spaceship.png',640,500,10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor1 = Meteor('Meteor1.png',400,400,1,1)
meteor_group = pygame.sprite.Group()
meteor_group.add(meteor1)

while True: # Game loop
    for event in pygame.event.get(): # Check for events / Player input
        if event.type == pygame.QUIT: # Close the game
            pygame.quit()
            sys.exit()


    screen.fill((40,30,51))
    spaceship_group.draw(screen)
    meteor_group.draw(screen)
    spaceship_group.update()
    pygame.display.update() # Draw frame
    clock.tick(120) # Control the framerate
