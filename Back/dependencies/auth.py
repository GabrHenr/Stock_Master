from typing import Annotated
from fastapi import Cookie
from ..utils.jwt import ServicosJwt
from ..contracts.UsuarioAutenticado import UsuarioAutenticado
async def get_usuario_autenticado(
    access_token: Annotated[str| None, Cookie()]=None
):
    dados = ServicosJwt.validar_e_retornar_dados_jwt(access_token)
    return UsuarioAutenticado(
        id = dados["id"],
        email = dados["email"],
        acesso = dados["acesso"]

    )