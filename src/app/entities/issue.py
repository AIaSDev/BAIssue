from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Issue:
    id: Optional[int]
    title: str
    body: Optional[str] = None
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("Issue title cannot be empty")