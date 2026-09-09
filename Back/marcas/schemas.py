from pydantic import BaseModel


class RegistrandoMarcaRequest(BaseModel):
    nome: str
