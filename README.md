

# Projeto: Criar um Servidor com MySQL Dados Netflix

**Autor:** João Henrique  
**Instagram:** [@jhenriqueorginal](https://www.instagram.com/jhenriqueorginal)

## Descrição do Projeto

Este projeto tem como objetivo criar um servidor MySQL e configurar um banco de dados chamado `netflix` com tabelas específicas para armazenar dados de diferentes países. As tabelas são `netflix_brazil`, `netflix_france` e `netflix_italia`.

## Estrutura do Banco de Dados

### Banco de Dados: `netflix`

O banco de dados `netflix` contém três tabelas, cada uma destinada a armazenar dados de um país específico.

### Tabelas

#### Tabela: `netflix_brazil`

| Coluna            | Tipo         | Descrição                          |
|-------------------|--------------|------------------------------------|
| `sale_date`       | DATE         | Data da venda                      |
| `customer`        | VARCHAR(255) | Nome do cliente                    |
| `contracted_plan` | VARCHAR(255) | Plano contratado                   |
| `amount`          | DECIMAL(10,2)| Valor do plano                     |
| `age`             | INT          | Idade do cliente                   |
| `utm_link`        | VARCHAR(255) | Link de origem do cliente          |

#### Tabela: `netflix_france`

| Coluna            | Tipo         | Descrição                          |
|-------------------|--------------|------------------------------------|
| `sale_date`       | DATE         | Data da venda                      |
| `customer`        | VARCHAR(255) | Nome do cliente                    |
| `contracted_plan` | VARCHAR(255) | Plano contratado                   |
| `amount`          | DECIMAL(10,2)| Valor do plano                     |
| `age`             | INT          | Idade do cliente                   |
| `utm_link`        | VARCHAR(255) | Link de origem do cliente          |

#### Tabela: `netflix_italia`

| Coluna            | Tipo         | Descrição                          |
|-------------------|--------------|------------------------------------|
| `sale_date`       | DATE         | Data da venda                      |
| `customer`        | VARCHAR(255) | Nome do cliente                    |
| `contracted_plan` | VARCHAR(255) | Plano contratado                   |
| `amount`          | DECIMAL(10,2)| Valor do plano                     |
| `age`             | INT          | Idade do cliente                   |
| `utm_link`        | VARCHAR(255) | Link de origem do cliente          |


Claro, aqui está a documentação para o seu script Python 

## Estrutura do Script

### Bibliotecas Utilizadas

pandas

: Utilizada para manipulação e leitura dos arquivos Excel.

sqlalchemy

: Utilizada para criar a conexão com o banco de dados MySQL e inserir os dados nas tabelas.


### Importação dos Dados

O script lê os dados dos arquivos Excel e os insere nas tabelas correspondentes no banco de dados MySQL. Os nomes das colunas são normalizados para evitar problemas de formatação.

## Código Python

```python
import pandas as pd
from sqlalchemy import create_engine



# Importar os dados para as tabelas correspondentes
for table_name, file_path in excel_files.items():
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')  # Normalizar os nomes das colunas
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Dados importados com sucesso para a tabela {table_name}!")
```

Se precisar de mais alguma coisa, estou à disposição.
