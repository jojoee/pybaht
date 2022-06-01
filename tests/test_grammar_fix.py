import unittest
from pybaht import grammar_fix


class TestGrammarFix(unittest.TestCase):

    def test_ending_with_11(self):
        self.assertEqual(grammar_fix("หนึ่งสิบหนึ่ง"), "สิบเอ็ด")

    def test_ending_with_1x(self):
        self.assertEqual(grammar_fix("หนึ่งสิบหก"), "สิบหก")
        self.assertEqual(grammar_fix("หนึ่งสิบสี่"), "สิบสี่")
        self.assertEqual(grammar_fix("ห้าร้อยหนึ่งสิบสาม"), "ห้าร้อยสิบสาม")
        self.assertEqual(grammar_fix("สี่หมื่นหนึ่งสิบสาม"), "สี่หมื่นสิบสาม")

    def test_ending_with_2x(self):
        self.assertEqual(grammar_fix("ห้าร้อยสองสิบหนึ่ง"), "ห้าร้อยยี่สิบเอ็ด")
        self.assertEqual(grammar_fix("สองสิบสี่"), "ยี่สิบสี่")
        self.assertEqual(grammar_fix("เก้าแสนหกหมื่นสามพันสามร้อยสองสิบสี่"), "เก้าแสนหกหมื่นสามพันสามร้อยยี่สิบสี่")
        self.assertEqual(grammar_fix("เจ็ดหมื่นห้าพันสี่ร้อยสองสิบหนึ่ง"), "เจ็ดหมื่นห้าพันสี่ร้อยยี่สิบเอ็ด")
