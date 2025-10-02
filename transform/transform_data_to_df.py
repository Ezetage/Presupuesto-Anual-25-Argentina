import pandas as pd
import os
import calendar

RAW_CSV = "raw_data/credito_vigente_2025.csv"

def transform_data():
    try:
        if not os.path.exists(RAW_CSV):
            raise FileNotFoundError(f"No se encontró el CSV crudo en {RAW_CSV}")
        df_raw = pd.read_csv(RAW_CSV)

        # Crear columna mes como fecha (primer día del mes)
        if "impacto_presupuestario_anio" in df_raw.columns and "impacto_presupuestario_mes" in df_raw.columns:
            df_raw["mes_date"] = pd.to_datetime(
                df_raw["impacto_presupuestario_anio"].astype(str) + "-" +
                df_raw["impacto_presupuestario_mes"].astype(str) + "-01",
                errors="coerce"
            )
            meses_es = {
                1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
                7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
            }
            df_raw["mes_nombre"] = df_raw["impacto_presupuestario_mes"].map(meses_es)

        columnas_base = [
            "mes_date", "impacto_presupuestario_anio", "impacto_presupuestario_mes", "mes_nombre",
            "credito_presupuestado", "credito_vigente",
            "credito_comprometido", "credito_devengado", "credito_pagado"
        ]
        df_jurisdiccion = df_raw[columnas_base + ["jurisdiccion_desc"]].copy()
        df_subjurisdiccion = df_raw[columnas_base + ["subjurisdiccion_desc"]].copy()
        df_entidad = df_raw[columnas_base + ["entidad_desc"]].copy()
        df_obra = df_raw[columnas_base + ["obra_desc"]].copy()
        print("✅ Transformación completada: 4 DataFrames listos")
        return df_jurisdiccion, df_subjurisdiccion, df_entidad, df_obra
    except Exception as e:
        print(f"❌ Error en la transformación de datos: {e}")
        raise