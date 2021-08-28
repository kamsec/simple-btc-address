# implementation of the elliptic curves arithmetic

# extended euclidean algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

# modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


class EllipticCurve:
    def __init__(self, p, ord_EC, a, b):
        self.p = p  # characteristic of the finite field that curve is defined over
        self.ord_EC = ord_EC  # order of the curve
        self.a = a  # a coefficient in short Weierstrass form
        self.b = b  # b coefficient in short Weierstrass form
        self.O = Point(None, None, self)  # point at infinity

class Point:
    def __init__(self, x, y, EC):
        self.x = x
        self.y = y
        self.EC = EC
        if Point.validate(self):
            pass
        else:
            raise Exception(f"Provided coordinates {self} don't form a point on that curve")

    # definition of point inversion on the elliptic curve
    def __neg__(self):
        if self.x is None:
            return self
        return Point(self.x, (-self.y) % self.EC.p, self.EC)

    # definition of point addition on the elliptic curve
    def __add__(self, other):
        if self.EC != other.EC:
            raise Exception('You cannot add two points on different curves')
        p = self.EC.p

        # cases involving identity element
        if self.x is None:
            return other
        elif other.x is None:
            return self
        elif self.x == other.x and other.y == ((-self.y) % self.EC.p):
            return self.EC.O
        else:
            # cases not involving identity element
            if self.x == other.x and self.y == other.y:
                # doubling
                # for that specific modinv function there has to be added +p to get proper result
                s = ((3 * self.x ** 2 + self.EC.a) * modinv(2 * self.y + p, p)) % p
            else:
                # addition
                s = ((other.y - self.y) * modinv((other.x - self.x + p), p)) % p
            x = (s ** 2 - self.x - other.x) % p
            y = (s * (self.x - x) - self.y) % p
            return Point(x, y, self.EC)

    # definition of point doubling on the elliptic curve
    def double(self):
        return self + self

    # definition of point scalar multiplication on the elliptic curve in form of scalar * Point
    def __rmul__(self, other):  # (Point, scalar)
        if isinstance(other, int) and isinstance(self, Point):
            # def point_scalar_multiplication(s, P, EC):  # double and add method
            Q = self.EC.O
            Q2 = Q
            binary = bin(other)
            binary = binary[2:]  # get rid of 0b

            NUM_BITS = 64
            # pre-pad binary with 0s - 1010 becomes 0000000...00001010
            binary = '0' * (NUM_BITS - len(binary)) + binary

            # reverse binary and iterate over bits
            for b in binary[::-1]:
                Q2 = Q + self
                if b == '1':
                    Q = Q2
                else:
                    Q2 = Q  # Useless, but balances instruction count
                self = self.double()
            return Q
        else:
            raise Exception('You can multiply only point by integer')

    # Point * scalar will work as well, just changing order
    def __mul__(self, other):
        self, other = other, self
        return self * other

    def validate(self):
        if self.x is None:
            return True
        return ((self.y ** 2 - (self.x ** 3 + self.EC.a * self.x + self.EC.b)) % self.EC.p == 0 and
                0 <= self.x < self.EC.p and 0 <= self.y < self.EC.p)

    # printing
    def __repr__(self):
        return f'({self.x}, {self.y})'

