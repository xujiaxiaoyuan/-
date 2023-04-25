import pygame
from random import randint

# 初始化pygame
pygame.init()

# 设定窗口大小和标题
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# 方块大小以及其他相关参数设定
BLOCK_SIZE = 30
COLUMN = 10
ROW = 20
TOP_LEFT_X = (WIDTH - COLUMN * BLOCK_SIZE) // 2
TOP_LEFT_Y = HEIGHT - ROW * BLOCK_SIZE

# 定义方块类
class Block(object):
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
        self.rotation = 0

# 定义七种不同的方块形状
S_BLOCK = [ 
    ['.....',
     '.....',
     '..00.',
     '.00..',
     '.....'],
    
    ['.....',
     '..0..',
     '..00.',
     '...0.',
     '.....']
]

Z_BLOCK = [
    ['.....',
     '.....',
     '.00..',
     '..00.',
     '.....'],
    
    ['.....',
     '..0..',
     '.00..',
     '.0...',
     '.....']
]

I_BLOCK = [
    ['..0..',
     '..0..',
     '..0..',
     '..0..',
     '.....'],
    
    ['.....',
     '0000.',
     '.....',
     '.....',
     '.....']
]

O_BLOCK = [
    ['.....',
     '.....',
     '.00..',
     '.00..',
     '.....']
]

J_BLOCK = [
    ['.....',
     '.0...',
     '.000.',
     '.....',
     '.....'],
    
    ['.....',
     '..00.',
     '..0..',
     '..0..',
     '.....'],
        
    ['.....',
     '.....',
     '.000.',
     '...0.',
     '.....'],
    
    ['.....',
     '..0..',
     '..0..',
     '.00..',
     '.....']
]

L_BLOCK = [
    ['.....',
     '...0.',
     '.000.',
     '.....',
     '.....'],
    
    ['.....',
     '..0..',