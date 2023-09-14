from unit_test import utils
import unittest

class TestMethods(unittest.TestCase):
    def test_reverse(self):
        util = utils()
        self.assertEqual(util.reversed("5"), -1)
        self.assertEqual(util.reversed("-2"), -1)
        self.assertEqual(util.reversed(-1), -1)
        self.assertEqual(util.reversed(20), 2)
        self.assertEqual(util.reversed(12345), 54321)
        self.assertEqual(util.reversed(0), 0)
        self.assertEqual(util.reversed(2.5), -1)
        self.assertEqual(util.reversed(0.5), -1)

    def test_bases(self):
        util = utils()
        self.assertEqual(util.formatter("5"), (-1, -1))
        self.assertEqual(util.formatter("-2"), (-1, -1))
        self.assertEqual(util.formatter(-1), (bin(-1), oct(-1)))
        self.assertEqual(util.formatter(-64), (bin(-64), oct(-64)))
        self.assertEqual(util.formatter(64), (bin(64), oct(64)))
        self.assertEqual(util.formatter(123), (bin(123), oct(123)))
        self.assertEqual(util.formatter(0), (bin(0), oct(0)))
        self.assertEqual(util.formatter(2.5), (-1, -1))
        self.assertEqual(util.formatter(0.5), (-1, -1))

if __name__ == "__main__":
    unittest.main()