import math

#game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
HALF_HEIGHT = HEIGHT // 2

# No FPS cap, since framerate does not affect player speed ()
FPS = 0

# Player settings
PLAYER_POS = 1.5, 5 #mini map
PLAYER_ANGLE  = 0
PLAYER_SPEED = 0.004
PLAYER_ROTATION_SPEED = 0.002

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH// 2
HALF_NUM_RAYS = NUM_RAYS//2
DELTA_ANGLE = FOV/NUM_RAYS
MAX_DEPTH = 20

SCREEN_DISTANCE = HALF_WIDTH / math.tan(HALF_FOV)

# Since the number of rays is less than the screen resolution in width, scaling is used to maintain better performance
SCALE =  WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
