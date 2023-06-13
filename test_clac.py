import unittest
import clac


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(clac.add(10, 5), 15)
        self.assertEqual(clac.add(-1, 1), 0)
        self.assertEqual(clac.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(clac.subtract(10, 5), 5)
        self.assertEqual(clac.subtract(-1, 1), -2)
        self.assertEqual(clac.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(clac.multiply(10, 5), 50)
        self.assertEqual(clac.multiply(-1, 1), -1)
        self.assertEqual(clac.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(clac.divide(10, 5), 2)
        self.assertEqual(clac.divide(-1, 1), -1)
        self.assertEqual(clac.divide(-1, -1), 1)
        self.assertEqual(clac.divide(5, 2), 2)
        with self.assertRaises(ValueError):
            clac.divide(10,0)
        with self.assertRaises(TypeError):
            clac.divide(10, '8')
        with self.assertRaises(TypeError):
            clac.divide('number', 10)

    if __name__ == '__main__':
        unittest.main()
