# this allows us to code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(PLAYER_START_POS_X, PLAYER_START_POS_Y)
    asteroidField = AsteroidField()

    dt = 0
    color = (0,0,0)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for sprite in updatable:
            sprite.update(dt)
        
        for sprite in asteroids:
            if sprite.collides_with(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if sprite.collides_with(shot):
                    sprite.split()
                    shot.kill()
            
        screen.fill(color)

        for sprite in drawable:
            sprite.draw(screen)
        
        
        pygame.display.flip()

        # 60 fps
        dt = clock.tick(60) / 1000
    
      
if __name__ == '__main__':
    main()
