import pygame
import constants
pygame.init()

class Wall:
	def __init__(self, x, y):
		self.image = pygame.Surface([32, 32])
		#self.image.fill(constants.WHITE)
		image = pygame.image.load("resources/tiles.png")
		self.image.blit(image, (0, 0), (128, 96, 32, 32))
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y