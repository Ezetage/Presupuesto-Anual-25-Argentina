#!/bin/bash
# Script end-to-end para ETL y reporte del Presupuesto Anual 2025

docker-compose down -v

docker-compose up -d

# Esperar a que los servicios estén listos
sleep 10

docker build -t data-etl -f Dockerfile.etl .
docker run --rm --network presupuesto-anual-25_default data-etl

# Esperar a que el ETL termine y los datos estén listos
sleep 10

docker build -t data-report -f Dockerfile.report .
docker run --rm -v "${PWD}:/app" --network presupuesto-anual-25_default data-report
