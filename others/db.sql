create database bancoFlask;
use bancoFlask;

create table person(
nome varchar(100) not null,
apelido varchar(100) not null,
sus bigint(15) not null,
rg int(10) not null,
cpf bigint(11) not null primary key,
nomeDaMae varchar(100) not null,
dataDeNascimento date not null,
sexo varchar(20) not null,
uf varchar(4) not null,
nacionalidade varchar(50) not null,
pais varchar(50) not null,
ler varchar(50) not null,
escolaridade varchar(50) not null,
raca varchar(50) not null,
etnia varchar(50) not null,
religiao varchar(50) not null

) Engine= InnoDB;

select * from person;