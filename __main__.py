import sys

import pygame

# Window size
from key import Key
from matrix import Matrix
from snake import Snake


def initialize_matrix(size_x, size_y):
    return Matrix(size_x=size_x, size_y=size_y)


def initialize_pygame(matrix: Matrix, size_per_pixel: int):
    # Checks for errors encountered
    check_errors = pygame.init()
    # pygame.init() example output -> (6, 0)
    # second number in tuple gives number of errors
    if check_errors[1] > 0:
        print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
        sys.exit(-1)
    else:
        print('[+] Game successfully initialised')
    pygame.display.set_caption("Game")
    return pygame.display.set_mode((matrix.size_x * size_per_pixel, matrix.size_y * size_per_pixel))


def update_screen(screen: pygame.Surface, matrix: Matrix, size_per_pixel: int):
    """
    Updates the screen with the current state of the matrix.

    :param screen: The screen to update
    :param matrix: The matrix to update the screen with
    :param size_per_pixel: The size of each pixel
    :return:
    """
    for row in range(matrix.size_y):
        for column in range(matrix.size_x):
            color = matrix.get_pixel(column, row)
            pygame.draw.rect(screen, color.value,
                             (column * size_per_pixel, row * size_per_pixel, size_per_pixel, size_per_pixel))

    pygame.display.update()


def main():
    matrix = initialize_matrix(30, 30)
    size_per_pixel = 20
    screen = initialize_pygame(matrix, size_per_pixel)

    # Game loop
    game = Snake(matrix)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.on_key_press(Key.ARROW_UP)
                elif event.key == pygame.K_DOWN:
                    game.on_key_press(Key.ARROW_DOWN)
                elif event.key == pygame.K_LEFT:
                    game.on_key_press(Key.ARROW_LEFT)
                elif event.key == pygame.K_RIGHT:
                    game.on_key_press(Key.ARROW_RIGHT)

        if not game.game_over:
            game.update_matrix(matrix)
        update_screen(screen, matrix, size_per_pixel)
        # Delay game loop
        wait = pygame.time.wait(80)


if __name__ == '__main__':
    print('Hello World!')
    main()
