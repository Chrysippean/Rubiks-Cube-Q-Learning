class Point(object):
    """A 3D point/vector"""

    def __init__(self, x, y=None, z=None):
        """Construct a Point from an (x, y, z) tuple or an iterable"""
        try:
            # convert from an iterable
            ii = iter(x)
            self.x = ii.next()
            self.y = ii.next()
            self.z = ii.next()
        except TypeError:
            # not iterable
            self.x = x
            self.y = y
            self.z = z
        if any(val is None for val in self):
            raise ValueError("Point does not allow None values: %s" % self)

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        return "Point" + str(self)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)

    def dot(self, other):
        """Return the dot product"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Point(self.y * other.z - self.z * other.y,
                     self.z * other.x - self.x * other.z,
                     self.x * other.y - self.y * other.x)

    def __getitem__(self, item):
        return tuple(self)[item]

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def count(self, *args):
        return tuple(self).count(*args)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __ne__(self, other):
        return not (self == other)


class Matrix(object):
    """A 3x3 matrix"""

    def __init__(self, *args):
        """Matrix(1, 2, 3, 4, 5, 6, 7, 8, 9)
        Matrix([1, 2, 3, 4, 5, 6, 7, 8, 9])
        Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        Matrix(x for x in range(1, 10))
        """
        if len(args) == 9:
            self.vals = list(args)
        elif len(args) == 3:
            try:
                self.vals = [x for y in args for x in y]
            except:
                self.vals = []
        else:
            self.__init__(*args[0])

        if len(self.vals) != 9:
            raise ValueError("Matrix requires 9 items, got %s" % args)

    def __str__(self):
        return "[{0}, {1}, {2},\n" \
               " {3}, {4}, {5},\n" \
               " {6}, {7}, {8}]".format(*self.vals)

    def __repr__(self):
        return "Matrix({0}, {1}, {2},\n" \
               "       {3}, {4}, {5},\n" \
               "       {6}, {7}, {8})".format(*self.vals)

    def __eq__(self, other):
        return self.vals == other.vals

    def __add__(self, other):
        return Matrix(a + b for a, b in zip(self.vals, other.vals))

    def __sub__(self, other):
        return Matrix(a - b for a, b in zip(self.vals, other.vals))

    def __iadd__(self, other):
        self.vals = [a + b for a, b in zip(self.vals, other.vals)]
        return self

    def __isub__(self, other):
        self.vals = [a - b for a, b in zip(self.vals, other.vals)]
        return self

    def __mul__(self, other):
        """Do Matrix-Matrix or Matrix-Point multiplication."""
        if isinstance(other, Point):
            return Point(other.dot(Point(row)) for row in self.rows())
        elif isinstance(other, Matrix):
            return Matrix(Point(row).dot(Point(col)) for row in self.rows() for col in other.cols())

    def rows(self):
        yield self.vals[0:3]
        yield self.vals[3:6]
        yield self.vals[6:9]

    def cols(self):
        yield self.vals[0:9:3]
        yield self.vals[1:9:3]
        yield self.vals[2:9:3]