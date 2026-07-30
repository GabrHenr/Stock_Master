from fastapi import Depends
from database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from .services import UsuariosService
from .repository import UsuarioRepository


def get_usuario_repository(
    session: AsyncSession = Depends(get_session),
) -> UsuarioRepository:
    return UsuarioRepository(session)


def get_usuario_service(
    session: AsyncSession = Depends(get_session),
    repository: UsuarioRepository = Depends(get_usuario_repository),
) -> UsuariosService:
    return UsuariosService(session=session, repository=repository)
