-- Cria o banco de dados
CREATE DATABASE netflix;

-- Usa o banco de dados criado
USE netflix;

-- Cria a tabela netflix_brazil
CREATE TABLE netflix_brazil (
    sale_date DATE,
    customer VARCHAR(255),
    contracted_plan VARCHAR(255),
    amount DECIMAL(10, 2),
    age INT,
    utm_link VARCHAR(255)
);

-- Cria a tabela netflix_france
CREATE TABLE netflix_france (
    sale_date DATE,
    customer VARCHAR(255),
    contracted_plan VARCHAR(255),
    amount DECIMAL(10, 2),
    age INT,
    utm_link VARCHAR(255)
);

-- Cria a tabela netflix_italia
CREATE TABLE netflix_italia (
    sale_date DATE,
    customer VARCHAR(255),
    contracted_plan VARCHAR(255),
    amount DECIMAL(10, 2),
    age INT,
    utm_link VARCHAR(255)
);