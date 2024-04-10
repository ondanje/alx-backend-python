import unittest
import utils
from utils import get_json
from parameterized import parameterized   # type: ignore
"""
importing unittest module for testing
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test method to check for output
        """
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, wrong_output):
        """
        Test method to catch exceptions
        """
        with self.assertRaises(KeyError) as e:
            utils.access_nested_map(nested_map, path)
            self.assertEqual(wrong_output, e.exception)

class TestGetJson(unittest.TestCase):
    """
    Get Json class to test
    """
    def test_get_json(self, test_url):
        pass
