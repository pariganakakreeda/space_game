import pygame, sys, random


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self,path,x_pos,y_pos,speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        self.shield_surface = pygame.image.load('shield.png')
        self.health =5

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()
        self.display_health()

    def screen_constrain(self):
        if self.rect.right >= 1696:
            self.rect.right = 1696
        if self.rect.left <= -400:
            self.rect.left = -400

    def display_health(self):
         for index,shield in enumerate(range(self.health)):
             screen.blit(self.shield_surface,(10 + index * 40 ,10))


    def get_damage(self,damage_amount):
        self.health -= damage_amount




class Meteor(pygame.sprite.Sprite):
    def __init__(self,path,x_pos,y_pos,x_speed,y_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed


class Laser(pygame.sprite.Sprite):
    def __init__(self,path,pos,speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed

    def update(self):
        self.rect.centery -= self.speed
        if self.rect.centery <= -100:
            self.kill()


        if self.rect.centery >= 800:
            self.kill()

pygame.init() # initiate pygame
screen = pygame.display.set_mode((1280,720)) #Create display surface
clock = pygame.time.Clock() # Crete clock object

spaceship = SpaceShip('spaceship.png',640,500,10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

#meteor1 = Meteor('Meteor1.png',400,-100,1,4)
meteor_group = pygame.sprite.Group()
#meteor_group.add(meteor1)

laser_group = pygame.sprite.Group()



METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT,250)

while True: # Game loop
    for event in pygame.event.get(): # Check for events / Player input
        if event.type == pygame.QUIT: # Close the game
            pygame.quit()
            sys.exit()
        if event.type == METEOR_EVENT:
           meteor_path = random.choice(('Meteor1.png','Meteor2.png','Meteor3.png'))
           random_x_pos = random.randrange(0,1280)
           random_y_pos = random.randrange(-500,-50)
           random_x_speed = random.randrange(-1,1)
           random_y_speed = random.randrange(4,10)
           meteor = Meteor(meteor_path,random_x_pos,random_y_pos,random_x_speed,random_y_speed)
           meteor_group.add(meteor)

        if event.type == pygame.MOUSEBUTTONDOWN:
           new_laser = Laser('Laser.png',event.pos,5)
           laser_group.add(new_laser)


    screen.fill((40,30,51))
    laser_group.draw(screen)
    spaceship_group.draw(screen)
    meteor_group.draw(screen)

    laser_group.update()
    spaceship_group.update()
    meteor_group.update()


    # Collision
    if pygame.sprite.spritecollide(spaceship_group.sprite,meteor_group,True):
        spaceship_group.sprite.get_damage(1)

    for laser in laser_group:
       pygame.sprite.spritecollide(laser,meteor_group,True)


    pygame.display.update() # Draw frame
    clock.tick(120) # Control the framerate
