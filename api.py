from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ticket_analyzer import analyze_ticket, load_tickets


app = FastAPI(
    title="Support Ticket Analyzer API",
    description="An API that analyzes support tickets and assigns a category and priority.",
    version="1.1.0",
)


class TicketRequest(BaseModel):
    title: str
    description: str


def get_analyzed_tickets():
    project_folder = Path(__file__).parent
    tickets_file = project_folder / "data" / "sample_tickets.csv"
    tickets = load_tickets(tickets_file)

    return [analyze_ticket(ticket) for ticket in tickets]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tickets")
def get_tickets():
    return get_analyzed_tickets()


@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: str):
    tickets = get_analyzed_tickets()

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    raise HTTPException(status_code=404, detail="Ticket not found")


@app.post("/analyze-ticket")
def analyze_new_ticket(ticket: TicketRequest):
    ticket_to_analyze = {
        "id": "NEW-TICKET",
        "title": ticket.title,
        "description": ticket.description,
    }

    return analyze_ticket(ticket_to_analyze)