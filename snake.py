import pygame, random
from pygame.locals import *

def on_grid_random():
	x = random.randint(0, 590)
	y = random.randint(0, 590)
	return (x//10 * 10, y//10 * 10)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

initial_snake = [(200, 200), (210, 200), (220, 200)]
snake = list(initial_snake)
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255,255,255))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = on_grid_random()

my_direction = LEFT

clock = pygame.time.Clock()

def collision(point1, point2):
	return ((point1[0] == point2[0]) and (point1[1] == point2[1]))

while True:

	clock.tick(20)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
		if event.type == KEYDOWN:
			if event.key == K_UP and my_direction != DOWN:
				my_direction = UP
			if event.key == K_DOWN and my_direction != UP:
				my_direction = DOWN
			if event.key == K_LEFT and my_direction != RIGHT:
				my_direction = LEFT
			if event.key == K_RIGHT and my_direction != LEFT:
				my_direction = RIGHT	

	if (collision(snake[0], apple_pos)):
		apple_pos = on_grid_random()
		snake.append((0,0))


	for i in range(len(snake) - 1, 0, -1):
		snake[i] = (snake[i-1][0], snake[i-1][1])


	
	if my_direction == UP:
		snake[0] = (snake[0][0], (snake[0][1] - 10) % 600)
	if my_direction == DOWN:
		snake[0] = (snake[0][0], (snake[0][1] + 10) % 600)
	if my_direction == LEFT:
		snake[0] = ((snake[0][0] - 10) % 600, snake[0][1])
	if my_direction == RIGHT:
		snake[0] = ((snake[0][0] + 10) % 600, snake[0][1])


	screen.fill((0,0,0))
	screen.blit(apple, apple_pos)
	for pos in snake:
		screen.blit(snake_skin, pos)

	pygame.display.update()
