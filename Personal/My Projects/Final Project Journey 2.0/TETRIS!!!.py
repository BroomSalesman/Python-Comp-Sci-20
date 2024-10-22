import pygame
from copy import deepcopy
from random import choice, randrange

DEBUG = True

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
main_font = pygame.font.Font('resources/font.ttf', 55)
font = pygame.font.Font('resources/font.ttf', 35)

title_tetris = main_font.render('TETRIS', True, pygame.Color('gold'))
next_piece_title = font.render('NEXT PIECE', True, pygame.Color('orange'))
title_score = font.render("SCORE:", True, pygame.Color('green'))
title_record = font.render('RECORD:', True, pygame.Color('purple'))

# Tetris Piece Color Variables
get_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

piece, next_piece = deepcopy(choice(pieces)), deepcopy(choice(pieces))
color, next_color = get_color(), get_color()

score, lines = 0, 0
#Determines what score increment is if x number of lines cleared with one piece
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}



# Border Rule Function
def check_borders():
    if piece[i].x < 0 or piece[i].x > WIDTH - 1:
        return False
    elif piece[i].y > HEIGHT - 1 or field[piece[i].y][piece[i].x]:
        return False
    return True

# Keeping record score systems
def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')

def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))



# DRIVER CODE
while True:
    record = get_record()
    dx, rotate = 0, False
    screen.blit(background, (0, 0))
    screen.blit(game_screen, (20, 20))
    game_screen.blit(game_background, (0, 0))
    # delay
    for i in range(lines):
        pygame.time.wait(200)

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


    # HORIZONTAL MOVEMENT (x-axis)
    piece_old = deepcopy(piece)

    for i in range(4):
        piece[i].x += dx
        if not check_borders():
            piece = deepcopy(piece_old)
            break


    # DOWNWARD MOVEMENT (y-axis)
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
                piece, color = next_piece, next_color
                next_piece, next_color = deepcopy(choice(pieces)), get_color()

                animation_limit = 2000
                break


    # ROTATE TETRIS PIECE
    #I  don't fully understand this, but I think I know what's going on.
    # It is changing the x and y values to turn into...
    # Actually, I think it is using graphing inverse functions logic, or something like that.
    # I only tried inverse functions on Khan Academy once, so I'm not sure if it is exactly like graphing inverse functions.
    # But I think that the y-values and x-values are swapped with each other to rotate the piece.
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
    line, lines = HEIGHT - 1, 0
    for row in range(HEIGHT -1, -1, -1):
        counter = 0
        for i in range(WIDTH):
            if field[row][i]:
                counter += 1
            field[line][i] = field[row][i]
        if counter < WIDTH:
            line -= 1
        else:
            animation_speed += 3
            lines += 1

    #DETERMINE SCORE
    score += scores[lines]


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

    #DRAWS WHAT NEXT TETRIS PIECE WILL BE
    for i in range(4):
        piece_rect.x = next_piece[i].x * TILE + 365
        piece_rect.y = next_piece[i].y * TILE + 180
        pygame.draw.rect(screen, next_color, piece_rect)


    # DRAW TITLES
    screen.blit(title_tetris, (450, 8))
    screen.blit(next_piece_title, (445, 120))
    screen.blit(title_score, (505, 680))
    screen.blit(font.render(str(score), True, pygame.Color('white')), (520, 730))
    screen.blit(title_record, (505, 600))
    screen.blit(font.render(record, True, pygame.Color('gold')), (550, 710))

    #game over
    for i in range(WIDTH):
        if field[0][i]:
            set_record(record, score)
            field = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
            animation_counter, animation_speed, animation_limit = 0, 60, 2000
        score = 0

        for i_rect in grid:
            pygame.draw.rect(game_screen, get_color(), i_rect)
            screen.blit(game_screen, (20, 20))
            pygame.display.flip()
            clock.tick(200)


    pygame.display.flip()
    clock.tick(FPS)
