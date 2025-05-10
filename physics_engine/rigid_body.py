import numpy as np

class RigidBody:
    def __init__(self, pos, size, mass=1.0, color=(0, 255, 0)):
        self.pos = np.array(pos, dtype=float)
        self.size = np.array(size, dtype=float)
        self.mass = mass
        self.vel = np.zeros(2)
        self.color = color
        self.force = np.zeros(2)

    def apply_force(self, force):
        self.force += force

    def update(self, dt):
        acc = self.force / self.mass
        self.vel += acc * dt
        self.pos += self.vel * dt
        self.force[:] = 0