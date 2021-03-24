class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        # end::source1[]
        # tag::source2[]
        if self.x is None and self.y is None:  # <1>

            return
        # end::source2[]
        # tag::source1[]
        if self.y**2 != self.x**3 + a * x + b:  # <1>
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

    def __eq__(self, other):  # <2>
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b
    # end::source1[]

    def __ne__(self, other):
        # this should be the inverse of the == operator
        return self.x != other.x or self.y != other.y \
            or self.a != other.a or self.b != other.b
    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    # tag::source3[]
    def __add__(self, other):  # <2>
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format
            (self, other))

        if self.x is None:  # <3>
            return other
        if other.x is None:  # <4>
            return self

        # vertical line (additive inverse)
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)
        # find the slope of the line
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s**2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

def test_online(x, y):
    print ({x, y}," ", y**2 == x**3 +5*x +7)

# test_online(2,4)
# test_online(-1,-1)
# test_online(18,77)
# test_online(5,7)

# test_online(2,2)
p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 7)

inf = Point(None, None, 5, 7)
print(p1 + inf)
print(inf + p2)
print(p1 + p2)