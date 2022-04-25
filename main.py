import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
carx = 170
cary = 320
fd = 25
camx_offset = 0
camy_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    camx = carx + camx_offset + 15
    camy = cary + camy_offset + 15
    up_px = window.get_at((camx, camy - fd))[0]
    down_px = window.get_at((camx, camy + fd))[0]
    right_px = window.get_at((camx + fd, camy))[0]
    print(up_px, right_px, down_px)

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        carx = carx + 30
        camx_offset = 0
        camy_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        cary += 30
        camx_offset = 30
        camy_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        carx += 30
        camx_offset = 0
        car = pygame.transform.rotate(car, 90)
    # drive
    if direction == 'up' and up_px == 255:
        cary = cary - 2
    elif direction == 'right' and right_px == 255:
        carx = carx + 2
    elif direction == 'down' and down_px == 255:
        cary = cary + 2
    window.blit(track, (0, 0))
    window.blit(car, (carx, cary))
    pygame.draw.circle(window, (0, 255, 0), (camx, camy), 5, 5)
    pygame.display.update()
