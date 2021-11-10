#!/usr/downloads/pypy/bin/pypy

import math


def clamp(x, cmin, cmax):
    return max(min(x, cmax), cmin)


def write_color(f, color, samples_per_pixel):
    r = color[0]
    g = color[1]
    b = color[2]

    scale = 1.0 / samples_per_pixel
    r = math.sqrt(scale * r)
    g = math.sqrt(scale * g)
    b = math.sqrt(scale * b)

    f.write(
        str(int(256 * clamp(r, 0.0, 0.999))) + " " +
        str(int(256 * clamp(g, 0.0, 0.999))) + " " +
        str(int(256 * clamp(b, 0.0, 0.999))) + "\n"
    )


class Color:
    def __init__(self, e0, e1, e2):
        self.e = [e0, e1, e2]

    def __str__(self):
        return str(self.e[0]) + " " + str(self.e[1]) + " " + str(self.e[2])

    def __getitem__(self, item):
        return self.e[item]

    def r(self):
        return self.e[0]

    def g(self):
        return self.e[1]

    def b(self):
        return self.e[2]

    def __add__(self, other):
        return Color(
            self.e[0] + other.e[0],
            self.e[1] + other.e[1],
            self.e[2] + other.e[2]
        )

    def __mul__(self, other):
        return Color(
            self.e[0] * other.e[0],
            self.e[1] * other.e[1],
            self.e[2] * other.e[2]

        )

    def mul(self, other):
        return Color(
            self.e[0] * other,
            self.e[1] * other,
            self.e[2] * other
        )

