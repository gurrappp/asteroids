# this allows us to code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(PLAYER_START_POS_X, PLAYER_START_POS_Y)

    color = (0,0,0)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        player.draw(screen)
        pygame.display.flip()

        # 60 fps
        dt = clock.tick(60) / 1000
    
      
if __name__ == '__main__':
    main()
