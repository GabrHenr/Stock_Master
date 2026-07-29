
CREATE TYPE acesso_tipos AS ENUM ('repositor','estoquista');
CREATE TYPE movimentacoes_tipos AS ENUM ('entrada','saida','ajuste');

CREATE TABLE IF NOT EXISTS marcas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS usuarios (
    id serial PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    contato VARCHAR(255) NOT NULL,
    acesso acesso_tipos NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    marca_id INT NOT NULL REFERENCES marcas(id),
    produto_nome VARCHAR(255) NOT NULL,
    produto_descricao VARCHAR(255) NOT NULL,
    quantidade_minima_unidades INT NOT NULL,
    produto_codigo_barras VARCHAR(100) NOT NULL UNIQUE
);
CREATE INDEX index_produtos_marca_id ON produtos(marca_id);

CREATE TABLE IF NOT EXISTS lotes(
    id SERIAL PRIMARY KEY,
    lote_quantidade_atual INT NOT NULL,
    lote_numero VARCHAR(50) NOT NULL,
    lote_data_registro TIMESTAMPTZ DEFAULT NOW(),
    lote_data_vencimento DATE NOT NULL,
    lote_data_fabricacao DATE NOT NULL,
    produto_id INT NOT NULL REFERENCES produtos(id),

    CHECK(lote_quantidade_atual>=0),
    CHECK (lote_data_vencimento > lote_data_fabricacao),

    UNIQUE(produto_id, lote_numero)
);
CREATE INDEX index_lotes_produto_id ON lotes(produto_id);

CREATE TABLE IF NOT EXISTS movimentacoes_estoque(
    id SERIAL PRIMARY KEY,
    lote_id INT NOT NULL REFERENCES lotes(id),
    usuario_id INT NOT NULL REFERENCES usuarios(id),
    movimentacoes_estoque_tipo movimentacoes_tipos NOT NULL,
    quantidade_unidades INT NOT NULL,
    movimentacoes_estoque_motivo VARCHAR(255) NOT NULL,
    movimentacoes_estoque_data TIMESTAMPTZ DEFAULT NOW(),
    
    CHECK (quantidade_unidades > 0)
);
CREATE INDEX index_movimentacoes_usuario ON movimentacoes_estoque (usuario_id);
CREATE INDEX index_movimentacoes_lote ON movimentacoes_estoque (lote_id);