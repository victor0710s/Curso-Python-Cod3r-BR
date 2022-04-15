ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

insert into empresas 
    (nome, cnpj)
values
    ('Bradesco', 22438894000139),
    ('Vale', 37901351000183),
    ('Cielo', 42550794000107);

desc empresas;
desc prefeitos;
select * from empresas;

INSERT INTO empresas_unidades 
    (empresa_id, cidade_id, sede)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);

select * from empresas_unidades;