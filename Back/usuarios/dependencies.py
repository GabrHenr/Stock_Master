from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .services import UsuariosService
from .repository import UsuarioRepository
from ..dependencies.database import get_session


def get_usuario_repository(
    session: AsyncSession = Depends(get_session),
) -> UsuarioRepository:
    return UsuarioRepository(session)


def get_usuario_service(
    session: AsyncSession = Depends(get_session),
    repository: UsuarioRepository = Depends(get_usuario_repository),
) -> UsuariosService:
    return UsuariosService(session=session, usuario_repository=repository)
