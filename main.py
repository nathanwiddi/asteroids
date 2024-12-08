import pygame
import sys
from constants import *
from player import Player
from circleshape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *


def main():   
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()
    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for event in updatable:
            event.update(dt)
        for event in drawable:
            event.draw(screen)

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        for objects in asteroids:
            if objects.collision(player) == True:
                print("Game Over!")
                sys.exit()

    
if __name__ == "__main__":
    main()
