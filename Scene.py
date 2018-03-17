import pygame
from Utils import *
from Cursor import *
from Character import *
from Menu import *
#GLOBAL
TITLE_OPTIONS = {"TITLE_NEW" : 0, "TITLE_CONTINUE" : 1, "TITLE_EXIT" : 2}
class SceneBase:
	def __init__(self):
		self.next = self
	def processInput(self, events):
		print("ProcessInput, you didn't override this in the child class")
	def update(self):
		print("Update, you didn't override this in the child class")
	def render(self, screen):
		print("Render, you didn't override this in the child class")
	def switchToScene(self, next_scene):
		self.next = next_scene
	def terminate(self):
		self.switchToScene(None)
class TitleScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.menu = ScreenMenu()
	def processInput(self, events, pressed_keys):
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if self.menu.option == TITLE_OPTIONS["TITLE_NEW"]:
						self.switchToScene(WorldScene())
					elif self.menu.option == TITLE_OPTIONS["TITLE_CONTINUE"]:
						self.switchToScene(BattleScene())
					elif self.menu.option == TITLE_OPTIONS["TITLE_EXIT"]:
						self.terminate()
				elif event.key == pygame.K_UP:
					if self.menu.option == 0:
						self.menu.option = self.menu.num_options-1
					else:
						self.menu.option = self.menu.option-1
				elif event.key == pygame.K_DOWN:
					self.menu.option = (self.menu.option+1)%self.menu.num_options
	def update(self):
		self.menu.update()
	def render(self, screen):
		self.menu.render(screen)
class WorldScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.character = Character()
	def processInput(self, events, pressed_keys):
		for event in events:
			if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.switchToScene(TitleScene())
		self.character.move(pygame.key.get_pressed())
	def update(self):
		pass
	def render(self, screen):
		screen.fill((0, 0, 0))
		self.character.update()
		self.character.render(screen)
class BattleScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.characters = []
		self.characters.append(Character())
		self.characters.append(Character())
		self.characters.append(Character())
		self.enemies = []
		self.enemies.append(Character())
		self.enemies.append(Character())
		self.enemies.append(Character())
		self.enemies.append(Character())
		self.menu = BattleMenu(self.characters, self.enemies)
	def processInput(self, events, pressed_keys):
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.switchToScene(TitleScene())
				if event.key == pygame.K_DOWN:
					self.menu.changeOption(1)
				if event.key == pygame.K_UP:
					self.menu.changeOption(-1)
	def enemies(self, enemies):
		self.enemies = enemies
	def update(self):
		pass
	def render(self, screen):
		screen.fill((0, 0, 0))
		numCharacters = len(self.characters)
		# We place the characters in the screen
		for index, character in enumerate(self.characters):
			posY = calculatePositionInList(startingPos = BATTLE_HEIGHT_SCREEN_OFFSET, endingPos = HEIGHT - BATTLE_HEIGHT_SCREEN_OFFSET, numberOfElements = numCharacters, element = index)
			character.setPos(WIDTH - BATTLE_HEIGHT_SCREEN_OFFSET, posY)
			character.update()
			character.render(screen)
		# We place the enemies in the screen
		for index, enemy in enumerate(self.enemies):
			posY = calculatePositionInList(startingPos = BATTLE_HEIGHT_SCREEN_OFFSET, endingPos = HEIGHT - BATTLE_HEIGHT_SCREEN_OFFSET, numberOfElements = numCharacters, element = index)
			enemy.setPos(BATTLE_HEIGHT_SCREEN_OFFSET, posY)
			enemy.update()
			enemy.render(screen)
		self.menu.render(screen)