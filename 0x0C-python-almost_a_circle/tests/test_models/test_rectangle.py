#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle
import sys
import random
import doctest


class TestRectangleClass(unittest.TestCase):
    """Test class for Rectangle class"""
    def test_atts(self):
        """test valid Rectangle instance attributes"""
        # List of different possible valid types
        rect_atts = [{"width": 12, "height": 4},
                     {"id": 13, "width": 3, "height": 4, "x": 7, "y": 8},
                     {"id": 0, "width": 5, "height": 7},
                     {"id": 1, "width": 4, "height": 3, "x": 1},
                     {"id": None, "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": -3, "width": 4, "height": 3},
                     {"id": "string", "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": "", "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": (1, 2), "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": [1], "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": [], "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": tuple(), "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": 3.14, "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": 1e1000, "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": (1+5j), "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": -0.2, "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": {"key": "value"}, "width": 4, "height": 3},
                     {"id": {}, "width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": {1, 2, 3}, "width": 4, "height": 3},
                     {"id": set(), "width": 4, "height": 3, "x": 1, "y": 3},
                     {"width": 4, "height": 3, "x": 1, "y": 3},
                     {"id": {4}, "width": 4, "height": 3, "x": 1, "y": 3}]

        # Tests if values have correctly been assigned to a Rectangle instance
        for i in range(len(rect_atts)):
            parameters = rect_atts[i]
            rect_inst = Rectangle(**parameters)
            default_id = Rectangle._Base__nb_objects

            expected_atts = {"id": None, "width": None,
                             "height": None, "x": None, "y": None}

            for key in expected_atts.keys():
                if key in parameters.keys():
                    if key == "id" and parameters[key] is None:
                        expected_atts[key] = default_id
                    else:
                        expected_atts[key] = parameters[key]
                else:
                    if key == "id":
                        expected_atts[key] = default_id
                    else:
                        expected_atts[key] = 0

            for key in rect_inst.__dict__.keys():
                rect_key = key[12:] if key != "id" else key
                self.assertEqual(rect_inst.__dict__[key],
                                 expected_atts[rect_key])

    def test_exceptions(self):
        """Tests different exceptions raised by
        Rectangle class
        """
        # List of invalid attribute types for width, height, x and y
        invalid_atts = ["string", "", {}, {1, 2}, set(), (1, 2), tuple(),
                        {"key": "value"}, [1, 2], [], 3.14, (1+5j), b"Hello",
                        1e3000]

        # Tests invalid attributes of invalid types
        r1 = Rectangle(1, 1)
        for att in invalid_atts:
            with self.assertRaises(TypeError, msg="width must be an integer"):
                Rectangle(att, 1)
            with self.assertRaises(TypeError, msg="height must be an integer"):
                Rectangle(1, att)
            with self.assertRaises(TypeError, msg="x must be an integer"):
                Rectangle(1, 1, att)
            with self.assertRaises(TypeError, msg="y must be an integer"):
                Rectangle(1, 1, 1, att)
            with self.assertRaises(TypeError, msg="width must be an integer"):
                r1.width = att
            with self.assertRaises(TypeError, msg="height must be an integer"):
                r1.height = att
            with self.assertRaises(TypeError, msg="x must be an integer"):
                r1.x = att
            with self.assertRaises(TypeError, msg="y must be an integer"):
                r1.y = att
            with self.assertRaises(TypeError, msg="width must be an integer"):
                r1.update(width=att)
            with self.assertRaises(TypeError, msg="height must be an integer"):
                r1.update(height=att)
            with self.assertRaises(TypeError, msg="x must be an integer"):
                r1.update(x=att)
            with self.assertRaises(TypeError, msg="y must be an integer"):
                r1.update(y=att)

        # Tests zero and negative values for width and height
        for i in range(-1, 1):
            with self.assertRaises(ValueError, msg="width must be > 0"):
                Rectangle(i, 1)
            with self.assertRaises(ValueError, msg="height must be > 0"):
                Rectangle(1, i)
            with self.assertRaises(ValueError, msg="width must be > 0"):
                r1.width = i
            with self.assertRaises(ValueError, msg="height must be > 0"):
                r1.height = i
            with self.assertRaises(ValueError, msg="width must be > 0"):
                r1.update(width=i)
            with self.assertRaises(ValueError, msg="height must be > 0"):
                r1.update(height=i)

        # Tests negative values for x and y
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(1, 1, 1, -1)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r1.x = -1
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r1.y = -1
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r1.update(x=-1)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r1.update(y=-1)

        # Tests missing required parameters width and height
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_area(self):
        """Test area method of Rectangle class"""
        r1 = Rectangle(3, 7)
        self.assertEqual(r1.area(), 21)

        width = height = sys.maxsize
        area = width * height
        r2 = Rectangle(width, height)
        self.assertEqual(r2.area(), area)

        r3 = Rectangle(1, 1)
        self.assertEqual(r3.area(), 1)

        width = random.randint(1, sys.maxsize)
        height = random.randint(1, sys.maxsize)
        area = width * height
        r4 = Rectangle(width, height)
        self.assertEqual(r4.area(), area)

    @staticmethod
    def extract_atts(rect):
        """Extracts attributes of a Rectangle
        instance and returns them as a list
        """
        return [rect.id, rect.width, rect.height, rect.x, rect.y]

    @staticmethod
    def str_helper(clsType, id, width, height, x, y):
        """Returns the expected output of the __str__
        method for comparison purposes
        """
        return f"[{clsType.__name__}] ({id}) {x}/{y} - {width}/{height}"

    def test_getters_setters(self):
        """Tests getters and setters of Rectangle class"""
        max_int = sys.maxsize
        r1 = Rectangle(1, 1)

        # Testing getters and setters with sys.maxsize
        r1.x = r1.y = r1.width = r1.height = r1.id = max_int
        # Getting all instance attributes
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying values were correctly assigned to all instance attributes
        self.assertEqual(r1_atts, [max_int, max_int,
                         max_int, max_int, max_int])

        # Testing getters and setters with lowest possible valid values
        r1.width, r1.height, r1.x, r1.y = 1, 1, 0, 0
        # Getting all instance attributes
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying values were correctly assigned to all instance attributes
        self.assertEqual(r1_atts, [max_int, 1, 1, 0, 0])

        # Testing getters and setters with randomly generated values
        random_vals = [random.randint(1, max_int) for i in range(5)]
        # Setting all instance attributes
        r1.id, r1.width, r1.height, r1.x, r1.y = random_vals
        # Getting all instance attributes
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying values were correctly assigned to all instance attributes
        self.assertEqual(r1_atts, random_vals)

    def test_update_args(self):
        """Tests the update method of Rectangle class
        using non-keyworded arguments"""
        max_int = sys.maxsize
        r1 = Rectangle(1, 1)

        # Testing update using sys.maxsize
        r1.update(max_int, max_int, max_int, max_int, max_int)
        # Getting the instance attributes after updating
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying that the values were correctly updated
        self.assertEqual(r1_atts, [max_int, max_int,
                         max_int, max_int, max_int])

        # Testing update using the lowest possible valid values
        r1.update(89, 1, 1, 0, 0)
        # Getting the instance attributes after updating
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying that the values were correctly updated
        self.assertEqual(r1_atts, [89, 1, 1, 0, 0])

        # Testing update using randomly generated values
        random_vals = [random.randint(1, max_int) for i in range(5)]
        r1.update(*random_vals)
        # Getting the instance attributes after updating
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying that the values were correctly updated
        self.assertEqual(r1_atts, random_vals)

    def test_update_kwargs(self):
        """Tests the update method of Rectangle class
        using keyworded arguments"""
        max_int = sys.maxsize
        r1 = Rectangle(1, 1)
        atts = ["id", "width", "height", "x", "y"]

        # Testing update with kwargs using sys.maxsize
        # Generating a dictionary with all attributes set to sys.max_size
        new_vals = {att: max_int for att in atts}
        # Updating instance attributes
        r1.update(**new_vals)
        # Getting the instance attributes after updating
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying that the values were correctly updated
        self.assertEqual(r1_atts, [max_int, max_int,
                         max_int, max_int, max_int])

        # Testing update using kwargs with the lowest possible valid values
        # Updating instance attributes
        r1.update(id=89, width=1, height=1, x=0, y=0)
        # Getting the instance attributes after updating
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying that the values were correctly updated
        self.assertEqual(r1_atts, [89, 1, 1, 0, 0])

        # Testing update with kwargs using randomly generated values
        # Generating a dictionary with random values
        random_vals = {att: random.randint(1, max_int) for att in atts}
        # Updating the Rectangle insatance
        r1.update(**random_vals)
        # Getting all instance attributes
        r1_atts = TestRectangleClass.extract_atts(r1)
        # Verifying that the attributes of the instance match the random values
        self.assertEqual(r1_atts, [random_vals[key] for key in atts])

    def test_str_method(self):
        """Tests str method of Rectangle class"""
        max_int = sys.maxsize

        r1 = Rectangle(1, 1)
        def_id = Rectangle._Base__nb_objects

        # Getting the expected output
        expected_output = TestRectangleClass.str_helper(type(r1), def_id,
                                                        1, 1, 0, 0)
        # Verifying that __str__ returns correct output
        self.assertEqual(str(r1), expected_output)

        # Updating all attributes
        r1.update("id", max_int, max_int, max_int, max_int)
        # Getting the expected output
        expected_output = TestRectangleClass.str_helper(type(r1), "id",
                                                        max_int, max_int,
                                                        max_int, max_int)
        # Verifying that __str__ returns correct output
        self.assertEqual(str(r1), expected_output)

        # Generating random values
        random_vals = [random.randint(1, max_int) for i in range(5)]
        # Updating the attributes of the Rectangle instance using random values
        r1.update(*random_vals)
        # Getting the expected output
        expected_output = TestRectangleClass.str_helper(type(r1), *random_vals)
        # Verifying that __str__ returns correct output
        self.assertEqual(str(r1), expected_output)

    def test_display(self):
        """Tests the display method of the Rectangle class.
        The test is extracted from a doctest file
        """
        # Opening and reading the content of doctest file
        with open("display_method_test.txt", "r", encoding="utf-8") as f:
            doctest_text = f.read()

        # Parsing the doctest content and creating a DocTest object
        parser = doctest.DocTestParser()
        test = parser.get_doctest(doctest_text, {}, "display_method_test.txt",
                                  None, None)

        # Running the doctest and capturing the results
        runner = doctest.DocTestRunner()
        runner.run(test)

        # Use unittest assertions to make assertions about the results
        self.assertEqual(runner.failures, 0, "Doctests failed")

    def test_to_dictionary(self):
        """Tests the to_dictionary method of the Rectangle class"""
        atts = ["id", "width", "height", "x", "y"]
        max_int = sys.maxsize

        r1 = Rectangle(1, 1)
        values = [Rectangle._Base__nb_objects, 1, 1, 0, 0]
        expected_output = {key: value for key, value in zip(atts, values)}
        self.assertEqual(r1.to_dictionary(), expected_output)

        values = [max_int for i in range(5)]
        r1.update(*values)
        expected_output = {key: value for key, value in zip(atts, values)}
        self.assertEqual(r1.to_dictionary(), expected_output)

        values = [random.randint(1, max_int) for i in range(5)]
        r1.update(*values)
        expected_output = {key: value for key, value in zip(atts, values)}
        self.assertEqual(r1.to_dictionary(), expected_output)
