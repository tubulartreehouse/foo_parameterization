import unittest
from foo_param.core import FooParameterization

class TestFooParameterization(unittest.TestCase):
    def test_calculate_volume(self):
        self.assertAlmostEqual(FooParameterization.calculate_volume(1), 4.1887902047863905)
        self.assertAlmostEqual(FooParameterization.calculate_volume(2), 33.510321638291124)
    
    def test_calculate_volume_significant_figures(self):
        self.assertAlmostEqual(FooParameterization.calculate_volume(1, significant_figures=2), 4.19)
        self.assertAlmostEqual(FooParameterization.calculate_volume(2, significant_figures=3), 33.510)
    
    def test_calculate_volume_custom_pi(self):
        self.assertAlmostEqual(FooParameterization.calculate_volume(1, custom_pi=3.14), 4.1866666666666665)
        self.assertAlmostEqual(FooParameterization.calculate_volume(2, custom_pi=3.14), 33.49333333333333)

    def test_calculate_volume_significant_figures_and_custom_pi(self):
        self.assertAlmostEqual(FooParameterization.calculate_volume(1, significant_figures=2, custom_pi=3.14), 4.19)
        self.assertAlmostEqual(FooParameterization.calculate_volume(2, significant_figures=3, custom_pi=3.14), 33.493)

    def test_calculate_volume_invalid_radius(self):
        with self.assertRaises(ValueError):
            FooParameterization.calculate_volume(-1)

if __name__ == '__main__':
    unittest.main()