import pygame
import constants
from game import Game
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption(constants.TITLE)

game = Game("menu")
clock = pygame.time.Clock()

while True:
	game.update_screen()
	game.check_events()
	game.run_logic()
	game.update_timer()
	clock.tick(constants.FPS)