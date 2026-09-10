# Support Ticket Analyzer

A Python application and FastAPI service that analyzes support tickets from a CSV file and assigns a category and priority.

## Features

- Loads support tickets from a CSV file
- Categorizes tickets as Authentication, API Integration, Data Issue, or Other
- Assigns a priority: Critical, High, or Normal
- Provides a FastAPI endpoint for ticket analysis
- Includes automated tests for the application and API
- Runs locally or in a Docker container
- Uses transparent rule-based classification

## Run Locally

```bash
py ticket_analyzer.py
```

## Run the API

```bash
.\.venv\Scripts\python.exe -m uvicorn api:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Run with Docker

Build the image:

```bash
docker build -t support-ticket-analyzer .
```

Run the container:

```bash
docker run --rm -p 8000:8000 support-ticket-analyzer
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

- `GET /health` — checks whether the API is running
- `GET /tickets` — returns all analyzed tickets
- `GET /tickets/{ticket_id}` — returns one analyzed ticket
- `POST /analyze-ticket` — analyzes a new ticket sent to the API

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
├── .dockerignore
├── .gitignore
├── api.py
├── Dockerfile
├── requirements.txt
├── ticket_analyzer.py
└── README.md
```

## Built With

- Python 3.13
- FastAPI
- Docker
- Git
- GitHub