select e.nome Empresa, c.nome Cidade
from empresas e, empresas_unidades eu, cidades c
where c.id = eu.cidade_id
and e.id = eu.empresa_id;