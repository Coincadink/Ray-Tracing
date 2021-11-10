import math
from Hittable import Hittable


def hit_sphere(center, radius, r):
    oc = r.origin() - center
    a = r.direction().length_squared()
    half_b = oc.dot(r.direction())
    c = oc.length_squared() - radius * radius
    discriminant = half_b * half_b - a * c

    if discriminant < 0:
        return -1.0
    else:
        return (-half_b - math.sqrt(discriminant)) / a


class Sphere(Hittable):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def hit(self, r, t_min, t_max, rec):
        oc = r.origin() - self.center
        a = r.direction().length_squared()
        half_b = oc.dot(r.direction())
        c = oc.length_squared() - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False
        sqrtd = math.sqrt(discriminant)

        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center).div(self.radius)
        rec.set_face_normal(r, outward_normal)
        rec.material = self.material

        return True
