import pygame as pg

pg.init()  # Initialize pygame

y, step, head = segments = [15, 16, 17]
n, apple = step, 99

screen_width, screen_height = 225, 225
screen = pg.display.set_mode([screen_width, screen_height], pg.SCALED)
font = pg.font.Font(None, 30)

score = 0

while segments.count(head) % 2 * head % n * (head & 240):
    for e in pg.event.get(768):
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_UP and step != n:
                step = -n
            elif e.key == pg.K_DOWN and step != -n:
                step = n
            elif e.key == pg.K_LEFT and step != 1:
                step = -1
            elif e.key == pg.K_RIGHT and step != -1:
                step = 1

    segments = segments[apple != head:] + [head + step]

    screen.fill('black')

    if apple == head:
        apple = segments[0]
        score += 1

    for i, v in enumerate([apple] + segments):
        screen.fill('green' if i else 'red', ((v - 1) % n * y, (v - n) // n * y, y, y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 0, screen_width, 30))
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 0))

    pg.display.flip()

    head += step

    pg.time.wait(100)