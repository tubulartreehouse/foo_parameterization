import unittest
from foo_param.core import FooParameterization

class TestFooParameterization(unittest.TestCase):
    def test_calculate_volume(self):
        self.assertAlmostEqual(FooParameterization.calculate_volume(1), 4.1887902047863905)
        self.assertAlmostEqual(FooParameterization.calculate_volume(2), 33.510321638291124)
    
    def test_calculate_volume_invalid_radius(self):
        with self.assertRaises(ValueError):
            FooParameterization.calculate_volume(-1)

if __name__ == '__main__':
    unittest.main()