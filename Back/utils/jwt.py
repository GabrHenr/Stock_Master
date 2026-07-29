import datetime as dt
from fastapi import HTTPException
from dotenv import load_dotenv
import os
import jwt


class ServicosJwt:
    load_dotenv()
    @staticmethod
    def criar_jwt(tipo,email,id:int):
        dados = {"tipo":tipo, "email": email, "id": id}
        expire = dt.datetime.now(tz=dt.timezone.utc) + dt.timedelta(
            minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))
        )
        dados.update({"exp": expire})
        jwt_codificado = jwt.encode(dados,os.getenv("JWT_SECRET_KEY"),algorithm=os.getenv("JWT_ALGORITHM"))
        return jwt_codificado
    @staticmethod
    def validar_e_retornar_dados_jwt(dados_para_validar):
        try:
            dados:dict = jwt.decode(dados_para_validar,os.getenv("JWT_SECRET_KEY"),algorithms=[os.getenv("JWT_ALGORITHM")])
        except:
            raise HTTPException(status_code=401, detail="Token Expirado")
        return dados
    pass
