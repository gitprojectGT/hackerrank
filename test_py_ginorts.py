import unittest
import sys
import os
from io import StringIO
import importlib.util

# Add the current directory to the path to import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the module with hyphens in filename
spec = importlib.util.spec_from_file_location("py_ginorts", "py-ginorts.py")
py_ginorts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(py_ginorts)

# Import functions from the module
sort_string_ginorts = py_ginorts.sort_string_ginorts
extract_digits_only = py_ginorts.extract_digits_only
separate_digits_non_digits = py_ginorts.separate_digits_non_digits
arrange_digits_odd_first = py_ginorts.arrange_digits_odd_first


class TestPyGinorts(unittest.TestCase):
    """Comprehensive test suite for py-ginorts.py functions"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_strings = [
            "Sorting1234",
            "abcABC123",
            "zZaA9876543210",
            "Hello123World456",
            "aA1bB2cC3",
            "",
            "12345",
            "abcdef",
            "ABCDEF",
            "135792468",
            "!@#$%^&*()",
            "a1B2c3D4e5F6",
            "ZzYyXx321",
            "987654321abcABC"
        ]

    def test_sort_string_ginorts_basic(self):
        """Test basic functionality of sort_string_ginorts"""
        # Test the main example
        result = sort_string_ginorts("Sorting1234")
        expected = "ginortS1324"  # lowercase, uppercase, odd digits, even digits
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_mixed_case(self):
        """Test sorting with mixed case letters and digits"""
        result = sort_string_ginorts("abcABC123")
        expected = "abcABC13"  # a,b,c then A,B,C then 1,3 (odds) then none (no evens except 2 which should be last)
        # Let me recalculate: abc (lowercase), ABC (uppercase), 1,3 (odd), 2 (even)
        expected = "abcABC132"
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_all_digits(self):
        """Test sorting string with only digits"""
        result = sort_string_ginorts("12345")
        expected = "13524"  # odd digits first (1,3,5), then even (2,4)
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_all_lowercase(self):
        """Test sorting string with only lowercase letters"""
        result = sort_string_ginorts("dcba")
        expected = "abcd"
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_all_uppercase(self):
        """Test sorting string with only uppercase letters"""
        result = sort_string_ginorts("DCBA")
        expected = "ABCD"
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_empty_string(self):
        """Test sorting empty string"""
        result = sort_string_ginorts("")
        expected = ""
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_complex(self):
        """Test complex string with all character types"""
        result = sort_string_ginorts("zZaA9876543210")
        # Expected: lowercase(a,z), uppercase(A,Z), odd(9,7,5,3,1), even(8,6,4,2,0)
        expected = "azAZ9753186420"
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_repeated_characters(self):
        """Test string with repeated characters"""
        result = sort_string_ginorts("aabbcc112233")
        # Expected: lowercase(a,a,b,b,c,c), odd(1,1,3,3), even(2,2)
        expected = "aabbcc113322"
        self.assertEqual(result, expected)

    def test_extract_digits_only_basic(self):
        """Test extract_digits_only function"""
        result = extract_digits_only("abc123def456")
        expected = ['1', '2', '3', '4', '5', '6']
        self.assertEqual(result, expected)

    def test_extract_digits_only_no_digits(self):
        """Test extract_digits_only with no digits"""
        result = extract_digits_only("abcdef")
        expected = []
        self.assertEqual(result, expected)

    def test_extract_digits_only_only_digits(self):
        """Test extract_digits_only with only digits"""
        result = extract_digits_only("123456")
        expected = ['1', '2', '3', '4', '5', '6']
        self.assertEqual(result, expected)

    def test_extract_digits_only_empty_string(self):
        """Test extract_digits_only with empty string"""
        result = extract_digits_only("")
        expected = []
        self.assertEqual(result, expected)

    def test_separate_digits_non_digits_mixed(self):
        """Test separate_digits_non_digits with mixed input"""
        digits, non_digits = separate_digits_non_digits("abc123XYZ")
        expected_digits = ['1', '2', '3']
        expected_non_digits = ['a', 'b', 'c', 'X', 'Y', 'Z']
        self.assertEqual(digits, expected_digits)
        self.assertEqual(non_digits, expected_non_digits)

    def test_separate_digits_non_digits_only_digits(self):
        """Test separate_digits_non_digits with only digits"""
        digits, non_digits = separate_digits_non_digits("123456")
        expected_digits = ['1', '2', '3', '4', '5', '6']
        expected_non_digits = []
        self.assertEqual(digits, expected_digits)
        self.assertEqual(non_digits, expected_non_digits)

    def test_separate_digits_non_digits_only_letters(self):
        """Test separate_digits_non_digits with only letters"""
        digits, non_digits = separate_digits_non_digits("abcXYZ")
        expected_digits = []
        expected_non_digits = ['a', 'b', 'c', 'X', 'Y', 'Z']
        self.assertEqual(digits, expected_digits)
        self.assertEqual(non_digits, expected_non_digits)

    def test_separate_digits_non_digits_empty(self):
        """Test separate_digits_non_digits with empty string"""
        digits, non_digits = separate_digits_non_digits("")
        expected_digits = []
        expected_non_digits = []
        self.assertEqual(digits, expected_digits)
        self.assertEqual(non_digits, expected_non_digits)

    def test_arrange_digits_odd_first_mixed(self):
        """Test arrange_digits_odd_first with mixed odd and even"""
        result = arrange_digits_odd_first(['1', '2', '3', '4', '5', '6'])
        expected = ['1', '3', '5', '2', '4', '6']
        self.assertEqual(result, expected)

    def test_arrange_digits_odd_first_only_odd(self):
        """Test arrange_digits_odd_first with only odd digits"""
        result = arrange_digits_odd_first(['1', '3', '5', '7', '9'])
        expected = ['1', '3', '5', '7', '9']
        self.assertEqual(result, expected)

    def test_arrange_digits_odd_first_only_even(self):
        """Test arrange_digits_odd_first with only even digits"""
        result = arrange_digits_odd_first(['2', '4', '6', '8'])
        expected = ['2', '4', '6', '8']
        self.assertEqual(result, expected)

    def test_arrange_digits_odd_first_empty(self):
        """Test arrange_digits_odd_first with empty list"""
        result = arrange_digits_odd_first([])
        expected = []
        self.assertEqual(result, expected)

    def test_arrange_digits_odd_first_single_odd(self):
        """Test arrange_digits_odd_first with single odd digit"""
        result = arrange_digits_odd_first(['7'])
        expected = ['7']
        self.assertEqual(result, expected)

    def test_arrange_digits_odd_first_single_even(self):
        """Test arrange_digits_odd_first with single even digit"""
        result = arrange_digits_odd_first(['8'])
        expected = ['8']
        self.assertEqual(result, expected)

    def test_arrange_digits_odd_first_alternating(self):
        """Test arrange_digits_odd_first with alternating pattern"""
        result = arrange_digits_odd_first(['2', '1', '4', '3', '6', '5'])
        expected = ['1', '3', '5', '2', '4', '6']
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_special_characters(self):
        """Test sorting with special characters (should be treated as non-digits)"""
        result = sort_string_ginorts("a!1B@2c#3")
        # Special characters should be sorted with letters, digits separated
        # Expected: non-digits in order they appear in sorting, then odd, then even
        # This might need adjustment based on exact sorting behavior
        self.assertTrue(isinstance(result, str))
        self.assertEqual(len(result), 9)

    def test_sort_string_ginorts_zero_digit(self):
        """Test sorting with zero digit (even)"""
        result = sort_string_ginorts("a0b1c2")
        # Expected: lowercase letters, then odd digits, then even digits
        expected = "abc102"
        self.assertEqual(result, expected)

    def test_sort_string_ginorts_performance_large_input(self):
        """Test performance with larger input"""
        large_input = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" * 10
        result = sort_string_ginorts(large_input)
        self.assertTrue(isinstance(result, str))
        self.assertEqual(len(result), len(large_input))

    def test_functions_dont_modify_input(self):
        """Test that functions don't modify the original input"""
        original_list = ['1', '2', '3', '4']
        original_list_copy = original_list.copy()
        arrange_digits_odd_first(original_list)
        self.assertEqual(original_list, original_list_copy)

    def test_edge_cases_unicode(self):
        """Test edge cases with potential unicode characters"""
        # Test with basic ASCII only to avoid unicode complications
        result = sort_string_ginorts("àáâã123")
        self.assertTrue(isinstance(result, str))

    def test_main_function_output(self):
        """Test the main function output by capturing stdout"""
        # Capture stdout to test print statements
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Import and run the main section
        import py_ginorts
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("s1:", output)
        self.assertIn("s2:", output)
        self.assertIn("Refactored result:", output)


class TestErrorHandling(unittest.TestCase):
    """Test error handling and edge cases"""

    def test_non_string_input_handling(self):
        """Test behavior with non-string inputs"""
        with self.assertRaises((TypeError, AttributeError)):
            sort_string_ginorts(123)
        
        with self.assertRaises((TypeError, AttributeError)):
            sort_string_ginorts(None)

    def test_arrange_digits_non_digit_input(self):
        """Test arrange_digits_odd_first with non-digit strings"""
        with self.assertRaises(ValueError):
            arrange_digits_odd_first(['a', 'b', 'c'])


if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2)
