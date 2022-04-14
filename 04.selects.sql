/* a. Produza um relatório que contenha os dados dos alunos matriculados em todos os
cursos oferecidos pela escola. */

SELECT a.nome, a.cpf_id as CPF, c.nome as Curso, d.nome as Departamento
FROM matricula as m
INNER JOIN aluno as a
ON a.cpf_id = m.cpf_aluno 
INNER JOIN curso as c
ON m.codigo_curso = c.curso_id
INNER JOIN departamento as d
ON d.departamento_id = c.codigo_depto
ORDER BY a.nome;


/* 
b. Produza um relatório com os dados de todos os cursos, com suas respectivas
disciplinas, oferecidos pela escola.
*/

SELECT c.nome as Curso,d.nome as Disciplina 
FROM compoe as co
INNER JOIN curso as c
ON c.curso_id = co.codigo_curso
INNER JOIN disciplina as d
ON d.disciplina_id = co.codigo_disciplina;


/* 
c. Produza um relatório que contenha o nome dos alunos e as disciplinas em que estão
matriculados.
*/

SELECT a.nome as Aluno, d.nome as Disciplina
FROM cursa as c
INNER JOIN aluno as a
ON c.cpf_aluno = a.cpf_id
INNER JOIN disciplina as d
ON c.codigo_disciplina = d.disciplina_id
ORDER BY Aluno;

/*
d. Produza um relatório com os dados dos professores e as disciplinas que ministram.
*/


/* 
e. Produza um relatório com os nomes das disciplinas e seus pré-requisitos.
*/

SELECT d.nome, r.nome
FROM pre_requisito p 
INNER JOIN disciplina d 
JOIN (SELECT * FROM disciplina) r 
WHERE p.codigo_disciplina = d.disciplina_id and p.codigo_dependencia = r.disciplina_id order by d.nome, r.nome;

/*
f. Produza um relatório com a média de idade dos alunos matriculados em cada curso.
*/

/*
g. Produza um relatório com os cursos oferecidos por cada departamento.
*/

SELECT d.nome as Departamento, c.nome as Curso 
FROM departamento as d
JOIN curso as c
WHERE d.departamento_id = c.codigo_depto
ORDER BY d.nome;