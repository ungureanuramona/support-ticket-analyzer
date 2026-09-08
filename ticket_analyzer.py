import csv
from pathlib import Path


def load_tickets(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def classify_category(text):
    normalized_text = text.lower()

    category_keywords = {
        "Authentication": ["login", "password", "access", "authentication"],
        "API Integration": ["api", "integration", "endpoint", "request"],
        "Data Issue": ["data", "report", "duplicate", "record"],
    }

    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in normalized_text:
                return category

    return "Other"


def determine_priority(text):
    normalized_text = text.lower()

    critical_keywords = ["production", "outage", "all users", "cannot access"]
    high_keywords = ["error", "failed", "urgent"]

    for keyword in critical_keywords:
        if keyword in normalized_text:
            return "Critical"

    for keyword in high_keywords:
        if keyword in normalized_text:
            return "High"

    return "Normal"


def analyze_ticket(ticket):
    full_text = f"{ticket['title']} {ticket['description']}"

    return {
        "id": ticket["id"],
        "title": ticket["title"],
        "category": classify_category(full_text),
        "priority": determine_priority(full_text),
    }


def main():
    project_folder = Path(__file__).parent
    tickets_file = project_folder / "data" / "sample_tickets.csv"
    tickets = load_tickets(tickets_file)

    print("--- Support Ticket Analysis ---")

    for ticket in tickets:
        analysis = analyze_ticket(ticket)

        print(f"\nTicket: {analysis['id']}")
        print(f"Title: {analysis['title']}")
        print(f"Category: {analysis['category']}")
        print(f"Priority: {analysis['priority']}")


if __name__ == "__main__":
    main()