import pygame
from copy import deepcopy
from random import choice, randrange


WIDTH, HEIGHT = 10 , 20
TILE = 45
GAME_RESOLUTION = WIDTH * TILE, HEIGHT * TILE
FPS = 60

pygame.init()
game_screen = pygame.display.set_mode(GAME_RESOLUTION)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEIGHT)]

pieces_positions = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                            [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                            [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                            [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                            [(0, 0), (0, -1), (0, 1), (-1, -1)],
                            [(0, 0), (0, -1), (0, 1), (1, -1)],
                            [(0, 0), (0, -1), (0, -1), (-1, 0)]]

# List of the pieces (what they should look like)
pieces = [[pygame.Rect(x + WIDTH // 2, y + 1, 1, 1) for x, y in piece_position] for piece_position in pieces_positions]
piece_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

animation_counter, animation_speed, animation_limit = 0, 60, 2000
piece = deepcopy(choice(pieces))


# Checking for border (super simple collision rules)
def check_borders():
    if piece[i].x < 0 or piece[i].x > WIDTH - 1:
        return False
    elif piece[i].y > HEIGHT - 1 or field[piece[i].y][piece[i].x]:
        return False
    return True



# Driver code
while True:
    dx, rotate = 0, False

    game_screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                animation_limit = 100
            elif event.key == pygame.K_UP:
                rotate = True


    # HORIZONTAL MOVEMENT
    piece_old = deepcopy(piece)

    for i in range(4):
        piece[i].x += dx
        if not check_borders():
            piece = deepcopy(piece_old)
            break


    # DOWNWARD MOVEMENT
    animation_counter += animation_speed
    if animation_counter > animation_limit:
        animation_counter = 0

        piece_old = deepcopy(piece)
        for i in range(4):
            piece[i].y += 1

            # This code draws the piece at the bottom, but it is not the piece itself. Like stamps from the turtle library.
            if not check_borders():
                for i in range(4):
                    field[piece_old[i].y][piece_old[i].x] = pygame.Color('white')
                piece = deepcopy(choice(pieces))
                animation_limit = 2000
                break


    # ROTATE TETRIS PIECE
    center = piece[0]
    piece_old = deepcopy(piece)
    if rotate:
        for i in range(4):
            x = piece[i].y - center.y
            y = piece[i].x -center.x
            piece[i] = center.x - x
            piece[i] = center.y + y

            if not check_borders():
                piece = deepcopy(piece_old)
                break

    # DRAW TETRIS GRID
    [pygame.draw.rect(game_screen, (40, 40, 40), square, 1) for square in grid]

    # DRAW TETRIS PIECE
    for i in range(4):
        piece_rect.x = piece[i].x * TILE
        piece_rect.y = piece[i].y * TILE
        pygame.draw.rect(game_screen, pygame.Color('white'), piece_rect)

    # DRAW FIELD
    for y, raw in enumerate(field):
        for x, color in enumerate(raw):
            if color:
                piece_rect.x, piece_rect.y = x *TILE, y * TILE
                pygame.draw.rect(game_screen, color, piece_rect)



    pygame.display.flip()
    clock.tick(FPS)
