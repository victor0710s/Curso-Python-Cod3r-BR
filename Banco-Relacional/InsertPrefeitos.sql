select *from cidades;

insert into prefeitos 
    (nome, cidade_id)
values 
    ('Rodrigo Neves', 2),
    ('Raquel Lyra', 3),
    ('Zenaldo Coutinho', null);

select * from prefeitos;

INSERT INTO prefeitos 
    (nome, cidade_id)
VALUES
    ('Rafael Greca', null);

INSERT INTO prefeitos
    (nome, cidade_id)
values
    ('Rodrigo Pinheiro', 3)