from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Usuarios


class UsuarioRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    async def recuperar_usuario_por_email(self, email: str):
        statement = (
            select(Usuarios).select_from(Usuarios).where(Usuarios.email == email)
        )
        resultado = await self.session.execute(statement)
        usuario = resultado.scalar_one_or_none()
        return usuario
