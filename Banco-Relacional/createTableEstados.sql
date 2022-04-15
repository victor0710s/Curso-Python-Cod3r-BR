-- Criando a tabela estado!

create table estados(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    sigla VARCHAR(2) NOT NULL,
    regiao ENUM('Norte', 'Nordeste', 'Centro-Oeste', 'Sul', 'Sudeste') not null,
    populacao DECIMAL(5,2) NOT NULL,
    PRIMARY key (id),
    unique key (nome),
    unique key (sigla)
);

