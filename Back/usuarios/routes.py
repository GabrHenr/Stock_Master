from fastapi import APIRouter, Depends
import usuarios.schemas as schemas
from usuarios.services import UsuariosService
from usuarios.dependencies import get_usuario_service

router = APIRouter(prefix="/user", tags=["Main Route"])


@router.get("/login", response_model=schemas.LoginResponse)
async def rota_login(
    dados_login: schemas.LoginRequest,
    service: UsuariosService = Depends(get_usuario_service),
):
    resultado = await service.validar_login(dados_login)
    return resultado