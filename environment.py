#!/usr/bin/env python3
import random


class Cell:
    def __init__(self, tree=False):
        """Initialise a cell, which is one grid space in an envionment.

        Args:
            tree (bool, optional): A tree object. Defaults to False.
        """

        self.tree = tree
        pass


class Environment:
    def __init__(self, width=32, height=8, species_of_seed=9):
        """Initialise an environment, based on size and species of seed.

        Args:
            width (int, optional): Horizontal size of environment. Defaults to 32.
            height (int, optional): Vertical size of environment. Defaults to 8.
            species_of_seed (int, optional): Number of species of seed. Defaults to 9.
        """
        self.width = width
        self.height = height
        self.species_of_seed = species_of_seed

        self.grid = self.generate(self.width, self.height)

    def generate(self, width=32, height=8):
        """Main function for generating a grid of cell objects.

        Args:
            width (int): Number of horizontal cells in a row (i.e. width).
            height (int): Number of rows of cells (i.e. height).

        Returns:
            [type]: [description]
        """
        # Initialise an empty grid.
        grid = []
        for y in range(self.height):
            # Initialise an empty row.
            row = []
            # Fill the row with cells, with a 5% of a tree.
            for x in range(self.width):
                cell = Cell(tree=False)
                if random.random() < 0.05:
                    cell.tree = True
                row.append(cell)
            # Add the row to the grid.
            grid.append(row)
        return grid

    def display(self):
        """Print a human-readable version of the grid."""
        for y in range(self.height):
            print("|", end="")
            for x in range(self.width):
                if self.grid[y][x].tree:
                    print("T", end="")
                else:
                    print(" ", end="")
                print("|", end="")
            print()


if __name__ == "__main__":
    environment = Environment()
    environment.display()
