from pwdlib import PasswordHash

class ServicosSenha:
    senha_hash = PasswordHash.recommended()
    @staticmethod
    def verificar_senha(senha:str,senha_encriptada:str):
        return ServicosSenha.senha_hash.verify(senha,senha_encriptada)
    @staticmethod
    def gerar_senha(senha:str):
        return ServicosSenha.senha_hash.hash(senha)