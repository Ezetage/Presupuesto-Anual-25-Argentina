import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from transform.transform_data_to_df import transform_data
from sqlalchemy import create_engine

# Configuración de SQLAlchemy
DB_USER = "user"
DB_PASS = "password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "presupuesto2025"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Cargar los DataFrames desde el módulo de transformación
df_jurisdiccion, df_subjurisdiccion, df_entidad, df_obra = transform_data()

# Guardar en la base de datos
df_jurisdiccion.to_sql("jurisdiccion", engine, if_exists="append", index=False)
df_subjurisdiccion.to_sql("subjurisdiccion", engine, if_exists="append", index=False)
df_entidad.to_sql("entidad", engine, if_exists="append", index=False)
df_obra.to_sql("obra", engine, if_exists="append", index=False)

print("✅ Datos cargados correctamente en todas las tablas")