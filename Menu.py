import pygame
from pygame.locals import *
from Cursor import *
class Menu:
	def __init__(self, posx, posy, width, height, cursor_size, background_colour = (255,255,255), buttons = [], text_size = 25):
		self.posx = posx
		self.posy = posy
		self.buttons = buttons
		self.background = pygame.Surface((width, height), pygame.SRCALPHA)
		self.background.fill(background_colour)
		self.option = 0
		self.num_options = 0
		self.text_size = text_size
		self.cursor = Cursor(size = cursor_size)
	#We need to pass the set of buttons just in case you added a new set for submenues
	def update(self, buttons = None):
		if buttons == None:
			buttons = self.buttons
		(surf,rect) = buttons[self.option]
		self.cursor.update(rect)
	def render(self, screen, buttons = None):
		if buttons == None:
			buttons = self.buttons
		self.update()
		screen.blit(self.background, (self.posx,self.posy))
		for (buttonSurf, buttonRect) in buttons:
			screen.blit(buttonSurf, buttonRect)
		self.cursor.render(screen)
	def changeOption(self, offset):
		self.option = (self.option + offset)%len(self.buttons)
		if self.option < 0:
			self.option = len(self.buttons)
	def getOption(self):
		return self.option
	def setOption(self, option):
		self.option = option
	def getTextSize(self):
		return self.text_size
	def appendButton(self, button):
		self.buttons.append(button)
		self.num_options += 1
	def getNumOptions(self):
		return self.num_options
class ScreenMenu(Menu):
	def __init__(self):
		Menu.__init__(self, posx = 0, posy = 0, width = WIDTH, height = HEIGHT, cursor_size = CURSOR_SIZE, background_colour = C_PURPLE, text_size = TEXT_LG)
		self.appendButton(writeText("New", posx = WIDTH_HALF, posy = HEIGHT_HALF-MENU_OFFSET, colour = C_WHITE, size = self.getTextSize(), position = TextPosition.centered, font = F_SWORD_OF_MANA))
		self.appendButton(writeText("Continue", posx = WIDTH_HALF, posy = HEIGHT_HALF, colour = C_WHITE, size = self.getTextSize(), position = TextPosition.centered, font = F_SWORD_OF_MANA))
		self.appendButton(writeText("Exit", posx = WIDTH_HALF, posy = HEIGHT_HALF + MENU_OFFSET, colour = C_WHITE, size = self.getTextSize(), position = TextPosition.centered, font = F_SWORD_OF_MANA))
class BattleMenu(Menu):
	def __init__(self, players, enemies, turn = 0):
		Menu.__init__(self, posx = MENU_BATTLE_SCREEN_X, posy = MENU_BATTLE_SCREEN_Y, width = MENU_BATTLE_SCREEN_WIDTH, height = MENU_BATTLE_SCREEN_HEIGHT, cursor_size = CURSOR_BATTLE_SIZE, background_colour = C_AQUAMARINE, buttons = [], text_size = 25)
		self.players = players
		self.enemies = enemies
		self.turn = turn
		self.appendButton(writeText("Atack", posx = WIDTH - MENU_BATTLE_SCREEN_X - MENU_BATTLE_OFFSET_WIDTH, posy = MENU_BATTLE_SCREEN_Y + MENU_BATTLE_OFFSET_HEIGHT, colour = C_WHITE, size = self.getTextSize(), position = TextPosition.right, font = F_ARCADE_CLASSIC))
		self.appendButton(writeText("Skills", posx = WIDTH - MENU_BATTLE_SCREEN_X - MENU_BATTLE_OFFSET_WIDTH, posy = MENU_BATTLE_SCREEN_Y + 2 * MENU_BATTLE_OFFSET_HEIGHT, colour = C_WHITE, size = self.getTextSize(), position = TextPosition.right, font = F_ARCADE_CLASSIC))
		self.appendButton(writeText("Items", posx = WIDTH - MENU_BATTLE_SCREEN_X - MENU_BATTLE_OFFSET_WIDTH, posy = MENU_BATTLE_SCREEN_Y + 3 * MENU_BATTLE_OFFSET_HEIGHT, colour = C_WHITE, size = self.getTextSize(), position = TextPosition.right, font = F_ARCADE_CLASSIC))