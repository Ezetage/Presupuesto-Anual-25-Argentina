import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from tabulate import tabulate

def get_engine():
    return create_engine(
        f"postgresql+psycopg2://{os.getenv('DB_USER', 'user')}:{os.getenv('DB_PASS', 'password')}@"
        f"{os.getenv('DB_HOST', 'postgres_presupuesto')}:{os.getenv('DB_PORT', 5432)}/{os.getenv('DB_NAME', 'presupuesto2025')}"
    )

def print_df(title, query, engine):
    df = pd.read_sql_query(query, engine)
    print("\n" + "="*80)
    print(f"{title.upper()}\n")
    if not df.empty:
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False, floatfmt=",.2f"))
        # Mostrar totales claros si corresponde
        cols_sum = [col for col in df.columns if col.lower() in ("presupuestado","vigente","devengado","pagado")]
        if cols_sum:
            totales = df[cols_sum].sum()
            print("\nTotales:")
            for col in cols_sum:
                print(f"  {col}: {totales[col]:,.2f}")
    else:
        print("No hay datos para mostrar.")
    print("-"*80)

def main():
    engine = get_engine()
    # Definir consultas y títulos
    consultas = [
        ("Total general 2025", '''SELECT 
            SUM(credito_presupuestado) AS Presupuestado,
            SUM(credito_vigente) AS Vigente,
            SUM(credito_devengado) AS Devengado,
            SUM(credito_pagado) AS Pagado
        FROM jurisdiccion
        WHERE impacto_presupuestario_anio = 2025;'''),
        ("Por Jurisdicción", '''SELECT 
            jurisdiccion_desc AS "Jurisdicción",
            SUM(credito_presupuestado) AS Presupuestado,
            SUM(credito_vigente) AS Vigente,
            SUM(credito_devengado) AS Devengado,
            SUM(credito_pagado) AS Pagado
        FROM jurisdiccion
        WHERE impacto_presupuestario_anio = 2025
        GROUP BY jurisdiccion_desc
        ORDER BY SUM(credito_presupuestado) DESC;'''),
        ("Por Subjurisdicción", '''SELECT 
            subjurisdiccion_desc AS "Subjurisdicción",
            SUM(credito_presupuestado) AS Presupuestado,
            SUM(credito_vigente) AS Vigente,
            SUM(credito_devengado) AS Devengado,
            SUM(credito_pagado) AS Pagado
        FROM subjurisdiccion
        WHERE impacto_presupuestario_anio = 2025
        GROUP BY subjurisdiccion_desc
        ORDER BY SUM(credito_presupuestado) DESC;'''),
        ("Por Entidad", '''SELECT 
            entidad_desc AS "Entidad",
            SUM(credito_presupuestado) AS Presupuestado,
            SUM(credito_vigente) AS Vigente,
            SUM(credito_devengado) AS Devengado,
            SUM(credito_pagado) AS Pagado
        FROM entidad
        WHERE impacto_presupuestario_anio = 2025
        GROUP BY entidad_desc
        ORDER BY SUM(credito_presupuestado) DESC;'''),
        ("Por Obra", '''SELECT 
            obra_desc AS "Obra",
            SUM(credito_presupuestado) AS Presupuestado,
            SUM(credito_vigente) AS Vigente,
            SUM(credito_devengado) AS Devengado,
            SUM(credito_pagado) AS Pagado
        FROM obra
        WHERE impacto_presupuestario_anio = 2025
        GROUP BY obra_desc
        ORDER BY SUM(credito_presupuestado) DESC;''')
    ]

    # Exportar a Excel
    with pd.ExcelWriter("reporte_presupuesto_2025.xlsx") as writer:
        for title, query in consultas:
            df = pd.read_sql_query(query, engine)
            # Imprimir en terminal
            print_df(title, query, engine)
            # Guardar en hoja Excel
            sheet_name = title[:31]  # Excel limita a 31 caracteres
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("\nArchivo Excel generado: reporte_presupuesto_2025.xlsx\n")

if __name__ == "__main__":
    main()
