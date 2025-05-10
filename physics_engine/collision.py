import numpy as np

def circle_vs_circle(p1, p2):
    dist = np.linalg.norm(p1.pos - p2.pos)
    return dist < (p1.radius + p2.radius)

def aabb_vs_aabb(r1, r2):
    return not (r1.pos[0] + r1.size[0] < r2.pos[0] or
                r1.pos[0] > r2.pos[0] + r2.size[0] or
                r1.pos[1] + r1.size[1] < r2.pos[1] or
                r1.pos[1] > r2.pos[1] + r2.size[1])