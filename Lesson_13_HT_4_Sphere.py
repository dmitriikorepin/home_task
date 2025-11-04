import math

class Sphere:
    def __init__(self, radius, coordinate_x=0, coordinate_y=0, coordinate_z=0):
        self.radius = radius
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_z = coordinate_z

    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.coordinate_x, self.coordinate_y, self.coordinate_z)

    def set_center(self, coordinate_x, coordinate_y, coordinate_z):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_z = coordinate_z

    def is_point_inside(self, new_coordinate_x, new_coordinate_y, new_coordinate_z):
        distance = math.sqrt(
            (new_coordinate_x - self.coordinate_x) ** 2 +
            (new_coordinate_y - self.coordinate_y) ** 2 +
            (new_coordinate_z - self.coordinate_z) ** 2
        )
        return distance <= self.radius

my_sphere = Sphere(3, 1, 2, 3)
print(my_sphere.get_radius())
print(my_sphere.volume())
print(my_sphere.area())
print(my_sphere.is_point_inside(0.4, 0.7, 1))  # True


