import unittest 

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):

        self.assertIsNone(None, "value must contain an English text")
        self.assertEqual(english_to_french("Hello"),"Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(None, "value must contain a French text")
        self.assertEqual(french_to_english("Bonjour"),"Hello")


unittest.main()

