import pygame.draw, pygame.key

from CircleShape import CircleShape
from Shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SPACE, \
    PLAYER_SHOT_COOLDOWN_SECONDS
from constants import LEFT, RIGHT, UP, DOWN


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.cooldown_timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        uv = pygame.Vector2(0, 1)
        rv = uv.rotate(self.rotation)
        mv = rv * PLAYER_SPEED * dt

        self.position += mv


    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown_timer -= dt

        if keys[LEFT]:
            self.rotate(dt)
        if keys[RIGHT]:
            self.rotate(-dt)
        if keys[UP]:
            self.move(dt)
        if keys[DOWN]:
            self.move(-dt)
        if keys[SPACE]:
            self.shoot()

    def shoot(self):
        if self.cooldown_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

            self.cooldown_timer = PLAYER_SHOT_COOLDOWN_SECONDS
