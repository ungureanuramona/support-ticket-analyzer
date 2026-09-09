import unittest

from fastapi.testclient import TestClient

from api import app
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


class TicketAnalyzerApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_get_tickets_endpoint(self):
        response = self.client.get("/tickets")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)

    def test_analyze_ticket_endpoint(self):
        ticket = {
            "title": "Users cannot log in",
            "description": "All users cannot access the production application.",
        }

        response = self.client.post("/analyze-ticket", json=ticket)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["category"], "Authentication")
        self.assertEqual(response.json()["priority"], "Critical")


if __name__ == "__main__":
    unittest.main()