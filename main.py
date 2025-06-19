import pyodbc
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Leer variables
driver = os.getenv("DB_DRIVER")
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Crear conexión
try:
    conn = pyodbc.connect(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )
    print("✅ Conexión exitosa a SQL Server")
    conn.close()
except Exception as e:
    print(f"❌ Error de conexión: {e}")
