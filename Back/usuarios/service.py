from repository import UsuarioRepository
from sqlalchemy.ext.asyncio import AsyncSession
from schema import LoginRequest
class UsuariosService:
    def __init__(self,repositorio: UsuarioRepository):
        self.repositorio = repositorio
        
    async def validar_login(self, session:AsyncSession, dados_login: LoginRequest, access_token):
        pass