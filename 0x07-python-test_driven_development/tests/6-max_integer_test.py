#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ testing class for max_integer in
    the 6-max_integer module """
    def test_positive_integers(self):
        """tests max_integer function against
        positive integers"""
        a = [64, 82, 58, 66, 12, 9, 60, 17, 92, 9]
        self.assertEqual(max_integer(a), 92)

        b = [311, 642, 287, 369, 547, 632, 455, 482, 676, 790]
        self.assertEqual(max_integer(b), 790)

        c = [280, 1046, 360, 813, 474, 465, 584, 357, 535, 1016]
        self.assertEqual(max_integer(c), 1046)

        d = [133, 148, 63, 107, 85, 11, 105, 90, 75, 11]
        self.assertEqual(max_integer(d), 148)

        a1 = (12, 100, 928, 22, 0, 1001, 34, 100)
        self.assertEqual(max_integer(a1), 1001)

        d1 = [100]
        self.assertEqual(max_integer(d1), 100)

    def test_negative_integers(self):
        """tests max_integer function against
        negative integers"""
        e = [-81, -30, -26, -44, -74, -75, -90, -24, -79, -69]
        self.assertEqual(max_integer(e), -24)

        f = [-804, -554, -622, -908, -986, -662, -988, -539, -755, -617]
        self.assertEqual(max_integer(f), -539)

        g = [-3, -7, -10, -1, -8, -8, -5, -6, -4, -8]
        self.assertEqual(max_integer(g), -1)

        h = (-297, -135, -255, -201, -102, -236, -254, -256, -269, -251)
        self.assertEqual(max_integer(h), -102)

    def test_floating_point_numbers(self):
        """tests max_integer function against
        floating-point numbers"""
        i = [49.143284, 4.719485, 91.23428, 53.049459, 20.285009,
             96.224357, 15.447278, 39.796289, 64.399266, 28.776587]
        self.assertEqual(max_integer(i), 96.224357)

        j = [-0.86, 0.19, -0.78, 0.58, -0.71, 0.01, -0.3, 0.02, -0.75, 0.37]
        self.assertEqual(max_integer(j), 0.58)

        k = (0.87, 1.79, 9.64, 3.33, 7.58, 9.71, 5.07, 7.9, 0.53, 5.49)
        self.assertEqual(max_integer(k), 9.71)

        lst = [-0.86, -0.3, -0.31, -2.55, -1.36,
               -0.01, -5.8, -3.51, -3.43, -5.85]
        self.assertEqual(max_integer(lst), -0.01)

    def test_strings(self):
        """tests max_integer against strings
        Expected behaviour: returns the char
        or string with the highest ascii value.
        """
        string1 = "This is not a list of numbers"
        self.assertEqual(max_integer(string1), "u")

        string2 = "AbCdEfGhIjKlMnOpQrStUvWxYz"
        self.assertEqual(max_integer(string2), "z")

        string3 = "CHECKING SENTENCE 3"
        self.assertEqual(max_integer(string3), "T")

        characters = ("b", "L", "H", "P", "x", "1", "3", "m")
        self.assertEqual(max_integer(characters), "x")

        strings = ("word", "xylophone", "123422", "House")
        self.assertEqual(max_integer(strings), "xylophone")

    def test_exceptions(self):
        """tests various exceptions raised by
        max_integer when the input data is
        invalid
        """
        lst1 = ["Sentence", None, [1, 2, 3], 100, 13.9823, 1e3000, (1+5j)]
        with self.assertRaises(TypeError):
            max_integer(lst1)

        lst2 = [(1, 2, 3), 10.23, (62, 0.11, 192.3445), 100]
        with self.assertRaises(TypeError):
            max_integer(lst2)

        var1 = None
        with self.assertRaises(TypeError):
            max_integer(var1)

        var2 = 1029
        with self.assertRaises(TypeError):
            max_integer(var2)

        var3 = 182.273664
        with self.assertRaises(TypeError):
            max_integer(var3)

        var4 = (92, "string", [1, 2, 3])
        with self.assertRaises(TypeError):
            max_integer(var4)

        var5 = [{"title": "roadmap", "function": "gets you places"},
                {"title": "knife", "function": "cuts things"}]
        with self.assertRaises(TypeError):
            max_integer(var5)

        var6 = {"dictionary": "This is a dict"}
        with self.assertRaises(KeyError):
            max_integer(var6)

        with self.assertRaises(TypeError):
            max_integer([[], (), {}])

        with self.assertRaises(TypeError):
            max_integer({{}, {}, {}})

    def test_empty(self):
        """tests empty sequences against max_integer
        """
        s = []
        self.assertEqual(max_integer(s), None)

        self.assertEqual(max_integer(), None)

        t = [[], [], []]
        self.assertEqual(max_integer(t), [])

        u = ()
        self.assertEqual(max_integer(u), None)

        v = ((), (), ())
        self.assertEqual(max_integer(v), ())


if __name__ == "__main__":
    unittest.main()
