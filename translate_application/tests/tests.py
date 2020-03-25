import unittest

import main


class ValidLanguageTestCase(unittest.TestCase):
    def test_is_target_language_valid(self):
        result = main.is_target_language_valid('fr')
        self.assertTrue(result)

    def test_is_target_language_valid2(self):
        result = main.is_target_language_valid('')
        self.assertFalse(result)

    def test_is_target_language_valid3(self):
        result = main.is_target_language_valid('qwerty')
        self.assertFalse(result)

    def test_is_target_language_valid4(self):
        result = main.is_target_language_valid(None)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
