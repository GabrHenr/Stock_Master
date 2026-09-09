from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from .repository import MarcaRepository
from .services import MarcasServices
from ..dependencies.database import get_session


def get_marcas_repositor(
    session: AsyncSession = Depends(get_session),
) -> MarcaRepository:
    return MarcaRepository(session)


def get_marcas_service(
    session: AsyncSession = Depends(get_session),
    repository: MarcaRepository = Depends(get_marcas_repositor),
):
    return MarcasServices(session, repository)
