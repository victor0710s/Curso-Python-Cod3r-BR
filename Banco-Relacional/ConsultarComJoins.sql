-- Codigo feito no WorkBench por conta de limitação do plugin no Vs.

select * from prefeitos;
select * from cidades;

select * from cidades c inner join prefeitos p on c.id = p.cidade_id;
select * from cidades c left outer join prefeitos p on c.id = p.cidade_id; -- Usar o outer ou não leva ao mesmo resultado!!
select * from cidades c right join prefeitos p on c.id = p.cidade_id;

-- O SQL tem uma limitação onde nao se consegue usar o full joinmas abaixo a um exemplo de como simular o mesmo!
select * from cidades c right join prefeitos p on c.id = p.cidade_id
union
select * from cidades c left outer join prefeitos p on c.id = p.cidade_id;