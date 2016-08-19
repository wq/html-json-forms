import unittest
from collections import OrderedDict
from html_json_forms import parse_json_form, ParseException


class TestAdditionalCases(unittest.TestCase):
    """
    Tests for the HTML JSON form algorithm
    Examples 1-10 from http://www.w3.org/TR/html-json-forms/
    """

    def test_sparse_array(self):
        """
        Sparse array
        """
        input_data = {
            'test[0]': 1,
            'test[100]': 1,
        }
        result = parse_json_form(input_data)
        assert 'test' in result
        assert len(result['test']) == 101

    def test_sparser_array(self):
        """
        Sparser array
        """
        input_data = OrderedDict((
            ('test[0]', 1),
            ('test[1000]', 1),
            ('test[2000]', 1),
        ))
        result = parse_json_form(input_data)
        assert 'test' in result
        assert len(result['test']) == 2001

    def test_invalid_array(self):
        """
        Sparse array with 1,000 consecutive blank values
        """
        input_data = {
            'test[0]': 1,
            'test[1001]': 1,
        }
        with self.assertRaises(ParseException):
            parse_json_form(input_data)
