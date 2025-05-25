"""
Example of using matplotlib's Circle patch
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle


def create_circle() -> Circle:
    circle = patches.Circle((0, 0), radius=0.5, fc="w", ec="r")
    return circle


def show_shape(patch: Circle):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis("scaled")
    plt.show()


if __name__ == "__main__":
    c = create_circle()
    show_shape(c)

