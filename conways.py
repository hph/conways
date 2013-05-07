#!/usr/bin/env python

from argparse import ArgumentParser
from os import system
from random import random
from sys import version_info
from time import sleep, time


if version_info.major == 2:
    range = xrange


class Colony(object):
    def __init__(self, args):
        self.width = args.width
        self.height = args.height
        self.fps = args.fps
        self.no_clear = args.no_clear
        self.index = 0
        self.thrives = True
        self.colony = [[1 if random() < args.chance else 0
                        for _ in range(self.width)]
                       for _ in range(self.height)]

    def __str__(self):
        if not self.no_clear:
            system('clear')
        lines = [' '.join(['O' if cell else ' ' for cell in cell_row])
                 for cell_row in self.colony]
        return '\n'.join(['Generation {0}\n'.format(self.index)] + lines)

    def neighbors(self, coord):
        """Return the number of cells in the Moore neighborhood of the cell at
        the specified coordinate."""
        moore_coords = [(coord[0] + y, coord[1] + x) for x in range(-1, 2)
                        for y in range(-1, 2) if not y == x == 0]
        return sum([self.colony[y][x] for y, x in moore_coords
                    if all([y >= 0, x >= 0, y < self.height, x < self.width])])

    def generate(self):
        """Apply the four rules of Conway's Game of Life to the colony."""
        self.index += 1
        new_colony = [[0 for _ in range(self.width)] for row in self.colony]
        neighs = [[self.neighbors((x, y)) for y, _ in enumerate(row)]
                  for x, row in enumerate(self.colony)]
        for y, row in enumerate(new_colony):
            for x, _ in enumerate(row):
                cell, neigh = self.colony[y][x], neighs[y][x]
                if cell and neigh == 2 or neigh == 3:
                    new_colony[y][x] = 1
        if new_colony == self.colony:
            self.thrives = False
        self.colony = new_colony

    def run(self):
        """Run Conway's Game of Life and show the colony in each generation."""
        while self.thrives:
            call_time = time()
            print(self)
            self.generate()
            delta_time = time() - call_time
            try:
                sleep(1.0 / self.fps - delta_time)
            except IOError:
                pass


def _process_args():
    parser = ArgumentParser(prog='conway',
                            description="""Visualize Conway's Game of Life with
                                           a command-line interface.""")
    parser.add_argument('--width', type=int, default=40,
                        help="""Number of columns in the grid. The default is
                                40.""")
    parser.add_argument('--height', type=int, default=21,
                        help="""Number of rows in the grid. The default is
                                21.""")
    parser.add_argument('--chance', type=float, default=0.5,
                        help="""Denotes the chance for a living cell in each
                                grid coordinate. The default is 0.5.""")
    parser.add_argument('--fps', type=float, default=4.0,
                        help="""The number of generations per second. The
                                default is 4.0.""")
    parser.add_argument('--no-clear', action='store_true',
                        help="""Do not clear previous generations.""")
    return parser.parse_args()


def main():
    args = _process_args()
    colony = Colony(args)
    try:
        colony.run()
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    main()
