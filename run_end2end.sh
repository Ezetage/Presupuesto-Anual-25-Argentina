#!/bin/bash
# Script end-to-end para ETL y reporte del Presupuesto Anual 2025

# Forzar ejecución desde la raíz del proyecto
cd "$(dirname "$0")"

docker-compose down -v

# Esperar hasta su eliminación
echo "Esperando 5 segundos para asegurar limpieza..."
sleep 5

docker-compose -p presupuesto-anual-25 up -d

# Esperar a que los servicios estén listos
echo "Esperando 10 segundos para que los servicios estén listos..."
sleep 10

docker build -t data-etl -f Dockerfile.etl .
docker run --rm --network presupuesto-anual-25_default data-etl

# Esperar a que el ETL termine y los datos estén listos
echo "Esperando 10 segundos antes de ejecutar el reporte..."
sleep 10

docker build -t data-report -f Dockerfile.report .
docker run --rm -v "${PWD}:/app" --network presupuesto-anual-25_default data-report
