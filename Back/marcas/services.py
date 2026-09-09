from sqlalchemy.ext.asyncio import AsyncSession
from marcas.repository import MarcaRepository
from schemas import RegistrandoMarcaRequest
from utils.exceptions import HttpException
from ..contracts.UsuarioAutenticado import UsuarioAutenticado


class MarcasServices:
    def __init__(self, session: AsyncSession, marcas_repository: MarcaRepository):
        self.marcas_repository = marcas_repository
        self.session = session

    def normalizar_marca(marca: str):
        return marca.upper()

    async def registro_marca_nova(
        self, usuario: UsuarioAutenticado, nome_marca: RegistrandoMarcaRequest
    ):
        nome_marca_normalizado = self.normalizar_marca(nome_marca.nome)

        existe_marca = await self.marcas_repository.buscar_marca_por_nome
        if existe_marca:
            raise HttpException.item_ja_registrado()

        await self.marcas_repository.inserir_nova_marca(nome_marca_normalizado)
        await self.session.commit()

    async def listar_marcas_registradas(self, cursor: int, limite: int):
        lista_marcas = await self.marcas_repository(cursor, limite)
        return lista_marcas
