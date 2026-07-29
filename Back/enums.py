
from enum import Enum

class AcessoTipos(str,Enum):
    REPOSITOR = 'repositor'
    ESTOQUISTA = 'estoquista'

class MovimentacoesTipos(str,Enum):
    ENTRADA = 'entrada'
    SAIDA = 'saida'
    AJUSTE = 'ajuste'
