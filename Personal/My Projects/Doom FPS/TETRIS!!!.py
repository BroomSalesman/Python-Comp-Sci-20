import pygame
from copy import deepcopy
from random import choice, randrange


WIDTH, HEIGHT = 10 , 19
TILE = 40
GAME_RESOLUTION = WIDTH * TILE, HEIGHT * TILE
RES = 700, 800
FPS = 60

pygame.init()

screen = pygame.display.set_mode(RES)
game_screen = pygame.Surface(GAME_RESOLUTION)
clock = pygame.time.Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEIGHT)]


# Tetris pieces variables
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


# Animation Variables
animation_counter, animation_speed, animation_limit = 0, 60, 2000

# Background Visuals
background = pygame.image.load("resources/bg.jpg").convert()
game_background = pygame.image.load("resources/bg2.jpg").convert()


# Game Text Variables
main_font = pygame.font.Font('resources/font.ttf', 60)
font = pygame.font.Font('resources/font.ttf', 40)

title_tetris = main_font.render('TETRIS', True, pygame.Color('gold'))
next_piece_title = font.render('NEXT PIECE', True, pygame.Color('orange'))

# Tetris Piece Color Variables
get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

piece = deepcopy(choice(pieces)), deepcopy(choice([pieces]))

colo, next_colorr = get_color(), get_color()


# Border Rule Function
def check_borders():
    if piece[i].x < 0 or piece[i].x > WIDTH - 1:
        return False
    elif piece[i].y > HEIGHT - 1 or field[piece[i].y][piece[i].x]:
        return False
    return True



# Driver code
while True:
    dx, rotate = 0, False
    screen.blit(background, (0, 0))
    screen.blit(game_screen, (20, 20))
    game_screen.blit(game_background, (0, 0))

    #Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # Piece controls
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
                    field[piece_old[i].y][piece_old[i].x] = color
                color = get_color()

                piece = deepcopy(choice(pieces))
                animation_limit = 2000
                break


    # ROTATE TETRIS PIECE
    #I  don't fully understand this, but I think I know what's going on.
    # It is changing the x and y values to turn into...
    # Actually, I think it is using graphing inverse functions logic, or something like that.
    # I only tried inverse functions on Khan Academy once, so I'm not sure if it is exactly like graphing inverse functions.
    center = piece[0]
    piece_old = deepcopy(piece)
    if rotate:
        for i in range(4):
            x = piece[i].y - center.y
            y = piece[i].x -center.x
            piece[i].x = center.x - x
            piece[i].y = center.y + y

            if not check_borders():
                piece = deepcopy(piece_old)
                break

    # CHECK FOR FILLED LINES
    line = HEIGHT - 1
    for row in range(HEIGHT -1, -1, -1):
        counter = 0
        for i in range(WIDTH):
            if field[row][i]:
                counter += 1
            field[line][i] = field[row][i]
        if counter < WIDTH:
            line -= 1


    # DRAW TETRIS GRID
    [pygame.draw.rect(game_screen, (40, 40, 40), square, 1) for square in grid]

    # DRAW TETRIS PIECE
    for i in range(4):
        piece_rect.x = piece[i].x * TILE
        piece_rect.y = piece[i].y * TILE
        pygame.draw.rect(game_screen, color, piece_rect)

    # DRAW FIELD (piecees that have stopped on a surface)
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                piece_rect.x, piece_rect.y = x *TILE, y * TILE
                pygame.draw.rect(game_screen, col, piece_rect)

    # DRAW TITLES
    screen.blit(title_tetris, (450, 10))
    screen.blit(next_piece_title, (450, 30))

    pygame.display.flip()
    clock.tick(FPS)
