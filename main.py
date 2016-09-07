import pygame, easygui, sys
import constants
from game import Game
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption(constants.TITLE)
try:
	icon = pygame.image.load("resources/tank1.png")
	icon = pygame.transform.scale2x(icon)
	pygame.display.set_icon(icon)
except pygame.error:
	easygui.msgbox("tank1.png does not exist")
	pygame.quit()
	sys.exit()

game = Game("menu")
clock = pygame.time.Clock()

while True:
	game.update_screen()
	game.check_events()
	game.run_logic()
	game.update_timer()
	clock.tick(constants.FPS)