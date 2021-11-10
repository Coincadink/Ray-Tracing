from Vec3 import random_unit_vector, reflect, random_in_unit_sphere
from Ray import Ray


class Material:
    def scatter(self, r_in, rec, scattered):
        pass


class Lambertian(Material):
    def __init__(self, a):
        self.albedo = a

    def scatter(self, r_in, rec):
        scatter_direction = rec.normal + random_unit_vector()

        # Catch degenerate scatter direction
        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered = Ray(rec.p, scatter_direction)
        return True, self.albedo, scattered


class Metal(Material):
    def __init__(self, a, f):
        self.albedo = a
        self.fuzz = f

    def scatter(self, r_in, rec):
        reflected = reflect(r_in.direction().unit_vector(), rec.normal)
        scattered = Ray(rec.p, reflected + random_in_unit_sphere().mul(self.fuzz))
        return scattered.direction().dot(rec.normal) > 0, self.albedo, scattered


class Dielectric(Material):
    def __init__(self, index_of_refraction):
        self.ir = index_of_refraction

    def scatter(self, r_in, rec, scattered):

        return scattered.direction().dot(rec.normal) > 0, self.albedo, scattered
