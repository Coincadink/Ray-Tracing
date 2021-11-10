class Ray:
    def __init__(self, origin, direction):
        self.orig = origin
        self.dir = direction

    def __str__(self):
        return str("Origin: " + str(self.orig.x()) + ", "
                   + str(self.orig.y()) + ", "
                   + str(self.orig.z()) + "\n"
                   + "Direction: " + str(self.dir.x()) + ", "
                   + str(self.dir.y()) + ", "
                   + str(self.dir.z())
                   )

    def origin(self):
        return self.orig

    def direction(self):
        return self.dir

    def at(self, t):
        return self.orig + self.dir.mul(t)
