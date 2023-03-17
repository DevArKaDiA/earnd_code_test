from typing import Dict, List, Optional
from flask import request, Blueprint
from pydantic import BaseModel, validator
from models import document
from service import document_service

document_blueprint = Blueprint("documents", __name__)


class CreateDocumentSectionInput(BaseModel):
    path: Optional[str] = None
    name: str
    text: str
    sections: Dict[str, "CreateDocumentSectionInput"] = {}

    @validator("sections", pre=True)
    def convert_sections(cls, sections):
        if isinstance(sections, list):
            return {section["name"]: section for section in sections}
        return sections


class GetDocumentSectionInput(BaseModel):
    path: Optional[str] = None


class GetDocumentSectionsResponse(BaseModel):
    name: str
    text: str
    sections: List["GetDocumentSectionsResponse"] = []

    @validator("sections", pre=True)
    def convert_sections(cls, sections):
        if isinstance(sections, dict):
            return list(sections.values())
        return sections


class GetDocumentsResponse(BaseModel):
    documents: List[GetDocumentSectionsResponse]

    @validator("documents", pre=True)
    def convert_sections(cls, documents):
        if isinstance(documents, dict):
            return list(documents.values())
        return documents


@document_blueprint.route("/", methods=["GET"])
def get_documents():
    return GetDocumentsResponse(documents=document_service.get_all_documents()).dict()


@document_blueprint.route("/<document_name>/sections/", methods=["GET"])
def get_document_sections(document_name: str):
    input = (
        GetDocumentSectionInput.parse_obj(request.get_json(silent=True))
        if request.get_json(silent=True)
        else GetDocumentSectionInput()
    )

    return GetDocumentSectionsResponse.parse_obj(
        document_service.get_sections_by_path(
            document_name=document_name, path=input.path
        ),
    ).dict()


@document_blueprint.route("/<document_name>/sections/", methods=["POST"])
def create_document_section(document_name: str):
    section = CreateDocumentSectionInput.parse_obj(request.json)
    try:
        document_service.add_section(
            document_name=document_name,
            path=section.path,
            section=document.Document.parse_obj(section),
        )
    except document_service.SectionNotFoundException:
        raise document_service.SectionNotFoundException
    else:
        return GetDocumentSectionsResponse.parse_obj(
            document_service.get_sections_by_path(
                document_name=document_name, path=section.path
            ),
        ).dict()
