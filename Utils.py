import sys, pygame
from pygame.locals import *
from enum import Enum
############################################
################# NUMBERS ##################
############################################
N_FPS = 60
############################################
################## SIZES ###################
############################################
################## SCREEN
WIDTH = 640
HEIGHT = 480
WIDTH_HALF = WIDTH/2
HEIGHT_HALF = HEIGHT/2
################## TEXTS
TEXT_SM = 16
TEXT_MD = 24
TEXT_LG = 42
TEXT_XLG = 64
################## BATTLE
BATTLE_WIDTH_SCREEN_OFFSET = WIDTH/10
BATTLE_HEIGHT_SCREEN_OFFSET = WIDTH/10
################## MENU
# INITIAL SCREEN
MENU_OFFSET = HEIGHT/8
# BATTLE_SCREEN
MENU_BATTLE_SCREEN_WIDTH = WIDTH
MENU_BATTLE_SCREEN_HEIGHT = 200
MENU_BATTLE_SCREEN_X = 0
MENU_BATTLE_SCREEN_Y = HEIGHT - MENU_BATTLE_SCREEN_HEIGHT
MENU_BATTLE_COLOUR = (85,0,85,128)
MENU_BATTLE_OFFSET_WIDTH = 20
MENU_BATTLE_OFFSET_HEIGHT = 20
# CURSOR
CURSOR_OFFSET = 20
CURSOR_SIZE = (64,64)
CURSOR_BATTLE_SIZE = (48,48)
################## SPRITESHEET
CHARACTER_SPRITESHEET_SIZE = (640,256)
CHARACTER_SPRITESHEET_UNIT = (24, 30)
############################################
################# COLOURS ##################
############################################
C_WHITE = (255,255,255)
C_BLACK = (0, 0, 0)
C_PURPLE = (80,20,80)
C_AQUAMARINE = (0, 85, 85)
############################################
############### ASSETS PATH ################
############################################
P_ASSETS = "assets/"
############################################
################## ICONS ###################
############################################
P_ICONS = P_ASSETS + "/icons/"
I_ICON = P_ICONS + "marioicon.png"
############################################
############### BACKGROUNDS ################
############################################
P_BACKGROUNDS = P_ASSETS + "backgrounds"
############################################
################# SPRITES ##################
############################################
P_SPRITES = P_ASSETS + "sprites/"
S_CURSOR = P_SPRITES + "cursor.png"
S_CHARACTER = P_SPRITES + "character.png"
############################################
################## FONTS ###################
############################################
P_FONT = P_ASSETS + "fonts/"
F_DROID_SANS = P_FONT + "DroidSans.ttf"
F_ARCADE_CLASSIC = P_FONT + "arcadeclassic.ttf"
F_SWORD_OF_MANA = P_FONT + "manaspc.ttf"
F_FINAL_FANTASY = P_FONT + "finalf.ttf"

class TextPosition(Enum):
	right = 0
	left = 1
	centered = 2

def sign(number):
	if number < 0:
		return -1
	return 1
def load_image(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except pygame.error:
		raise pygame.error
	if transparent:
		image = image.convert_alpha()
		image.set_colorkey((0,0,0,0), pygame.RLEACCEL)
	else:
		image = image.convert()
	return image
def writeText(text, posx, posy, colour=(255, 255, 255), size = 25, position = TextPosition.left, font = F_DROID_SANS):
	font = pygame.font.Font(font, size)
	output = pygame.font.Font.render(font, text, 1, colour)
	output_rect = output.get_rect()
	if position == TextPosition.left:
		output_rect.left = posx
	elif position == TextPosition.centered:
		output_rect.centerx = posx
	elif position == TextPosition.right:
		output_rect.right = posx
	output_rect.top = posy
	return output, output_rect
def calculatePositionInList(startingPos, endingPos, numberOfElements, element):
	return ((endingPos-startingPos)/numberOfElements)*element + startingPos