import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return math.hypot(self.x, self.y, self.z)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return NotImplemented

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def normalized(self):
        length = abs(self)
        if length < 1e-9:
            raise ValueError()
        return Vector(self.x / length, self.y / length, self.z / length)

    def angle(self, other):
        len_a = abs(self)
        len_b = abs(other)
        if len_a < 1e-9 or len_b < 1e-9:
            raise ValueError()
        
        cos_phi = self.dot(other) / (len_a * len_b)
        cos_phi = max(-1.0, min(1.0, cos_phi))
        return math.acos(cos_phi)

    def is_orthogonal(self, other):
        return abs(self.dot(other)) < 1e-9

    def is_collinear(self, other):
        return abs(self.cross(other)) < 1e-9

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


def triangle_area(a, b, c):
    return 0.5 * abs((b - a).cross(c - a))


def volume(a, b, c):
    return abs(a.dot(b.cross(c)))


a = Vector(1, 0, 0)
b = Vector(0, 1, 0)

print(a + b)
print(a.dot(b))
print(a.cross(b))
print(b.cross(a))
print(abs(Vector(3, 4)))
print(2 * Vector(1, 2, 3))
print(a.is_orthogonal(b))
print(Vector(1, 2, 3).is_collinear(Vector(-2, -4, -6)))
print(round(a.angle(Vector(1, 1, 0)), 4))
print(triangle_area(Vector(0, 0), Vector(4, 0), Vector(0, 3)))
print(volume(Vector(1, 0, 0), Vector(0, 2, 0), Vector(0, 0, 3)))

try:
    Vector(0, 0, 0).normalized()
except ValueError:
    print("Ошибка: нельзя нормализовать нулевой вектор (ValueError)")