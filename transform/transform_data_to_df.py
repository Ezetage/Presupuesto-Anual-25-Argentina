# transform.py
import pandas as pd
import os

RAW_CSV = "raw_data/credito_vigente_2025.csv"

def transform_data():
    # Verificamos que exista el archivo crudo
    if not os.path.exists(RAW_CSV):
        raise FileNotFoundError(f"No se encontró el CSV crudo en {RAW_CSV}")

    # Leemos el CSV crudo
    df_raw = pd.read_csv(RAW_CSV)

    # Convertimos la fecha a tipo datetime
    if "impacto_presupuestario_fecha" in df_raw.columns:
        df_raw["impacto_presupuestario_fecha"] = pd.to_datetime(df_raw["impacto_presupuestario_fecha"], errors='coerce')

    # ---------- Crear DataFrames para cada tabla ----------
    df_jurisdiccion = df_raw[[
        "impacto_presupuestario_fecha", "impacto_presupuestario_anio", "impacto_presupuestario_mes",
        "jurisdiccion_desc", "credito_presupuestado", "credito_vigente",
        "credito_comprometido", "credito_devengado", "credito_pagado"
    ]].copy()

    df_subjurisdiccion = df_raw[[
        "impacto_presupuestario_fecha", "impacto_presupuestario_anio", "impacto_presupuestario_mes",
        "subjurisdiccion_desc", "credito_presupuestado", "credito_vigente",
        "credito_comprometido", "credito_devengado", "credito_pagado"
    ]].copy()

    df_entidad = df_raw[[
        "impacto_presupuestario_fecha", "impacto_presupuestario_anio", "impacto_presupuestario_mes",
        "entidad_desc", "credito_presupuestado", "credito_vigente",
        "credito_comprometido", "credito_devengado", "credito_pagado"
    ]].copy()

    df_obra = df_raw[[
        "impacto_presupuestario_fecha", "impacto_presupuestario_anio", "impacto_presupuestario_mes",
        "obra_desc", "credito_presupuestado", "credito_vigente",
        "credito_comprometido", "credito_devengado", "credito_pagado"
    ]].copy()

    print("✅ Transformación completada: 4 DataFrames listos")

    return df_jurisdiccion, df_subjurisdiccion, df_entidad, df_obra


if __name__ == "__main__":
    df_jurisdiccion, df_subjurisdiccion, df_entidad, df_obra = transform_data()
    # Podemos ver un resumen rápido
    print("Jurisdicción:", df_jurisdiccion.shape)
    print("Subjurisdicción:", df_subjurisdiccion.shape)
    print("Entidad:", df_entidad.shape)
    print("Obra:", df_obra.shape)