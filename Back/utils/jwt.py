import datetime as dt
import jwt
from enums import AcessoTipos
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 15
JWT_SECRET_KEY = "Aksjdiawnjnakhsbyabwjkmcio19028dshaiudnad"
JWT_ALGORITHM = "HS256"
class ServicosJWT:
    @staticmethod
    def criar_jwt(acesso:AcessoTipos, email:str, id:int):
        dados:dict = {"acesso":acesso, "email": email, "id":id}
        expire = dt.datetime.now(tz=dt.timezone.utc)+ dt.timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        dados.update({"exp": expire})
        jwt_codificado = jwt.encode(dados,JWT_SECRET_KEY,JWT_ALGORITHM)
        return jwt_codificado
    @staticmethod
    def jwt_validar_e_retornar_dados(jwt_para_validar):
        try:
            dados:dict = jwt.decode(jwt_para_validar,JWT_SECRET_KEY,[JWT_ALGORITHM])
        except:
            raise
        return dados    
        