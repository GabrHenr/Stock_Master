from fastapi import APIRouter, Depends
from services import MarcasServices
from schemas import RegistrandoMarcaRequest
from ..marcas.dependencies import get_marcas_service
from ..contracts.UsuarioAutenticado import UsuarioAutenticado
from ..dependencies.auth import get_usuario_autenticado

router = APIRouter(prefix="/marca", tags=["Rota Marca"])


@router.get("/lista")
async def listar_marcas_registradas(
    nome_marca: RegistrandoMarcaRequest,
    service: MarcasServices = Depends(get_marcas_service),
    usuario: UsuarioAutenticado = Depends(get_usuario_autenticado),
):
    resultado = await service.registro_marca_nova(usuario,nome_marca)
