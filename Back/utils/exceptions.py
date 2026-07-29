from fastapi import HTTPException

class HttpException:
    @staticmethod
    def usuario_ou_senha_incorretos():
        return HTTPException(
            status_code= 401,
            detail= "Senha ou usuário incorretos"
        )
