import pygame
import constants

class Mine:
	def __init__(self, x, y, tank):
		self.image = pygame.Surface(constants.TILE_SIZE)
		self.image.fill(constants.BLUE)
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.tank = tank
		self.map = self.tank.map