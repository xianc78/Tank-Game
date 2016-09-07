import pygame, sys
import constants, tank
from wall import Wall

class Map:
	def __init__(self, file):
		self.file = open(file, "r")
		data = self.file.read()
		self.layout = data.split("\n")
		self.create_map()
		
	def create_map(self):
		self.wall_list = []
		self.bullet_list = []
		self.explosion_list = []
		self.mine_list = []
		x = y = 0
		for row in self.layout:
			for tile in row:
				if tile == "w":
					self.wall_list.append(Wall(x, y))
				elif tile == "1":
					self.tank1 = tank.Tank1(x, y, self)
				elif tile == "2":
					self.tank2 = tank.Tank2(x, y, self)
				elif tile == ".":
					pass
				else:
					print tile + " is not a valid tile."
					raw_input("<press enter>")
					pygame.quit()
					sys.exit()
				x += constants.TILE_SIZE[0]
			x = 0
			y += constants.TILE_SIZE[1]