import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

def area(a, b): 
    '''Принимает длины сторон прямоугольника, возвращает площадь прямоугольника'''
    return a * b 

def perimeter(a, b): 
    '''Принимает длины сторон прямоугольника, возвращает периметр прямоугольника'''
    return 2 * (a + b) 
