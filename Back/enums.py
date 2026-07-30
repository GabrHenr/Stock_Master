
from enum import Enum

class AcessoTipos(str,Enum):
    repositor = 'repositor'
    estoquista = 'estoquista'

class MovimentacoesTipos(str,Enum):
    entrada = 'entrada'
    saida = 'saida'
    ajuste = 'ajuste'
