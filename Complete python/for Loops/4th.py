import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area, circumference

a, c = circle_stats(5)

print("Area: {:.2f}, Circumference: {:.2f}".format(a, c))