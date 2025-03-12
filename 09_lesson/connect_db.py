from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:111@localhost:5432/QA"
engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Успешное подключение к базе данных!")
    connection.close()
except Exception as e:
    print(f"Ошибка подключения: {e}")
