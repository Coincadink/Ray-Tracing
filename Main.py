# This project is currently using the .ppm file format. This "portable pixel map"
# file format notates the color of each pixel on the screen sequentially. A file
# must start with a line "P3" indicating ascii color use, a line formatted as "x y"
# to define the dimensions of the file as x columns, and y rows, and finally a line
# to indicate the max color value, such as "255." This file will be read as the
# pixels from left to right, and as rows top to bottom.

# TODO: Antialiasing increased render time by 67x... this can't be the best way.

import sys
from Vec3 import Vec3, random_in_unit_sphere, random_in_hemisphere
from Color import Color, write_color
from Sphere import Sphere
from Hittable import HitRecord
from HittableList import HittableList
from Ray import Ray
from Camera import Camera
from random import random
from Material import Lambertian, Metal


def ray_color(r, world, depth):
    rec = HitRecord()

    if depth <= 0:
        return Color(0, 0, 0)

    if world.hit(r, 0.0001, sys.float_info.max, rec):
        hit = rec.material.scatter(r, rec)  # hit[0] = boolean, hit[1] = albedo, hit[2] = scattered
        if hit[0]:
            return hit[1] * ray_color(hit[2], world, depth - 1)
        return Color(0, 0, 0)

    unit_direction = r.direction().unit_vector()
    t = (unit_direction.y() + 1.0) * 0.5
    return Color(1, 1, 1).mul(1.0 - t) + Color(0.5, 0.7, 1.0).mul(t)


def main():
    # Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 1
    max_depth = 10

    # World
    world = HittableList()

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Lambertian(Color(0.7, 0.3, 0.3))
    material_left = Metal(Color(0.8, 0.8, 0.8), 0.3)
    material_right = Metal(Color(0.8, 0.6, 0.2), 1.0)

    world.add(Sphere(Vec3(0, -100.5, -1), 100, material_ground))
    world.add(Sphere(Vec3(0, 0, -1), 0.5, material_center))
    world.add(Sphere(Vec3(-1, 0, -1), 0.5, material_left))
    world.add(Sphere(Vec3(1, 0, -1), 0.5, material_right))

    # Camera
    cam = Camera()

    # Render
    with open("file.ppm", 'w') as f:
        f.write("P3\n" + str(image_width) + " " + str(image_height) + "\n255\n")

        for j in range(image_height - 1, -1, -1):
            print("Scan-lines remaining: " + str(j + 1))

            for i in range(image_width):
                pixel_color = Color(0, 0, 0)
                for s in range(samples_per_pixel):
                    u = (i + random()) / (image_width - 1)
                    v = (j + random()) / (image_height - 1)
                    r = cam.get_ray(u, v)
                    pixel_color += ray_color(r, world, max_depth)
                write_color(f, pixel_color, samples_per_pixel)
        print("Done.")


if __name__ == "__main__":
    main()
