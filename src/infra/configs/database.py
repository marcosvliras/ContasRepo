from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

host = "localhost"
port = "3306"
database = "contas_database"
user = "root"
password = "1234"

# Criando a string de conexão
connection_string = (
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
)

engine = create_engine(connection_string)
SessionLocal = sessionmaker(bind=engine)
