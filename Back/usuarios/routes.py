from fastapi import APIRouter, Depends, Cookie, Response
import usuarios.schemas as schemas
from usuarios.services import UsuariosService
from usuarios.dependencies import get_usuario_service

router = APIRouter(prefix="/user", tags=["Main Route"])


@router.post("/login", response_model=schemas.LoginResponse)
async def rota_login(
    response: Response,
    dados_login: schemas.LoginRequest,
    service: UsuariosService = Depends(get_usuario_service)
):
    resultado, access_token = await service.validar_login(dados_login)
    response.set_cookie(
        key ="access_token",
        value= access_token,
        httponly= True,
        secure= False,
        samesite= "lax"
        )
    return resultado