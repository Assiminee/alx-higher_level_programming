#!/usr/bin/python3
"""Unittest for base module"""
import pep8
import unittest


class TestPep8(unittest.TestCase):
    """Test if files follow pep8 coding style"""
    def test_pep8(self):
        """tests if files conform to pep8 style"""
        style = pep8.StyleGuide()
        checker = style.check_files(['models/base.py',
                                     'models/rectangle.py',
                                     'models/square.py',
                                     'tests/test_models/test_base.py',
                                     'tests/test_models/test_rectangle.py',
                                     'tests/test_models/test_pep8.py'])
        self.assertEqual(checker.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
