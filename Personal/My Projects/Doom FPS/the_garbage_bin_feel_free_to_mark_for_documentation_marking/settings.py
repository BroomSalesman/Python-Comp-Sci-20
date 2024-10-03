import math

#game settings (don't mess with these, they're not the type of settings you can change (well, change safely))
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

# No FPS cap, since framerate does not affect player speed ()
FPS = 0

# Player settings
PLAYER_POSITION = 1.5, 5 #mini map
PLAYER_ANGLE  = 0
PLAYER_SPEED = 0.004
PLAYER_ROTATION_SPEED = 0.002
PLAYER_SIZE_SCALE = 60

#Mouse settings
MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_RELATIVITY = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

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