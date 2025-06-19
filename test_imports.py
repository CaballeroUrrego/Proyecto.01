try:
    import pyodbc
    print("✅ pyodbc importado correctamente")
except ImportError as e:
    print("❌ Error con pyodbc:", e)

try:
    import dotenv
    print("✅ dotenv importado correctamente")
except ImportError as e:
    print("❌ Error con dotenv:", e)
