from typing import Dict, List
from pydantic import BaseModel

from models import document


class DB(BaseModel):
    documents: Dict[str, document.Document]


db = DB(
    documents={
        "my_document": document.Document(
            name="my_document",
            text="Prueba Earnd",
            sections={
                "Titulo": document.Document(
                    name="Titulo",
                    text="Hola Mundo",
                    sections={
                        "sub_titulo": document.Document(
                            name="sub_titulo",
                            text="Prueba Earnd subtitle",
                            sections={
                                "SubSub_Titulo": document.Document(
                                    name="SubSub_Titulo", text="Hola Mundo", sections={}
                                )
                            },
                        ),
                    },
                )
            },
        ),
        "my_document2": document.Document(
            name="my_document2",
            text="Prueba Earnd2",
            sections={
                "Titulo2": document.Document(
                    name="Titulo2", text="Hola Mundo2", sections={}
                )
            },
        ),
    }
)
