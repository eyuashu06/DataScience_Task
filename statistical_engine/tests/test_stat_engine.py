import unittest
from stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    # --------------------------
    # Setup
    # --------------------------
    def setUp(self):
        self.data = [1, 2, 2, 3, 4]
        self.engine = StatEngine(self.data)

    # --------------------------
    # Mean Tests
    # --------------------------
    def test_mean(self):
        self.assertEqual(self.engine.get_mean(), 2.4)

    # --------------------------
    # Median Tests
    # --------------------------
    def test_median_odd(self):
        self.assertEqual(self.engine.get_median(), 2)

    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    # --------------------------
    # Mode Tests
    # --------------------------
    def test_single_mode(self):
        self.assertEqual(self.engine.get_mode(), [2])

    def test_multimodal(self):
        engine = StatEngine([1, 1, 2, 2, 3])
        self.assertCountEqual(engine.get_mode(), [1, 2])

    def test_no_mode(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_mode(), "No mode (all values are unique)")

    # --------------------------
    # Variance Tests
    # --------------------------
    def test_sample_variance(self):
        self.assertAlmostEqual(self.engine.get_variance(), 1.3, places=1)

    def test_population_variance(self):
        self.assertAlmostEqual(self.engine.get_variance(is_sample=False), 1.04, places=2)

    def test_variance_single_value_sample(self):
        engine = StatEngine([5])
        with self.assertRaises(ValueError):
            engine.get_variance()

    # --------------------------
    # Standard Deviation Tests
    # --------------------------
    def test_standard_deviation(self):
        self.assertAlmostEqual(self.engine.get_standard_deviation(), 1.14, places=2)

    # --------------------------
    # Outlier Tests
    # --------------------------
    def test_outliers(self):
        engine = StatEngine([1, 2, 2, 3, 4, 100])
        self.assertEqual(engine.get_outliers(), [100])

    def test_no_outliers(self):
        self.assertEqual(self.engine.get_outliers(), [])

    # --------------------------
    # Error Handling Tests
    # --------------------------
    def test_empty_data(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            StatEngine([1, 2, "abc"])

    def test_convertible_string(self):
        engine = StatEngine([1, "2", 3])
        self.assertEqual(engine.get_mean(), 2.0)


# --------------------------
# Run Tests
# --------------------------
if __name__ == "__main__":
    unittest.main()