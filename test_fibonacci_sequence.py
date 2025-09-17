import unittest
from fibonacci_sequence import generate_fibonacci

class TestFibonacciSequence(unittest.TestCase):
    def test_standard_fibonacci(self):
        """Test standard Fibonacci sequence starting with [0, 1]"""
        self.assertEqual(generate_fibonacci([0, 1], 10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_empty_sequence(self):
        """Test sequence of length 0"""
        self.assertEqual(generate_fibonacci([0, 1], 0), [])
    
    def test_length_one(self):
        """Test sequence of length 1"""
        self.assertEqual(generate_fibonacci([0, 1], 1), [0])
    
    def test_length_two(self):
        """Test sequence of length 2"""
        self.assertEqual(generate_fibonacci([3, 5], 2), [3, 5])
    
    def test_custom_start(self):
        """Test sequence with custom starting numbers"""
        self.assertEqual(generate_fibonacci([2, 3], 5), [2, 3, 5, 8, 13])
    
    def test_negative_numbers(self):
        """Test sequence starting with negative numbers"""
        self.assertEqual(generate_fibonacci([-1, 4], 4), [-1, 4, 3, 7])
    
    def test_invalid_start_sequence_length(self):
        """Test invalid start sequence (wrong length)"""
        with self.assertRaises(ValueError):
            generate_fibonacci([1], 5)
        with self.assertRaises(ValueError):
            generate_fibonacci([1, 2, 3], 5)
    
    def test_invalid_length(self):
        """Test invalid length parameter"""
        with self.assertRaises(ValueError):
            generate_fibonacci([0, 1], -1)
    
    def test_invalid_start_sequence_type(self):
        """Test invalid start sequence type"""
        with self.assertRaises(ValueError):
            generate_fibonacci("01", 5)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2)
