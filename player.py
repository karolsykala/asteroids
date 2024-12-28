import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED
from shot import Shot
class Player(CircleShape):
    rotation = 0
    PLAYER_SHOOT_COOLDOWN = 0.3

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
            self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.cooldown > 0:
            self.cooldown -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.cooldown <= 0:
            self.shoot()
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        shot_direction = pygame.Vector2(0, 1)
        shot_direction = shot_direction.rotate(self.rotation)
        new_shot.velocity = shot_direction * PLAYER_SHOT_SPEED
        self.cooldown = self.PLAYER_SHOOT_COOLDOWN