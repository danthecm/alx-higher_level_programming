import unittest

from models import base

class TestBase(unittest.TestCase):
    """Test Base class for testing base classes"""

    def test_create_instance(self):
        base.Base.__nb_objects = 0
        base1 = base.Base(1)
        base2 = base.Base(2)
        self.assertTrue(isinstance(base1, base.Base))
        self.assertTrue(isinstance(base2, base.Base))


if __name__ == '__main__':
    unittest.main()
