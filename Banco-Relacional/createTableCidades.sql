create table if not exists cidades(
    id int unsigned not null auto_increment,
    nome varchar(255) not null,
    estado_id int unsigned not null,
    area DECIMAL(10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (estado_id) REFERENCES estados (id)
);

-- create table if not exists TESTEs (
--     id int unsigned not null auto_increment PRIMARY KEY
-- );

-- drop table if exists testes;