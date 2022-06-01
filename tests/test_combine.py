import unittest
from pybaht import combine


class TestCombine(unittest.TestCase):

    def test_both_baht_and_satang_are_empty(self):
        self.assertEqual(combine("", ""), "ศูนย์บาทถ้วน")

    def test_both_baht_and_satang_are_not_empty(self):
        self.assertEqual(combine("หนึ่งร้อยยี่สิบสาม", "ห้าสิบหก"), "หนึ่งร้อยยี่สิบสามบาทห้าสิบหกสตางค์")

    def test_has_only_baht(self):
        self.assertEqual(combine("แปดแสนเจ็ดหมื่นสี่พันห้าร้อยหกสิบสาม", ""),
                         "แปดแสนเจ็ดหมื่นสี่พันห้าร้อยหกสิบสามบาทถ้วน")

    def test_has_only_satang(self):
        self.assertEqual(combine("", "ลบสามสิบหก"), "ลบสามสิบหกสตางค์")
