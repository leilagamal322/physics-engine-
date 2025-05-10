import pygame
import numpy as np
import random
from physics_engine.particle import Particle
from physics_engine.rigid_body import RigidBody

WIDTH, HEIGHT = 400, 600
BG_COLOR = (30, 30, 60)
GRAVITY = np.array([0, 1800])

def rects_collide(r1, r2):
    return not (r1.pos[0] + r1.size[0] < r2.pos[0] or
                r1.pos[0] > r2.pos[0] + r2.size[0] or
                r1.pos[1] + r1.size[1] < r2.pos[1] or
                r1.pos[1] > r2.pos[1] + r2.size[1])

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    player = RigidBody([WIDTH//2 - 20, HEIGHT - 60], [40, 40], mass=1, color=(0, 255, 255))
    player.on_ground = False


    platforms = [
        RigidBody([WIDTH//2 - 50, HEIGHT - 20], [100, 20], mass=1000, color=(200, 200, 255))
    ]
    for i in range(1, 10):
        x = random.randint(0, WIDTH - 100)
        y = HEIGHT - 80 - i * 60
        platforms.append(RigidBody([x, y], [100, 20], mass=1000, color=(200, 200, 255)))

    scroll_y = 0
    max_height = 0
    game_over = False

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.apply_force(np.array([-2000, 0]))
            if keys[pygame.K_RIGHT]:
                player.apply_force(np.array([2000, 0]))
            if keys[pygame.K_UP] and player.on_ground:
                player.vel[1] = -900
                player.on_ground = False

            player.apply_force(GRAVITY * player.mass)
            player.update(dt)

            if player.on_ground:
                player.vel[0] *= 0.8

            player.on_ground = False
            for plat in platforms:
                if rects_collide(player, plat):
                    if player.vel[1] > 0 and player.pos[1] + player.size[1] - player.vel[1]*dt <= plat.pos[1]:
                        player.pos[1] = plat.pos[1] - player.size[1]
                        player.vel[1] = 0
                        player.on_ground = True

            if player.pos[1] < HEIGHT // 2:
                dy = HEIGHT // 2 - player.pos[1]
                player.pos[1] += dy
                for plat in platforms:
                    plat.pos[1] += dy
                scroll_y += dy

            platforms = [plat for plat in platforms if plat.pos[1] < HEIGHT]
            while len(platforms) < 10:
                x = random.randint(0, WIDTH - 100)
                y = min(plat.pos[1] for plat in platforms) - 60
                platforms.append(RigidBody([x, y], [100, 20], mass=1000, color=(200, 200, 255)))

            max_height = max(max_height, int(scroll_y))

            if player.pos[1] > HEIGHT:
                game_over = True

        screen.fill(BG_COLOR)
        for plat in platforms:
            pygame.draw.rect(screen, plat.color, (*plat.pos, *plat.size))
        pygame.draw.rect(screen, player.color, (*player.pos, *player.size))
        score_text = font.render(f"Score: {max_height//10}", True, (255,255,255))
        screen.blit(score_text, (10, 10))
        if game_over:
            over_text = font.render("Game Over!", True, (255, 100, 100))
            screen.blit(over_text, (WIDTH//2 - 80, HEIGHT//2 - 20))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()