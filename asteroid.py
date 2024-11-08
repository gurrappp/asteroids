import pygame
from circleshape import CircleShape 
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.line_width = 2
        self.color = (255, 255, 255)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, self.line_width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(angle)
        vector_two = self.velocity.rotate(-angle)
        asteroid_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        ateroid_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_one.velocity = vector_one*(1.2)
        ateroid_two.velocity = vector_two*(1.2)

