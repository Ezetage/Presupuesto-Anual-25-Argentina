import os
import time
from sqlalchemy import create_engine
from create.create_tables import create_tables
from extract.get_data import extract_data
from transform.transform_data_to_df import transform_data
from load.load_data import load_data

# -------------------------------
# Configuración desde variables de entorno o defaults
# -------------------------------
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "password")
DB_HOST = os.getenv("DB_HOST", "postgres_presupuesto")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "presupuesto2025")

def wait_for_postgres(host, port, user, password, dbname, retries=10, delay=3):
    from psycopg2 import connect, OperationalError
    attempt = 0
    while attempt < retries:
        try:
            conn = connect(
                host=host,
                port=port,
                user=user,
                password=password,
                dbname=dbname
            )
            conn.close()
            print("✅ PostgreSQL está listo")
            return
        except OperationalError as e:
            attempt += 1
            print(f"⏳ Esperando PostgreSQL... intento {attempt}/{retries} ({e})")
            time.sleep(delay)
    raise Exception("❌ PostgreSQL no está disponible después de varios intentos")

def main():
    # 1. Esperar a que PostgreSQL esté listo
    wait_for_postgres(DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME)

    # 2. Crear engine y tablas
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    create_tables(engine)

    # 3. Extraer datos crudos
    extract_data()

    # 4. Transformar datos
    df_jurisdiccion, df_subjurisdiccion, df_entidad, df_obra = transform_data()

    # 5. Cargar datos
    load_data(engine, df_jurisdiccion, df_subjurisdiccion, df_entidad, df_obra)


    print("🎉 Pipeline finalizado correctamente")

if __name__ == "__main__":
    main()