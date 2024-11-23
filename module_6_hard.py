import math

class Figure:
    sides_count = None

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = [*color]
        if len(sides) != self.sides_count:
            for i in range(self.sides_count):
                self.__sides.append(1)
        else:
            for i in range(self.sides_count):
                self.__sides.append(*sides)
        self.filled = bool
        self.sides = []
        self.color = []

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        _count = 0
        for i in range(len(sides)):
            if sides[i] > 0 and isinstance(sides[i], int) is True:
                _count += 1
        if _count == len(sides) and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) is True:
            self.__sides = [*new_sides]

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = [*color]
        self.filled = bool
        if len(sides) != self.sides_count:
            self.__sides.append(1)
        else:
            self.__sides = [*sides]
        self.__radius = sum(self.__sides) / 2 * math.pi

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        count = 0
        for i in range(len(sides)):
            if sides[i] > 0 and isinstance(sides[i], int) is True:
                count += 1
        if count == len(sides) and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) is True:
            self.__sides = [*new_sides]

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = [*color]
        self.filled = bool
        for i in range(self.sides_count):
            self.__sides.append(None)
        if len(sides) != self.sides_count:
            for i in range(self.sides_count):
                self.__sides[i] = 1
        else:
            for i in range(self.sides_count):
                self.__sides[i] = sides[i]
        self.p = sum(self.__sides) / 2

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        _count = 0
        for i in range(len(sides)):
            if sides[i] > 0 and isinstance(sides[i], int) is True:
                _count += 1
        if _count == len(sides) and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) is True:
            self.__sides = [*new_sides]

    def get_square(self):
        return math.sqrt(self.p * (self.p - self.__sides[0]) * (self.p - self.__sides[1]) * (self.p - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = [*color]
        self.filled = bool
        if len(sides) == 1:
            for i in range(self.sides_count):
                self.__sides.append(*sides)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)
        self.__len_side = self.__sides[0]

    def get_volume(self):
        return self.__len_side ** 3

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        _count = 0
        for i in range(len(sides)):
            if sides[i] > 0 and isinstance(sides[i], int) is True:
                _count += 1
        if _count == len(sides) and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) is True:
            self.__sides = [*new_sides]


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
