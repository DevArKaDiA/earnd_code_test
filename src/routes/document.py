from typing import Optional
from flask import request, Blueprint
from models import document
from service import document_service

document_blueprint = Blueprint("documents", __name__)


@document_blueprint.route("/", methods=["GET"])
def get_documents():
    return document_service.get_all_documents()


@document_blueprint.route("/<document_name>/sections/<path>", methods=["GET"])
@document_blueprint.route("/<document_name>/sections/", methods=["GET"])
def get_document_sections(document_name: str, path: Optional[str] = None):
    return document_service.get_sections_by_path(
        document_name=document_name, path=path
    ).dict()


@document_blueprint.route("/<document_name>/sections/", methods=["POST"])
@document_blueprint.route("/<document_name>/sections/<path>", methods=["POST"])
def create_document_section(document_name: str, path: Optional[str] = None):
    section = document.Document.parse_obj(request.json)
    try:
        document_service.add_section(
            document_name=document_name, path=path, section=section
        )
    except document_service.SectionNotFoundException:
        raise document_service.SectionNotFoundException
    else:
        return document_service.get_sections_by_path(
            document_name=document_name, path=path
        ).dict()
