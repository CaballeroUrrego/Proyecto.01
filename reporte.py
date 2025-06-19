import pandas as pd
import pyodbc
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Leer variables
driver = os.getenv("DB_DRIVER")
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

print("🔍 Variables cargadas:")
print(f"DRIVER: {driver}")
print(f"SERVER: {server}")
print(f"DATABASE: {database}")
print(f"USER: {username}")

# Intentar conexión
try:
    conn = pyodbc.connect(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
    )
    print("✅ Conexión exitosa a SQL Server")

    # Consulta a la base de datos
    query = "SELECT * FROM usuarios;"  # Cambia esta línea si necesitas otro reporte

    df = pd.read_sql(query, conn)

    # Crear carpeta si no existe
    os.makedirs("reportes", exist_ok=True)

    # Guardar el archivo
    df.to_csv("reportes/reporte_usuarios.csv", index=False)
    df.to_excel("reportes/reporte_usuarios.xlsx", index=False)

    print("📁 Reportes guardados en carpeta 'reportes/'")
    conn.close()

except Exception as e:
    print(f"❌ Error de conexión o consulta: {e}")
