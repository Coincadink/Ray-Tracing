from Vec3 import Vec3


class Hittable:
    def hit(self, r, t_min, t_max, rec):
        pass


class HitRecord:
    def __init__(self, t=0.0, p=Vec3(0, 0, 0), normal=Vec3(0, 0, 0), front_face=Vec3(0, 0, 0), material=None):
        self.t = t
        self.p = p
        self.normal = normal
        self.front_face = front_face
        self.material = material

    def set_face_normal(self, r, outward_normal):
        self.front_face = r.direction().dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal
