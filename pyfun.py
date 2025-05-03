import math

class Shape:
    """Base shape class."""
    def area(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.__class__.__name__} area: {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Example usage
c = Circle(3)
r = Rectangle(4, 5)
t = Triangle(6, 2)

print(c)
print(r)
print(t)
