import pygame
import random

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
BRICK_WIDTH = 50
BRICK_HEIGHT = 20
BRICK_GAP = 2
ROWS = 5
COLS = 12
FPS = 60
SPEED_INC = 1.05
BRICK_COLORS = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Global variables
paddle = pygame.Rect((WINDOW_WIDTH - PADDLE_WIDTH) // 2, WINDOW_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_RADIUS, WINDOW_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx = 5
ball_dy = -5
bricks = [[None] * COLS for _ in range(ROWS)]
score = 0
level = 1
game_over = False

# Initialize pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Atari Breakout')
clock = pygame.time.Clock()

# Create the bricks
def create_bricks():
    global bricks, level
    brick_width_with_gap = BRICK_WIDTH + BRICK_GAP
    brick_height_with_gap = BRICK_HEIGHT + BRICK_GAP
    top_gap = 50
    left_gap = (WINDOW_WIDTH - (BRICK_WIDTH * COLS + BRICK_GAP * (COLS - 1))) // 2
    for i in range(ROWS):
        for j in range(COLS):
            x = left_gap + j * brick_width_with_gap
            y = top_gap + i * brick_height_with_gap
            bricks[i][j] = {'rect': pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT), 'color': BRICK_COLORS[i]}
    level += 1

# Check if the ball hits the paddle
def check_paddle_collision():
    global ball_dx, ball_dy
    if ball.colliderect(paddle):
        ball_dy = -abs(ball_dy)
        offset = ball.x - paddle.x
        if offset < PADDLE_WIDTH // 3:
            ball_dx = -abs(ball_dx)
        elif offset > PADDLE_WIDTH * 2 // 3:
            ball_dx = abs(ball_dx)
        else:
            ball_dx = 0

# Check if the ball hits a brick
def check_brick_collision():
    global ball_dx, ball_dy, score
    for i in range(ROWS):
        for j in range(COLS):
            brick = bricks[i][j]
            if brick is not None and ball.colliderect(brick['rect']):
                ball_dy = abs(ball_dy)
                bricks[i][j] = None
                score += 1
                if score == ROWS * COLS:
                    global game_over
                    game_over = True
                if ball_dx > 0:
                    if ball.centerx < brick['rect'].left:
                        ball_dx = -ball_dx
                    else:
                        ball_dy = -ball_dy
                        ball_dx = -ball_dx
                else:
                    if ball.centerx > brick['rect'].right:
                        ball_dx = -ball_dx
                    else:
                        ball_dy = -ball_dy
                        ball_dx = -ball_dx

# Move the ball
def move_ball():
    global ball_dx, ball_dy
    ball.move_ip(ball_dx, ball_dy)
    if ball.left < 0:
        ball.left = 0
        ball_dx = abs(ball_dx)
    elif ball.right > WINDOW_WIDTH:
        ball.right = WINDOW_WIDTH
        ball_dx = -abs(ball_dx)
    if ball.top < 0:
        ball.top = 0
        ball_dy = abs(ball_dy)

# Move the paddle
def move_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)
    elif keys[pygame.K_RIGHT] and paddle.right < WINDOW_WIDTH:
        paddle.move_ip(5, 0)

# Draw the bricks
def draw_bricks():
    for i in range(ROWS):
        for j in range(COLS):
            brick = bricks[i][j]
            if brick is not None:
                pygame.draw.rect(window, brick['color'], brick['rect'])

# Draw the paddle and the ball
def draw_paddle_and_ball():
    pygame.draw.rect(window, WHITE, paddle)
    pygame.draw.circle(window, WHITE, ball.center, BALL_RADIUS)

# Draw the score and the level
def draw_score_and_level():
    font = pygame.font.Font(None, 30)
    score_text = font.render(f'Score: {score}', True, WHITE)
    level_text = font.render(f'Level: {level}', True, WHITE)
    window.blit(score_text, (10, 10))
    window.blit(level_text, (WINDOW_WIDTH - level_text.get_width() - 10, 10))

# Draw the game over message
def draw_game_over():
    font = pygame.font.Font(None, 50)
    text = font.render('Game Over', True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(text, text_rect)

# Main loop
create_bricks()

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the game state
    if not game_over:
        check_paddle_collision()
        check_brick_collision()
        move_ball()
        move_paddle()
        if ball.bottom > WINDOW_HEIGHT:
            game_over = True
        if score == ROWS * COLS:
            create_bricks()
            ball.center = (WINDOW_WIDTH // 2 - BALL_RADIUS, WINDOW_HEIGHT // 2 - BALL_RADIUS)
            ball_dx = 5
            ball_dy = -5
            score = 0
            level += 1
            PADDLE_WIDTH = int(PADDLE_WIDTH * SPEED_INC)
            paddle.width = PADDLE_WIDTH
    else:
        draw_game_over()

    # Draw the screen
    window.fill(BLACK)
    draw_bricks()
    draw_paddle_and_ball()
    draw_score_and_level()
    pygame.display.update()
    clock.tick(FPS)

                    
