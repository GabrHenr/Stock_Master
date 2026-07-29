from usuarios.repository import UsuarioRepository
from sqlalchemy.ext.asyncio import AsyncSession
from usuarios.schemas import LoginRequest
from utils.hash_senha import ServicosSenha
from utils.jwt import ServicosJwt
from models import Usuarios
from utils.exceptions import HttpException


class UsuariosService:
    def __init__(self, session: AsyncSession, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository
        self.session = session
        
    async def validar_login(self, dados_login: LoginRequest):
        usuarioBD: Usuarios|None = await self.usuario_repository.recuperar_usuario_por_email(
            email= dados_login.email
        )
        if not usuarioBD:
            raise HttpException.usuario_ou_senha_incorretos()
        isSenhaValida = ServicosSenha.verificar_senha(
            dados_login.senha, usuarioBD.senha
        )
        if not isSenhaValida:
            raise HttpException.usuario_ou_senha_incorretos()
        access_token = ServicosJwt.criar_jwt(
            acesso=usuarioBD.acesso, email=usuarioBD.email, id=usuarioBD.id
        )
        return usuarioBD, access_token
