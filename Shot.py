from CircleShape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame
from random import randint


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

        self.color = (randint(150, 255), 0, randint(0, 150))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)