#!usr/bin/python3
"""base class test module"""
import unittest
from models import base
import os
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """base class test class"""

    def setUp(self):
        base.Base._Base__nb_objects = 0

    def test_instance_of_base_class(self):
        base.Base.__nb_objects = 0
        b1 = base.Base()
        b2 = base.Base(42)
        self.assertTrue(isinstance(b1, base.Base))
        self.assertTrue(isinstance(b2, base.Base))

    def test_id_is_none(self):
        base.Base.__nb_objects = 0
        b1 = base.Base()
        b2 = base.Base()
        b4 = base.Base()
        b5 = base.Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 4)

    def test_id_not_none(self):
        b1 = base.Base(42)
        self.assertEqual(b1.id, 42)

    def test_id_isnone_and_notnone(self):
        b1 = base.Base()
        b2 = base.Base(98)
        b3 = base.Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 98)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        a_dict = {'a': 1, 'b': 2, 'c': 3}
        a_dict2 = {'d': 4, 'e': 5}
        json_str = base.Base.to_json_string([a_dict, a_dict2])
        self.assertTrue(type(json_str) is str)
        self.assertEqual(
            json_str, '[{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5}]')
        self.assertEqual(base.Base.to_json_string([]), '[]')
        self.assertEqual(base.Base.to_json_string(), '[]')

    def test_save_to_file(self):
        b1 = Rectangle(1, 2)
        b2 = Rectangle(3, 4, id=98)

        Rectangle.save_to_file([b1, b2])
        self.assertTrue(os.path.exists('Rectangle.json'))
        os.remove('Rectangle.json')

    def test_from_json_string(self):
        list_dict = base.Base.from_json_string(
            '[{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5}]')
        self.assertTrue(type(list_dict) is list)
        self.assertTrue(type(list_dict[0]) is dict)

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertTrue(type(r1_dictionary) is dict)
        r2 = Rectangle.create(**r1_dictionary)
        self.assertTrue(isinstance(r2, Rectangle))
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_load_from_file(self):
        pass

    def test_doc(self):
        self.assertIsNotNone(base.Base.__doc__)
        self.assertIsNotNone(base.__doc__)
        self.assertIsNotNone(base.Base.__init__.__doc__)


if __name__ == '__main__':
    unittest.main()
