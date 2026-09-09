from sqlalchemy.ext.asyncio import AsyncSession
from models import Marcas
from sqlalchemy import select


class MarcaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def inserir_nova_marca(self, nome_marca: str):
        marca_para_insercao = Marcas(nome_marca)
        self.session.add(marca_para_insercao)

    async def buscar_marca_por_nome(self, nome_marca: str):
        statement = select(Marcas).where(Marcas.nome == nome_marca)
        resultado = await self.session.execute(statement)
        return resultado.scalar_one_or_none()

    async def buscar_lista_marcas(self, cursor: int, limite: int):
        statement = select(Marcas).order_by(Marcas.id).limit(limite)
        if cursor:
            statement = statement.where(Marcas.id > cursor)
        resultado = await self.session.execute(statement)
        lista_marcas = resultado.scalars().all()
        return lista_marcas
