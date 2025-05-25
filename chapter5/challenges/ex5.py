# 5: Estimating the Area of a Circle

import random
import math

def estimate_area(radius: float, total_points: int):
    center = (radius, radius)
    hit_circle = 0

    for i in range(total_points):
        # Generate the (x, y) coordinates of
        # point p, where the dart hits the board
        x = random.uniform(0, 2*radius)
        y = random.uniform(0, 2*radius)
        p = (x, y)

        # distance of the dart coordinate from circle's center
        d = math.sqrt((p[0]-center[0])**2 + (p[1]-center[1])**2)
        if d <= radius:
            hit_circle += 1

    area_of_square = (2*radius)**2
    f = (hit_circle/total_points)*area_of_square

    return f * area_of_circle

if __name__ == '__main__':
    radius = float(input('Radius: '))
    area_of_circle = math.pi*radius**2
    print('Radius: {0}'.format(radius))

    for trial in [1000, 10000, 100000]:
        estimated = estimate_area(radius, trial)
        print('Area: {0}  Estimated ({1} darts): {2}'.format(area_of_circle, trial, estimated))