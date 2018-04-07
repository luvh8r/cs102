import pygame
from pygame.locals import *
import random
from pprint import pprint as pp
import copy
from copy import deepcopy


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed


    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('RIJID COPMANY')
        self.screen.fill(pygame.Color('white'))
        running = True
        self.clist = self.cell_list(randomize=True)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_cell_list(self.clist)
            self.update_cell_list(self.clist)
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True):
        """ Создание списка клеток.
        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        clist = [[0 for i in range(self.cell_width)] for j in range(self.cell_height)]
        if randomize:
            clist = [[random.randint(0, 1) for i in range(self.cell_width)] for j in range(self.cell_height)]
        self.clist = clist
        return self.clist

    def draw_cell_list(self, rects):
        for i in range(len(rects)):
            for j in range(len(rects[i])):
                if rects[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('White'),
                                     (self.cell_size * j, self.cell_size * i, self.cell_size, self.cell_size))
                elif rects[i][j] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('Grey'),
                                     (self.cell_size * j, self.cell_size * i, self.cell_size, self.cell_size))


    def get_neighbours(self, cell):
        """ Вернуть список соседей для указанной ячейки
        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        x, y = cell
        n = self.cell_height - 1
        m = self.cell_width - 1
        neighbours = [self.clist[i][j] for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if
                      (0 <= i <= n) and (0 <= j <= m) and (i != x or j != y)]
        return neighbours

    def update_cell_list(self, cell_list):
        """ Выполнить один шаг игры.
        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.
        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = []
        new_list = deepcopy(cell_list)
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if cell_list[i][j]:
                    if sum(self.get_neighbours((i, j))) in (2, 3):
                        new_list[i][j] = 1
                    else:
                        new_list[i][j] = 0
                else:
                    if sum(self.get_neighbours((i, j))) == 3:
                        new_list[i][j] = 1
                    else:
                        new_list[i][j] = 0
        self.clist = new_list
        return new_list


if __name__ == '__main__':
    game = GameOfLife(1980, 800, 10)
    game.run()