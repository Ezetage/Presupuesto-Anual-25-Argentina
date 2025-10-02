import requests
import os

# Configuración
URL = "https://www.presupuestoabierto.gob.ar/api/v1/credito"
OUTPUT_DIR = "raw_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {
    "Authorization": "a587ae7f-7123-4ed1-991a-2eb5d9127962",
    "Content-Type": "application/json"
}

COLUMNS = [
    "impacto_presupuestario_anio",
    "impacto_presupuestario_mes",
    "jurisdiccion_desc",
    "subjurisdiccion_desc",
    "entidad_desc",
    "obra_desc",
    "credito_presupuestado",
    "credito_vigente",
    "credito_comprometido",
    "credito_devengado",
    "credito_pagado",
    "ultima_actualizacion_fecha"
]

BODY = {
    "title": "Credito vigente 2025",
    "columns": COLUMNS
}

def extract_data():
    print("📥 Descargando datos crudos del Presupuesto 2025...")
    try:
        response = requests.post(URL, headers=HEADERS, json=BODY)
        response.raise_for_status()
        output_file = os.path.join(OUTPUT_DIR, "credito_vigente_2025.csv")
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"✅ Archivo guardado en {output_file}")
    except Exception as e:
        print(f"❌ Error al descargar datos: {e}")
