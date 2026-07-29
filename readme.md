E sinceramente? Você está fazendo a pergunta certa na hora certa.

A maior parte dos problemas de arquitetura em FastAPI acontece porque a pessoa já começa criando “classes para tudo” sem entender o papel de cada camada. Como você quer aprofundar FastAPI (e ainda vem do contexto de engenharia/POO), vou te passar as dicas que eu gostaria de ter recebido no meu primeiro projeto sério.

### Regra de ouro: pense em “quem sabe o quê”

### `main.py` → “montador”

Não sabe regra de negócio. Só monta a aplicação.

Python

Run

```
app = FastAPI()
app.include_router(usuario_router)
```

Ele é o equivalente ao `main()` do C/C++.

### `routes.py` → “tradutor HTTP”

Recebe HTTP → chama serviço → devolve HTTP.

Python

Run

```
@router.post('/')
async def criar_usuario(dados: UsuarioCreate):
    return await service.criar(dados)
```

Essa camada não deve:

* abrir conexão com banco

* escrever SQL

* fazer regra de negócio complexa

* validar permissões complicadas

Ela só traduz o mundo HTTP.

### `schemas.py` → “contrato”

Aqui entra o Pydantic.

Python

Run

```
class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
```

Pensa nele como:

“Qual formato de dados entra e sai da API?”

Ele não é “classe de negócio”. É um DTO/contrato.

### `services.py` → “cérebro”

Aqui fica a regra.

Python

Run

```
class UsuarioService:

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    async def criar(self, dados: UsuarioCreate):
        if await self.repo.buscar_por_email(dados.email):
            raise ValueError('E-mail já cadastrado')

        return await self.repo.criar(dados)
```

Tudo que você escrever aqui deveria funcionar mesmo sem FastAPI.

Essa é a camada mais importante.

### `repositories.py` → “mãos”

Só conversa com o banco.

Python

Run

```
class UsuarioRepository:

    async def buscar_por_email(self, email: str):
        stmt = select(Usuario).where(Usuario.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
```

Percebe a diferença?

* Service → “pode cadastrar?”

* Repository → “como buscar no PostgreSQL?”

### Estrutura que eu usaria HOJE

Para um projeto pequeno/médio:

### Estrutura recomendada

Escala bem sem virar over-engineering

app/

`main.py`

`database.py`

usuarios/

`routes.py`

`schemas.py`

`services.py`

`repositories.py`

`models.py`

Isso é praticamente o que você acabou usando no Avisos Escolares — então você já está no caminho certo.

### Dependency Injection: o jeito “FastAPI”

Em vez de criar o service na mão dentro da rota:

❌

Python

Run

```
repo = UsuarioRepository(session)
service = UsuarioService(repo)
```

Use dependências.

### Dependência do banco

Python

Run

```
async def get_session():
    async with SessionLocal() as session:
        yield session
```

### Dependência do repositório

Python

Run

```
def get_usuario_repository(
    session: AsyncSession = Depends(get_session)
):
    return UsuarioRepository(session)
```

### Dependência do serviço

Python

Run

```
def get_usuario_service(
    repo: UsuarioRepository = Depends(get_usuario_repository)
):
    return UsuarioService(repo)
```

### Na rota

Python

Run

```
@router.post('/')
async def criar_usuario(
    dados: UsuarioCreate,
    service: UsuarioService = Depends(get_usuario_service)
):
    return await service.criar(dados)
```

Isso parece mais verboso no começo, mas ganha:

* testes fáceis

* troca de implementação

* menos acoplamento

* reaproveitamento

### Erro clássico de iniciante (você quase evitou)

### Colocar `HTTPException` no Repository

Você mesmo comentou isso no projeto anterior.

❌ Errado:

Python

Run

```
class UsuarioRepository:
    async def buscar(self, id: int):
        usuario = ...
        if not usuario:
            raise HTTPException(404, 'Usuário não encontrado')
```

O repository agora “sabe” que existe HTTP.

✅ Melhor:

Python

Run

```
class UsuarioRepository:
    async def buscar(self, id: int):
        return usuario
```

E o service decide:

Python

Run

```
usuario = await repo.buscar(id)

if not usuario:
    raise UsuarioNaoEncontrado()
```

A rota converte para HTTP.

Isso é arquitetura limpa na prática.

### Como eu começo TODO projeto FastAPI

### Checklist de bootstrap

Criar database.py (engine + SessionLocal)

Criar main.py

Criar pasta do domínio (usuarios/)

Criar schemas.py primeiro

Criar model do SQLAlchemy

Criar repository

Criar service

Criar route por último

💡 Ordem importante: Schema → Model → Repository → Service → Route.

Porque a rota depende de tudo; começar por ela costuma gerar retrabalho.

### Um “teste de arquitetura” de 10 segundos

Pergunte:

“Se amanhã eu trocar FastAPI por Flask, o que quebra?”

* `routes.py` → quebra (normal)

* `schemas.py` → talvez ajuste

* `services.py` → não deveria quebrar

* `repositories.py` → não deveria quebrar (se continuar usando SQLAlchemy)

Se service e repository sobrevivem à troca de framework, sua separação de responsabilidades está muito boa.

E como você quer aprofundar FastAPI “do jeito profissional”, o próximo assunto que mais vale estudar é lifespan + dependency injection + gerenciamento de sessão async do SQLAlchemy (é exatamente o trio que diferencia um CRUD de tutorial de uma API pronta para produção).
