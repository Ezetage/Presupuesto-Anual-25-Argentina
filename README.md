# Presupuesto Anual 2025 - Argentina
 
Proyecto basado en el **Presupuesto Anual 2025 de la República Argentina**, utilizando **PostgreSQL, Docker, Bash y Python** para la creación de base de datos, carga de datos y consultas SQL.

---

## Dataset elegido

**Fuente oficial:** [Presupuesto Abierto - Ministerio de Economía](https://www.presupuestoabierto.gob.ar/)

Este dataset contiene la información del presupuesto nacional de Argentina para el año 2025, incluyendo asignaciones por jurisdicción, funciones, programas, partidas, obras, entre otros, asi como también el crédito presupuestado, vigente, comprometido, devengado y pagado.

---

## Algunas de las Preguntas posibles de responder

1. **¿Cuanto es el monto total del Presupuesto para el año 2025?**
2. **¿Cuanto es el monto asignado por jurisdicción y subjurisdicción?**
3. **¿Cuál es la jurisdicción con mayor asignación presupuestaria en 2025?**
4. **Al día de la fecha, ¿Cuánto es el monto devengado del total presupuestado?**
5. **¿Cuáles son las principales obras y proyectos con mayor presupuesto asignado y su estado de ejecución?**

## Resolución de los ejercicios y ejecución end-to-end

Para resolver los ejercicios del proyecto se siguió el siguiente flujo:

1. **Creación del contenedor y base de datos:**
   - Se utiliza Docker y PostgreSQL para levantar el entorno de base de datos.
2. **Operaciones DDL:**
   - Se ejecutan los scripts de creación de tablas y estructuras necesarias.
3. **Carga de datos:**
   - Se cargan los datos del dataset oficial al esquema de la base.
4. **Consultas y reportes:**
   - Se ejecutan consultas SQL y se genera un reporte tabular y un archivo Excel con los resultados.

### Ejecución del proceso end-to-end

Para ejecutar todo el proceso de punta a punta (desde la creación del contenedor, operaciones DDL, carga de datos y consultas), simplemente ejecuta el siguiente script de BASH desde la raíz del proyecto:

```bash
bash ./run_end2end.sh
```

Este script realiza automáticamente:
- Levantamiento y limpieza de contenedores
- Creación de la base de datos y tablas
- Carga de datos
- Ejecución de consultas y generación de reporte Excel

El archivo generado con el reporte final se encontrará en la raíz del proyecto.

### Tablas incluidas en el archivo Excel generado

El archivo Excel generado (`reporte_presupuesto_2025.xlsx`) contiene las siguientes tablas principales:

1. **Resumen general del presupuesto 2025:**
   - Total del crédito presupuestado, vigente, devengado y pagado al día de la fecha.
2. **Detalle por jurisdicción:**
   - Totales de crédito presupuestado, vigente, devengado y pagado, desglosados por cada jurisdicción.
3. **Detalle por subjurisdicción:**
   - Totales de crédito presupuestado, vigente, devengado y pagado, desglosados por cada subjurisdicción.
4. **Detalle por entidad:**
   - Totales de crédito presupuestado, vigente, devengado y pagado, desglosados por cada entidad.
5. **Detalle por obra:**
   - Totales de crédito presupuestado, vigente, devengado y pagado, desglosados por cada obra.

Cada tabla permite analizar el presupuesto desde el total nacional hasta el nivel más granular de obra, mostrando la ejecución presupuestaria en cada caso.

---

## Requisitos mínimos para la ejecución

Para poder ejecutar este proyecto de punta a punta necesitas tener instalado en tu sistema:

- **Python 3.11+**
- **Docker**
- **VS Code** (Visual Studio Code)
- **Git Bash** (opcional, recomendado para Windows si quieres ejecutar scripts bash)

> Se recomienda crear un entorno virtual de Python (venv) y, una vez instalado Python y VS Code, instalar las dependencias del proyecto con:
>
> ```bash
> python -m venv env
> source env/bin/activate  # En Windows: .\env\Scripts\activate
> pip install -r requirements.txt
> ```

Docker y los scripts automatizan la mayor parte del proceso, pero tener las herramientas anteriores instaladas es indispensable para el desarrollo y la ejecución local.