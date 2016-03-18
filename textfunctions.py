import pygame, easygui, sys
import constants
pygame.init()

try:
	centerFontObj = pygame.font.Font("resources/font.ttf", 32)
except pygame.error:
	easygui.msgbox("font.ttf doesn't exist.")
	pygame.quit()
	sys.exit()
	
fontObj = pygame.font.Font("resources/font.ttf", 16)


class centerText:
	def __init__(self, text):
		self.text = centerFontObj.render(text, True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
		
	def __str__(self):
		return self.text
		
class ScoreText:
	def __init__(self):
		self.text = fontObj.render("", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		
	def update(self, score1, score2, time):
		self.text = fontObj.render("Tank 1 Score: " + str(score1) + " | Tank 2 Score: " + str(score2) + " | Time: " + str(time), True, constants.WHITE, constants.BLACK)