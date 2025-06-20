import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)


ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Player1': 3,
    'Ring1': 2
}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME 1P',
               'EXIT',)

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL}

# S
SPAWN_TIME = 2000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
