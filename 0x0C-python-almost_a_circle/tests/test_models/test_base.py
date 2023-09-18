#!/usr/bin/python3
"""Unittest for base module"""
import unittest
import sys
import random
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test class for Base class"""
    @classmethod
    def setUpClass(cls):
        """class method to set up the tests"""
        cls.ids = [0, 1, None, -3, "string", "", (1, 2), None, [1], [],
                   tuple(), 3.14, 1e1000, (1+5j), -0.2, None,
                   {"key": "value"}, {}, {1, 2, 3}, set(), {1}, None,
                   True, False]
        cls.rect_atts = ["id", "width", "height", "x", "y"]
        cls.square_atts = ["id", "size", "x", "y"]

    def test_ids(self):
        """ids of different types"""
        for i in range(len(self.ids)):
            base_inst = Base(self.ids[i])
            default_id = base_inst._Base__nb_objects
            with self.subTest(i=i):
                if self.ids[i] is not None:
                    self.assertEqual(base_inst.id, self.ids[i])
                else:
                    self.assertEqual(base_inst.id, default_id)

    def test_to_json_string_rectangle(self):
        """Tests to_json_string method using both
        Rectangle and Square class
        """
        r1 = Rectangle(1, 1, 0, 0)
        def_id = Rectangle._Base__nb_objects

        # Test case 1
        inst_dict = r1.to_dictionary()
        self.assertEqual(type(inst_dict).__name__, "dict")

        expected_dict = {"id": def_id, "width": 1, "height": 1, "x": 0, "y": 0}
        self.assertEqual(inst_dict, expected_dict)

        serialized_obj = Rectangle.to_json_string([inst_dict])
        self.assertEqual(type(serialized_obj).__name__, "str")

        expected_output = f"[{json.dumps(expected_dict, ensure_ascii=False)}]"
        self.assertEqual(serialized_obj, expected_output)

        # Test case 2
        vals = [sys.maxsize for i in range(5)]
        r1.update(*vals)

        inst_dict = r1.to_dictionary()
        self.assertEqual(type(inst_dict).__name__, "dict")

        expected_dict = {att: sys.maxsize for att in self.rect_atts}
        self.assertEqual(inst_dict, expected_dict)

        serialized_obj = Rectangle.to_json_string([inst_dict])
        self.assertEqual(type(serialized_obj).__name__, "str")

        expected_output = f"[{json.dumps(expected_dict, ensure_ascii=False)}]"
        self.assertEqual(serialized_obj, expected_output)

        # Test case 3

        expected_dict = {att: random.randint(1, sys.maxsize)
                         for att in self.rect_atts}
        r1.update(**expected_dict)

        inst_dict = r1.to_dictionary()
        self.assertEqual(type(inst_dict).__name__, "dict")

        self.assertEqual(inst_dict, expected_dict)

        serialized_obj = Rectangle.to_json_string([inst_dict])
        self.assertEqual(type(serialized_obj).__name__, "str")

        expected_output = f"[{json.dumps(expected_dict, ensure_ascii=False)}]"
        self.assertEqual(serialized_obj, expected_output)

    def test_to_json_string_multiple(self):
        """Testing serialization with both square and Rectangle"""
        # Using different serializable types
        serializable_ids = [0, 1, "string", "", [1], [], 3.14,
                            1e1000, {"key": "value"}, {}, True, False]

        r1 = Rectangle(1, 1)
        s1 = Square(1)

        for value in serializable_ids:
            expected_dict_r1 = {"id": value, "width": 1,
                                "height": 1, "x": 0, "y": 0}
            expected_dict_s1 = {"id": value, "size": 1, "x": 0, "y": 0}

            r1.update(**expected_dict_r1)
            s1.update(**expected_dict_s1)

            r1_dict = r1.to_dictionary()
            s1_dict = s1.to_dictionary()

            self.assertEqual(type(r1_dict).__name__, "dict")
            self.assertEqual(type(s1_dict).__name__, "dict")

            self.assertEqual(r1_dict, expected_dict_r1)
            self.assertEqual(s1_dict, expected_dict_s1)

            serialized_obj = Rectangle.to_json_string([r1_dict, s1_dict])
            self.assertEqual(type(serialized_obj).__name__, "str")

            json_str_r1 = json.dumps(expected_dict_r1, ensure_ascii=False)
            json_str_s1 = json.dumps(expected_dict_s1, ensure_ascii=False)
            expected_output = f"[{json_str_r1}, {json_str_s1}]"
            self.assertEqual(serialized_obj, expected_output)

    def test_to_json_string_square(self):
        """Tests to_json_string method on Square class"""
        s1 = Square(1)
        def_id = Square._Base__nb_objects

        # Test case 1
        s1_dict = s1.to_dictionary()
        self.assertEqual(type(s1_dict).__name__, "dict")

        expected_dict = {"id": def_id, "size": 1, "x": 0, "y": 0}
        self.assertEqual(s1_dict, expected_dict)

        serialized_obj = Square.to_json_string([s1_dict])
        self.assertEqual(type(serialized_obj).__name__, "str")

        expected_output = f"[{json.dumps(expected_dict, ensure_ascii=False)}]"
        self.assertEqual(serialized_obj, expected_output)

        # Test case 2
        vals = [sys.maxsize for i in range(4)]
        s1.update(*vals)

        s1_dict = s1.to_dictionary()
        self.assertEqual(type(s1_dict).__name__, "dict")

        expected_dict = {att: sys.maxsize for att in self.square_atts}
        self.assertEqual(s1_dict, expected_dict)

        serialized_obj = Square.to_json_string([s1_dict])
        self.assertEqual(type(serialized_obj).__name__, "str")

        expected_output = f"[{json.dumps(expected_dict, ensure_ascii=False)}]"
        self.assertEqual(serialized_obj, expected_output)

        # Test case 3
        expected_dict = {att: random.randint(1, sys.maxsize)
                         for att in self.square_atts}
        s1.update(**expected_dict)

        s1_dict = s1.to_dictionary()
        self.assertEqual(type(s1_dict).__name__, "dict")

        self.assertEqual(s1_dict, expected_dict)

        serialized_obj = Square.to_json_string([s1_dict])
        self.assertEqual(type(serialized_obj).__name__, "str")

        expected_output = f"[{json.dumps(expected_dict, ensure_ascii=False)}]"
        self.assertEqual(serialized_obj, expected_output)

    def test_to_json_string_large(self):
        """Tests to_json_string on a large number
        of instances
        """
        dictionary_list = []
        expected_output = []

        for i in range(10000):
            square_vals = {att: random.randint(1, 100)
                           for att in self.square_atts}
            rect_vals = {att: random.randint(1, 100) for att in self.rect_atts}

            new_square = Square(**square_vals)
            new_rect = Rectangle(**rect_vals)

            dictionary_list.extend([new_rect.to_dictionary(),
                                    new_square.to_dictionary()])
            expected_output.extend([rect_vals, square_vals])

        serialized_obj = Rectangle.to_json_string(dictionary_list)
        expected_output = f"{json.dumps(expected_output, ensure_ascii=False)}"
        self.assertEqual(serialized_obj, expected_output)

        self.assertEqual(Rectangle.to_json_string([]), "[]")

    def prepare_params(self, cls):
        """Returns necessary params for other test methods"""
        if cls.__name__ == "Rectangle":
            atts = self.rect_atts
        elif cls.__name__ == "Square":
            atts = self.square_atts

        expected_output = []
        dictionary_list = []

        for i in range(10):
            instance_vals = {att: random.randint(1, 100) for att in atts}

            new_instance = cls(**instance_vals)

            dictionary_list.append(new_instance)
            expected_output.append(instance_vals)

        return (dictionary_list, expected_output)

    def run_save_to_file_test(self, cls):
        """Helper method for test_save_to_file"""
        params = self.prepare_params(cls)
        cls.save_to_file(params[0])
        expected_output = f"{json.dumps(params[1], ensure_ascii=False)}"
        with open(f"{cls.__name__}.json", encoding="utf-8") as f:
            actual_output = f.read()

        self.assertEqual(actual_output, expected_output)

        # Test save_to_file on empty list of objects
        cls.save_to_file([])
        expected_output = "[]"
        with open(f"{cls.__name__}.json", encoding="utf-8") as f:
            actual_output = f.read()
        self.assertEqual(actual_output, expected_output)

    def test_save_to_file(self):
        """Tests save_to_file method on Rectangle and Square instances"""
        self.run_save_to_file_test(Rectangle)
        self.run_save_to_file_test(Square)

    def test_from_json_string(self):
        """Test from_json_string method"""
        rect_params = self.prepare_params(Rectangle)[1]
        square_params = self.prepare_params(Square)[1]

        expected_output = [rect_params, square_params]

        json_string = Base.to_json_string(expected_output)

        actual_output = Base.from_json_string(json_string)
        self.assertEqual(actual_output, expected_output)

        self.assertEqual(type(expected_output).__name__, "list")
        self.assertEqual(type(json_string).__name__, "str")
        self.assertEqual(type(actual_output).__name__, "list")

    def test_create(self):
        """Tests create method of Base class"""
        pass

if __name__ == "__main__":
    unittest.main()
