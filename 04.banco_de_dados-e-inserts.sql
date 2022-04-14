

DROP TABLE IF EXISTS `aluno`;

CREATE TABLE `aluno` (
  `cpf_id` char(11) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `endereco` varchar(45) DEFAULT NULL,
  `telefone` varchar(12) DEFAULT NULL,
  `data_nasc` date DEFAULT NULL,
  PRIMARY KEY (`cpf_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


LOCK TABLES `aluno` WRITE;
INSERT INTO `aluno` VALUES ('120','Pedro','Rua 48','8812','1983-02-12'),('121','Bruna','Rua 48','3321','1983-06-29'),('122','Carlos','Rua 48','8812','1980-01-13'),('123','Washington','Rua 47','9871','1973-04-17'),('124','Laura','Rua 27','7331','1987-03-22'),('125','João','Rua 13','9131','1945-12-02'),('126','Bruno','Rua 13','9131','1967-04-21'),('127','Paula','Rua 51','2123','2002-12-13'),('128','Meire','Rua 13','8221','1991-12-25'),('129','Maria','Rua 48','0988','2000-08-13');
UNLOCK TABLES;


DROP TABLE IF EXISTS `compoe`;
CREATE TABLE `compoe` (
  `codigo_curso` char(5) NOT NULL,
  `codigo_disciplina` char(5) NOT NULL,
  KEY `codigo_curso_idx` (`codigo_curso`),
  KEY `codigo_disciplina_idx` (`codigo_disciplina`),
  CONSTRAINT `codigo_curso` FOREIGN KEY (`codigo_curso`) REFERENCES `curso` (`curso_id`),
  CONSTRAINT `codigo_disciplina` FOREIGN KEY (`codigo_disciplina`) REFERENCES `disciplina` (`disciplina_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

LOCK TABLES `compoe` WRITE;
INSERT INTO `compoe` VALUES ('00501','50001'),('00501','50002'),('00501','50003'),('00501','50004'),('00501','50005'),('00501','50006'),('00501','50007'),('00501','50008'),('00501','50009'),('00501','50010');
UNLOCK TABLES;


DROP TABLE IF EXISTS `cursa`;
CREATE TABLE `cursa` (
  `cpf_aluno` char(11) NOT NULL,
  `codigo_disciplina` char(5) NOT NULL,
  KEY `cpf_id_idx` (`cpf_aluno`),
  KEY `codigo_curso_id_idx` (`codigo_disciplina`),
  CONSTRAINT `codigo_curso_id` FOREIGN KEY (`codigo_disciplina`) REFERENCES `disciplina` (`disciplina_id`),
  CONSTRAINT `cpf_id` FOREIGN KEY (`cpf_aluno`) REFERENCES `aluno` (`cpf_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

LOCK TABLES `cursa` WRITE;
INSERT INTO `cursa` VALUES ('120','50001'),('123','50001'),('125','50001'),('127','50001'),('129','50001'),('121','50001'),('122','50009'),('124','50009'),('126','50009'),('128','50009');
UNLOCK TABLES;


DROP TABLE IF EXISTS `curso`;
CREATE TABLE `curso` (
  `curso_id` char(5) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `codigo_depto` char(5) NOT NULL,
  PRIMARY KEY (`curso_id`),
  KEY `departamento_id_idx` (`codigo_depto`),
  CONSTRAINT `departamento_id` FOREIGN KEY (`codigo_depto`) REFERENCES `departamento` (`departamento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

LOCK TABLES `curso` WRITE;
INSERT INTO `curso` VALUES ('00101','Engenharia Civil','Engenharia Civil','61001'),('00201','Linguistica Aplicada','Linguistica Aplicada','61002'),('00301','UX/IU Design','UX/IU Design','61003'),('00401','Física Aplicada','Física Aplicada','61004'),('00501','Desenvolve 40+ Magalu','Desenvolve 40+ Magalu','61005');
UNLOCK TABLES;


DROP TABLE IF EXISTS `departamento`;

CREATE TABLE `departamento` (
  `departamento_id` char(5) NOT NULL,
  `nome` varchar(45) NOT NULL,
  PRIMARY KEY (`departamento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


LOCK TABLES `departamento` WRITE;
INSERT INTO `departamento` VALUES ('61001','Departamento de Engenharia'),('61002','Departamento de Letras'),('61003','Departamento de Design'),('61004','Departamento de Física'),('61005','Let\'s Code');
UNLOCK TABLES;


DROP TABLE IF EXISTS `disciplina`;

CREATE TABLE `disciplina` (
  `disciplina_id` char(5) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `qtde_creditos` int DEFAULT NULL,
  `matricula_prof` char(5) NOT NULL,
  PRIMARY KEY (`disciplina_id`),
  KEY `matricula_id_idx` (`matricula_prof`),
  CONSTRAINT `matricula_id` FOREIGN KEY (`matricula_prof`) REFERENCES `professor` (`matricula_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


LOCK TABLES `disciplina` WRITE;
INSERT INTO `disciplina` VALUES ('50001','Calculo I',24,'99005'),('50002','Calculo II',24,'99005'),('50003','Modelagem',24,'99002'),('50004','Algoritmos',24,'99002'),('50005','Estrutura de Dados',24,'99003'),('50006','Grafos',24,'99003'),('50007','Data Driven',24,'99001'),('50008','SQL',24,'99001'),('50009','Programação Orientada à Objeto I',24,'99004'),('50010','Programação Orientada à Objeto II',24,'99005');
UNLOCK TABLES;


DROP TABLE IF EXISTS `matricula`;

CREATE TABLE `matricula` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cpf_aluno` char(11) NOT NULL,
  `codigo_curso` char(5) NOT NULL,
  `data_matricula` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `curso_id_idx` (`codigo_curso`),
  KEY `teste_idx` (`cpf_aluno`),
  CONSTRAINT `codigo_id` FOREIGN KEY (`cpf_aluno`) REFERENCES `aluno` (`cpf_id`),
  CONSTRAINT `curso_id` FOREIGN KEY (`codigo_curso`) REFERENCES `curso` (`curso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;


LOCK TABLES `matricula` WRITE;
INSERT INTO `matricula` VALUES (1,'120','00501','2022-01-01'),(10,'121','00501','2022-01-01'),(11,'122','00501','2022-01-01'),(12,'123','00501','2022-01-01'),(13,'124','00501','2022-01-01'),(14,'125','00501','2022-02-01'),(15,'126','00501','2022-02-01'),(16,'127','00501','2022-02-01'),(17,'128','00501','2022-02-01');
UNLOCK TABLES;


DROP TABLE IF EXISTS `pre_requisito`;
CREATE TABLE `pre_requisito` (
  `codigo_disciplina` char(5) NOT NULL,
  `codigo_dependencia` char(5) NOT NULL,
  KEY `disciplina_id_de_idx` (`codigo_dependencia`),
  KEY `disciplina_id_di_idx` (`codigo_disciplina`),
  CONSTRAINT `disciplina_id_de` FOREIGN KEY (`codigo_dependencia`) REFERENCES `disciplina` (`disciplina_id`),
  CONSTRAINT `disciplina_id_di` FOREIGN KEY (`codigo_disciplina`) REFERENCES `disciplina` (`disciplina_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


LOCK TABLES `pre_requisito` WRITE;
INSERT INTO `pre_requisito` VALUES ('50002','50001'),('50010','50009'),('50002','50007'),('50010','50007'),('50004','50007'),('50008','50007');
UNLOCK TABLES;


DROP TABLE IF EXISTS `professor`;
CREATE TABLE `professor` (
  `matricula_id` char(5) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `endereco` varchar(45) DEFAULT NULL,
  `telefone` varchar(12) DEFAULT NULL,
  `data_nasc` date DEFAULT NULL,
  `data_contratacao` date DEFAULT NULL,
  `codigo_depto` char(5) NOT NULL,
  PRIMARY KEY (`matricula_id`),
  KEY `departamento_id_pr_idx` (`codigo_depto`),
  CONSTRAINT `departamento_id_pr` FOREIGN KEY (`codigo_depto`) REFERENCES `departamento` (`departamento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


LOCK TABLES `professor` WRITE;
INSERT INTO `professor` VALUES ('99001','Matheus','Rua 123','8892','1975-12-22','2002-01-01','61005'),('99002','Fernando','Rua 773','9112','1980-12-22','2005-04-01','61005'),('99003','Brian','Rua 433','7811','1980-12-12','2007-05-01','61005'),('99004','Paulo','Rua 322','9443','1982-01-23','2009-12-01','61005'),('99005','Rafael','Rua 831','8912','1978-06-05','2012-10-01','61005');
UNLOCK TABLES;