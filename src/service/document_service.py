from typing import Dict, Optional, cast

from pydantic import BaseModel
from models import db
from models import document
import pydash


class SectionNotFoundException(Exception):
    ...


def _find_section_by_dot_notation(
    base_document: document.Document, path: str
) -> Optional[document.Document]:
    section = pydash.get(
        base_document.sections,
        path=".sections.".join(path.split(".")),
    )
    section = cast(Optional[document.Document], section)
    return section


def find_section_by_path(
    document_name: str, path: Optional[str] = None
) -> Optional[document.Document]:
    if path:
        return _find_section_by_dot_notation(db.db.documents[document_name], path=path)
    else:
        return db.db.documents[document_name]


def get_sections_by_path(
    document_name: str, path: Optional[str] = None
) -> document.Document:
    if section := find_section_by_path(document_name=document_name, path=path):
        return section
    else:
        raise SectionNotFoundException


def add_section(document_name: str, path: Optional[str], section: document.Document):
    document = get_sections_by_path(document_name=document_name, path=path)
    document.sections[section.name] = section


def get_all_documents() -> Dict[str, document.Document]:
    return db.db.dict()["documents"]
