import unittest
from pybaht import bahttext
import json
from typing import List


class TestBahttext(unittest.TestCase):
    def test_invalid_numbers(self):
        zero_text = 'ศูนย์บาทถ้วน'

        self.assertEqual(bahttext(None), zero_text)
        self.assertEqual(bahttext(True), zero_text)
        self.assertEqual(bahttext(False), zero_text)
        self.assertEqual(bahttext([]), zero_text)
        self.assertEqual(bahttext([1, 2, 3]), zero_text)
        self.assertEqual(bahttext({}), zero_text)
        self.assertEqual(bahttext(), zero_text)
        self.assertEqual(bahttext('this-is-not-number'), zero_text)
        self.assertEqual(bahttext('it-must-be-number-only'), zero_text)

    def test_numbers_are_imported_from_google_sheet(self):
        # TODO: define class
        test_cases: List[object] = []

        # load test cases from json file
        with open('testcases.json') as d:
            test_cases = json.load(d)

        for test_case in test_cases:
            input_number = float(test_case["number"])
            expected_string = test_case["text"]
            actual_string = bahttext(input_number)
            self.assertEqual(actual_string, expected_string)


if __name__ == "__main__":
    unittest.main()
