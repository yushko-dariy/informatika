class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Polygon:
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError()
        self._points = [Point(p.x, p.y) for p in points]

    def perimeter(self):
        n = len(self._points)
        perm = 0.0
        for i in range(n):
            p1 = self._points[i]
            p2 = self._points[(i + 1) % n]
            perm += ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
        return perm

    def area(self):
        n = len(self._points)
        total = 0.0
        for i in range(n):
            p1 = self._points[i]
            p2 = self._points[(i + 1) % n]
            total += p1.x * p2.y - p2.x * p1.y
        return 0.5 * abs(total)

    def move(self, dx, dy):
        for p in self._points:
            p.x += dx
            p.y += dy

    def bounding_box(self):
        xs = [p.x for p in self._points]
        ys = [p.y for p in self._points]
        return min(xs), min(ys), max(xs), max(ys)

    def is_convex(self):
        n = len(self._points)
        has_pos = False
        has_neg = False
        
        for i in range(n):
            pA = self._points[i]
            pB = self._points[(i + 1) % n]
            pC = self._points[(i + 2) % n]
            
            cross_product = (pB.x - pA.x) * (pC.y - pB.y) - (pB.y - pA.y) * (pC.x - pB.x)
            
            if cross_product > 1e-9:
                has_pos = True
            elif cross_product < -1e-9:
                has_neg = True
                
            if has_pos and has_neg:
                return False
                
        return True

    def __len__(self):
        return len(self._points)

    def __lt__(self, other):
        if isinstance(other, Polygon):
            return self.area() < other.area()
        return NotImplemented


corner = Point(0, 0)
square = Polygon([corner, Point(2, 0), Point(2, 2), Point(0, 2)])

print(len(square))
print(square.perimeter())
print(square.area())
print(square.is_convex())

square.move(5, 5)
print(square.bounding_box())
print(corner.x)

letter_g = Polygon([Point(0, 0), Point(2, 0), Point(2, 1),
                    Point(1, 1), Point(1, 2), Point(0, 2)])

print(letter_g.area())
print(letter_g.is_convex())
print(letter_g < square)

try:
    Polygon([Point(0, 0), Point(1, 1)])
except ValueError:
    print("Ошибка: многоугольник должен иметь не менее 3 вершин (ValueError)")