#!/usr/bin/python3
"""
Island Perimeter:
    returns to the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """island perimenter function"""
    perimeter = 0
    for c in range(len(grid)):
        for j in range(len(grid[c])):
            if grid[c][j] == 1:
                perimeter += 4
                if c > 0 and grid[c-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[c][j-1] == 1:
                    perimeter -= 2
    return perimeter
