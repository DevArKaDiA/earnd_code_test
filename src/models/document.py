from typing import Dict, List
from pydantic import BaseModel


class Document(BaseModel):
    name: str
    text: str
    sections: Dict[str, "Document"]
