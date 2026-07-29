from pydantic import BaseModel
from enums import AcessoTipos


class LoginRequest(BaseModel):
    email: str
    senha: str


class LoginResponse(BaseModel):
    nome: str
    sobrenome: str
    acesso: AcessoTipos
