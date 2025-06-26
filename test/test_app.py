import unittest
from form_matcher import find_matching_template

class TestFormMatcher(unittest.TestCase):

    def setUp(self):
        self.db_path = "database.json"

    def test_exact_match(self):
        data = {"login": "vasilev@example.com", "tel": "+7 985 456 78 90"}
        result = find_matching_template(self.db_path, data)
        self.assertEqual(result, "Данные пользователя")

    def test_extra_fields(self):
        data = {"login": "vasilev@example.com", "tel": "+7 985 456 78 90", "extra": "123"}
        result = find_matching_template(self.db_path, data)
        self.assertEqual(result, "Данные пользователя")

    def test_no_match(self):
        data = {"wwo": "mat"}
        result = find_matching_template(self.db_path, data)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["wwo"], "text")

    def test_partial_match(self):
        data = {"login": "vasilev@example.com"}
        result = find_matching_template(self.db_path, data)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
