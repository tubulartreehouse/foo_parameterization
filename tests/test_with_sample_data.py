import unittest
import csv
from foo_param.core import FooParameterization

class TestFooParameterizationWithSampleData(unittest.TestCase):
    def setUp(self):
        # Load sample data from CSV
        self.sample_data = []
        with open('foo_param/data/sample_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.sample_data.append((float(row['radius']), float(row['volume'])))
    
    def test_calculate_volume_with_sample_data(self):
        for radius, expected_volume in self.sample_data:
            with self.subTest(radius=radius):
                calculated_volume = FooParameterization.calculate_volume(radius)
                self.assertAlmostEqual(calculated_volume, expected_volume, places=7)

if __name__ == '__main__':
    unittest.main()