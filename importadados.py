import pandas as pd
from sqlalchemy import create_engine

# Caminhos dos arquivos Excel
excel_files = {
    'netflix_brazil': r'C:\Users\Pamela e Rick\Documents\Projeto_Analise_de_Dados\Src\brazil.xlsx',
    'netflix_france': r'C:\Users\Pamela e Rick\Documents\Projeto_Analise_de_Dados\Src\france.xlsx',
    'netflix_italia': r'C:\Users\Pamela e Rick\Documents\Projeto_Analise_de_Dados\Src\italia.xlsx'
}

# Criar conexão com o banco de dados MySQL
server = '127.0.0.1'
port = '3306'
database = 'netflix'
username = 'root'
password = '03122003'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{server}:{port}/{database}')

# Importar os dados para as tabelas correspondentes
for table_name, file_path in excel_files.items():
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')  # Normalizar os nomes das colunas
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Dados importados com sucesso para a tabela {table_name}!")