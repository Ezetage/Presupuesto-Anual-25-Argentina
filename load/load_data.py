from sqlalchemy.engine import Engine

def load_data(engine: 'Engine', df_jurisdiccion, df_subjurisdiccion, df_entidad, df_obra):
    """
    Carga los DataFrames en las tablas correspondientes usando el engine provisto.
    """
    try:
        df_jurisdiccion.to_sql("jurisdiccion", engine, if_exists="append", index=False)
        df_subjurisdiccion.to_sql("subjurisdiccion", engine, if_exists="append", index=False)
        df_entidad.to_sql("entidad", engine, if_exists="append", index=False)
        df_obra.to_sql("obra", engine, if_exists="append", index=False)
        print("✅ Datos cargados correctamente en todas las tablas")
    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")