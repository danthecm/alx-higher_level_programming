#!/usr/bin/python3
"""Test for rectangle"""
import unittest
import sys
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Square test class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_issubclass(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_init(self):
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, x=1)
        self.assertRaises(TypeError, Square, y=5)
        self.assertRaises(TypeError, Square, id=98)

        rect_2attr = Square(9)
        self.assertEqual(rect_2attr.width, 9)
        self.assertEqual(rect_2attr.x, 0)
        self.assertEqual(rect_2attr.y, 0)
        rect_5attr = Square(21, 9, 5, 42)
        self.assertEqual(rect_5attr.x, 9)
        self.assertEqual(rect_5attr.y, 5)
        self.assertEqual(rect_5attr.id, 42)

    def test_input_validation(self):
        with self.assertRaises(TypeError):
            Square('a', 2)
        with self.assertRaises(TypeError):
            Square(1, [2])
        with self.assertRaises(TypeError):
            Square(1, 2, {'y': 3})
        with self.assertRaises(TypeError):
            Square(1, (2,), 4)

        with self.assertRaises(ValueError):
            Square(-1, 2)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_area(self):
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(10).area(), 100)
        self.assertEqual(Square(5, 4, 5, 98).area(), 25)

    def test_display(self):
        output = StringIO()  # create StringIO object
        sys.stdout = output  # assign to sys.stdout
        rect = Square(3)
        rect.display()  # output captured
        sys.stdout = sys.__stdout__  # reassign default to sys.stdout
        self.assertEqual(output.getvalue(), '###\n###\n###\n')

        output = StringIO()
        sys.stdout = output
        rect.x = 2
        rect.y = 3
        rect.display()
        sys.stdout = sys.__stdout__
        expected = '\n\n\n  ###\n  ###\n  ###\n'
        self.assertEqual(output.getvalue(), expected)

    def test_str(self):
        self.assertEqual(str(Square(3, 5, 6, 98)),
                         '[Square] (98) 5/6 - 3')

    def test_update(self):
        sqr = Square(10, 10, 10)

        sqr.update()
        self.assertEqual(str(sqr), '[Square] (1) 10/10 - 10')

        sqr.update(89)
        self.assertEqual(str(sqr), '[Square] (89) 10/10 - 10')

        sqr.update(89, 2)
        self.assertEqual(str(sqr), '[Square] (89) 10/10 - 2')

        sqr.update(89, 2, 4)
        self.assertEqual(str(sqr), '[Square] (89) 4/10 - 2')

        sqr.update(89, 2, 4, 5)
        self.assertEqual(str(sqr), '[Square] (89) 4/5 - 2')

        sqr2 = Square(10, 10, 10)

        sqr2.update(size=3)
        self.assertEqual(str(sqr2), '[Square] (2) 10/10 - 3')

        sqr2.update(size=3, x=2)
        self.assertEqual(str(sqr2), '[Square] (2) 2/10 - 3')

        sqr2.update(y=1, size=5, x=3, id=89)
        self.assertEqual(str(sqr2), '[Square] (89) 3/1 - 5')

        sqr2.update(x=1, y=3, size=4)
        self.assertEqual(str(sqr2), '[Square] (89) 1/3 - 4')

    def test_to_dictionary(self):
        sq = Square(2, 3, 4, 89)
        for attr in ['id', 'size', 'x', 'y']:
            self.assertTrue(attr in sq.to_dictionary().keys())
        self.assertEqual(sq.to_dictionary(),
                         {'id': 89, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(Square(2).to_dictionary(),
                         {'id': 1, 'size': 2, 'x': 0, 'y': 0})

    def test_doc(self):
        from models import square
        self.assertIsNotNone(square.__doc__)
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
