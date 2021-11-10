import math

from Hittable import Hittable, HitRecord


class HittableList(Hittable):
    def __init__(self):
        self.hittable_objects = []

    def add(self, other):
        self.hittable_objects.append(other)

    def hit(self, r, t_min, t_max, rec):
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = t_max

        for hittable_object in self.hittable_objects:
            if hittable_object.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.t = temp_rec.t
                rec.p = temp_rec.p
                rec.normal = temp_rec.normal
                rec.front_face = temp_rec.front_face
                rec.material = temp_rec.material

        return hit_anything
