from dataclasses import dataclass

@dataclass
class SaveEmailRequest:
    event_id: int
    email_subject: str
    email_content: str
    timestamp: str

    def __post_init__(self):
        # Validate data here
        return