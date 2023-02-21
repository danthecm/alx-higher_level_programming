#!/usr/bin/python3
"""Test for rectangle"""
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Rectangle test class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_issubclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_init(self):
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)
        self.assertRaises(TypeError, Rectangle, height=2)
        self.assertRaises(TypeError, Rectangle, x=1)
        self.assertRaises(TypeError, Rectangle, y=5)
        self.assertRaises(TypeError, Rectangle, id=98)

        rect_2attr = Rectangle(21, 9)
        self.assertEqual(rect_2attr.width, 21)
        self.assertEqual(rect_2attr.height, 9)
        self.assertEqual(rect_2attr.x, 0)
        self.assertEqual(rect_2attr.y, 0)
        rect_5attr = Rectangle(21, 9, 4, 5, 42)
        self.assertEqual(rect_5attr.x, 4)
        self.assertEqual(rect_5attr.y, 5)
        self.assertEqual(rect_5attr.id, 42)

    def test_input_validation(self):
        with self.assertRaises(TypeError):
            Rectangle('a', 2)
        with self.assertRaises(TypeError):
            Rectangle(1, [2])
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {'x': 3})
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, (4,))

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(2, 5, 4, 5, 98).area(), 10)

    def test_display(self):
        output = StringIO()  # create StringIO object
        sys.stdout = output  # assign to sys.stdout
        rect = Rectangle(2, 5)
        rect.display()  # output captured
        sys.stdout = sys.__stdout__  # reassign default to sys.stdout
        self.assertEqual(output.getvalue(), '##\n##\n##\n##\n##\n')

        output = StringIO()
        sys.stdout = output
        rect.x = 2
        rect.y = 3
        rect.display()
        sys.stdout = sys.__stdout__
        expected = '\n\n\n  ##\n  ##\n  ##\n  ##\n  ##\n'
        self.assertEqual(output.getvalue(), expected)

    def test_str(self):
        self.assertEqual(str(Rectangle(3, 2, 5, 6, 98)),
                         '[Rectangle] (98) 5/6 - 3/2')

    def test_update(self):
        rect = Rectangle(10, 10, 10, 10)

        rect.update()
        self.assertEqual(str(rect), '[Rectangle] (1) 10/10 - 10/10')

        rect.update(89)
        self.assertEqual(str(rect), '[Rectangle] (89) 10/10 - 10/10')

        rect.update(89, 2)
        self.assertEqual(str(rect), '[Rectangle] (89) 10/10 - 2/10')

        rect.update(89, 2, 3)
        self.assertEqual(str(rect), '[Rectangle] (89) 10/10 - 2/3')

        rect.update(89, 2, 3, 4)
        self.assertEqual(str(rect), '[Rectangle] (89) 4/10 - 2/3')

        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rect), '[Rectangle] (89) 4/5 - 2/3')

        rect2 = Rectangle(10, 10, 10, 10)

        rect2.update(height=1)
        self.assertEqual(str(rect2), '[Rectangle] (2) 10/10 - 10/1')

        rect2.update(width=1, x=2)
        self.assertEqual(str(rect2), '[Rectangle] (2) 2/10 - 1/1')

        rect2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rect2), '[Rectangle] (89) 3/1 - 2/1')

        rect2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rect2), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        r1 = Rectangle(2, 3, 4, 5, 89)
        for attr in ['id', 'width', 'height', 'x', 'y']:
            self.assertTrue(attr in r1.to_dictionary().keys())
        self.assertEqual(r1.to_dictionary(),
                         {'id': 89, 'width': 2, 'height': 3, 'x': 4, 'y': 5})
        self.assertEqual(Rectangle(2, 3).to_dictionary(),
                         {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0})

    def test_doc(self):
        from models import rectangle
        self.assertIsNotNone(rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
