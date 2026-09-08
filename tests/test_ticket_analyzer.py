import unittest

from ticket_analyzer import classify_category, determine_priority


class TicketAnalyzerTests(unittest.TestCase):
    def test_authentication_category(self):
        result = classify_category("A user needs a password reset.")
        self.assertEqual(result, "Authentication")

    def test_api_integration_category(self):
        result = classify_category("The API endpoint returns an error.")
        self.assertEqual(result, "API Integration")

    def test_data_issue_category(self):
        result = classify_category("The report has duplicate records.")
        self.assertEqual(result, "Data Issue")

    def test_critical_priority(self):
        result = determine_priority("All users cannot access the production application.")
        self.assertEqual(result, "Critical")

    def test_high_priority(self):
        result = determine_priority("The API request failed with an error.")
        self.assertEqual(result, "High")

    def test_normal_priority(self):
        result = determine_priority("A user needs help with a password reset.")
        self.assertEqual(result, "Normal")


if __name__ == "__main__":
    unittest.main()