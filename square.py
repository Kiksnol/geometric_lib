import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(25)
        self.assertEqual(res, 625)


def area(a):
    '''Принимает длину сторон квадрата, возвращает площадь квадрата'''
    return a * a


def perimeter(a):
    '''Принимает длину сторон квадрата, возвращает периметр квадрата'''
    return 4 * a
