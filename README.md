# Support Ticket Analyzer

A Python command-line application that analyzes support tickets from a CSV file and assigns a category and priority.

## Features

- Loads support tickets from a CSV file
- Categorizes tickets as Authentication, API Integration, Data Issue, or Other
- Assigns a priority: Critical, High, or Normal
- Uses transparent rule-based classification
- Includes automated tests
- Includes sample support tickets for testing

## Run Locally

```bash
py ticket_analyzer.py
```

## Run Tests

```bash
py -m unittest discover -s tests
```

## Project Structure

```text
support-ticket-analyzer/
├── data/
│   └── sample_tickets.csv
├── tests/
│   └── test_ticket_analyzer.py
├── ticket_analyzer.py
└── README.md
```

## Built With

- Python 3.13
- Git
- GitHub