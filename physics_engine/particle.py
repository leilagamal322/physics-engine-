import numpy as np

class Particle:
    def __init__(self, pos, vel, mass=1.0, radius=5, color=(255, 255, 255)):
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.mass = mass
        self.radius = radius
        self.color = color
        self.force = np.zeros(2)

    def apply_force(self, force):
        self.force += force

    def update(self, dt):
        acc = self.force / self.mass
        self.vel += acc * dt
        self.pos += self.vel * dt
        self.force[:] = 0