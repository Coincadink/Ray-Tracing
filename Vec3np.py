import numpy


def random_vec():
    a = random() * (-1 if random() < .5 else 1)
    b = random() * (-1 if random() < .5 else 1)
    c = random() * (-1 if random() < .5 else 1)
    return Vec3(a, b, c)


def random_unit_vector():
    return random_in_unit_sphere().unit_vector()


def random_in_unit_sphere():
    while True:
        p = random_vec()
        if p.length_squared() >= 1:
            continue
        return p


def random_in_hemisphere(normal):
    in_unit_sphere = random_in_unit_sphere()
    if in_unit_sphere.dot(normal) > 0:
        return in_unit_sphere
    else:
        return -in_unit_sphere


def reflect(v, n):
    return v - n.mul(v.dot(n)).mul(2)


def refract(uv, n, etai_over_etat):
    cos_theta = min(-uv.dot(n), 1.0)
    r_out_perp = etai_over_etat * (uv + n.mul(cos_theta))
    r_out_parallel = -math.sqrt(math.fabs(1.0 - r_out_perp.length_squared())) * n
    return r_out_perp + r_out_parallel


class Vec3:
    def __init__(self, e0, e1, e2):
        self.e = [e0, e1, e2]

    def __str__(self):
        return str(self.e[0]) + " " + str(self.e[1]) + " " + str(self.e[2])

    def __getitem__(self, item):
        return self.e[item]

    def x(self):
        return self.e[0]

    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __add__(self, other):
        return Vec3(
            self.e[0] + other.e[0],
            self.e[1] + other.e[1],
            self.e[2] + other.e[2]
        )

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return Vec3(
            self.e[0] * other.e[0],
            self.e[1] * other.e[1],
            self.e[2] * other.e[2]
        )

    def mul(self, other):
        return Vec3(
            self.e[0] * other,
            self.e[1] * other,
            self.e[2] * other
        )

    def __truediv__(self, other):
        return Vec3(
            self.e[0] / other.e[0],
            self.e[1] / other.e[1],
            self.e[2] / other.e[2]
        )

    def div(self, other):
        return self.mul(1 / other)

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    def dot(self, other):
        return self.e[0] * other.e[0] + self.e[1] * other.e[1] + self.e[2] * other.e[2]

    def cross(self, other):
        return Vec3(
            self.e[1] * other.e[2] - self.e[2] * other.e[1],
            self.e[2] * other.e[0] - self.e[0] * other.e[2],
            self.e[0] * other.e[1] - self.e[1] * other.e[0]
        )

    def unit_vector(self):
        return self.div(self.length())

    def near_zero(self):
        s = 1e-8
        return math.fabs(self.e[0]) < s and math.fabs(self.e[1]) < s and math.fabs(self.e[2]) < s
