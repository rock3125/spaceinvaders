import sys, pygame
import time
from pygame.locals import *


width = 1024
height =768

speed = [1, 1]
black = 0, 0, 0

# initialise the gaming library
pygame.init()

# setup the display
screen = pygame.display.set_mode((width, height))

# this is a space invader
class SpaceInvader:
    def __init__(self, graphic_1, graphic_2, counter):
        self.invader = [pygame.image.load(graphic_1), pygame.image.load(graphic_2)]
        self.rect = self.invader[0].get_rect()
        self.counter = counter

    def draw(self, screen):
        screen.blit(self.invader[self.counter], self.rect)

    def animate(self):
        self.counter += 1
        if self.counter > 1:
            self.counter = 0

    def move(self, direction):
        self.rect = self.rect.move(direction)


space_invaders = [
    SpaceInvader("graphics/invader_1_1.png", "graphics/invader_1_2.png",0),
    SpaceInvader("graphics/invader_1_1.png", "graphics/invader_1_2.png",1),
    SpaceInvader("graphics/invader_1_1.png", "graphics/invader_1_2.png",0),
    SpaceInvader("graphics/invader_1_1.png", "graphics/invader_1_2.png",1),
]

for i in range(0, len(space_invaders)):
    space_invaders[i].move([70 * i, 0])

# forever
t1 = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # TODO: only during development, remove later
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break

    # clear the screen
    screen.fill(black)

    for si in space_invaders:
        si.draw(screen)

    # draw invader 1
    t2 = time.time()
    diff_in_time = t2 - t1
    if diff_in_time > 0.2:  # this is the game frame-rate (at the moment 5 fps)
        t1 = t2
        for si in space_invaders:
            si.animate()

    pygame.display.flip()
