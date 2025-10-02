# create_tables.py
from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Tablas

class Jurisdiccion(Base):
    __tablename__ = "jurisdiccion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    mes_date = Column(Date)
    impacto_presupuestario_anio = Column(Integer)
    impacto_presupuestario_mes = Column(Integer)
    mes_nombre = Column(String)
    jurisdiccion_desc = Column(String)
    credito_presupuestado = Column(Float)
    credito_vigente = Column(Float)
    credito_comprometido = Column(Float)
    credito_devengado = Column(Float)
    credito_pagado = Column(Float)

class Subjurisdiccion(Base):
    __tablename__ = "subjurisdiccion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    mes_date = Column(Date)
    impacto_presupuestario_anio = Column(Integer)
    impacto_presupuestario_mes = Column(Integer)
    mes_nombre = Column(String)
    subjurisdiccion_desc = Column(String)
    credito_presupuestado = Column(Float)
    credito_vigente = Column(Float)
    credito_comprometido = Column(Float)
    credito_devengado = Column(Float)
    credito_pagado = Column(Float)

class Entidad(Base):
    __tablename__ = "entidad"
    id = Column(Integer, primary_key=True, autoincrement=True)
    mes_date = Column(Date)
    impacto_presupuestario_anio = Column(Integer)
    impacto_presupuestario_mes = Column(Integer)
    mes_nombre = Column(String)
    entidad_desc = Column(String)
    credito_presupuestado = Column(Float)
    credito_vigente = Column(Float)
    credito_comprometido = Column(Float)
    credito_devengado = Column(Float)
    credito_pagado = Column(Float)

class Obra(Base):
    __tablename__ = "obra"
    id = Column(Integer, primary_key=True, autoincrement=True)
    mes_date = Column(Date)
    impacto_presupuestario_anio = Column(Integer)
    impacto_presupuestario_mes = Column(Integer)
    mes_nombre = Column(String)
    obra_desc = Column(String)
    credito_presupuestado = Column(Float)
    credito_vigente = Column(Float)
    credito_comprometido = Column(Float)
    credito_devengado = Column(Float)
    credito_pagado = Column(Float)

# -------------------------
# Función para crear tablas
# -------------------------

def create_tables(engine):
    """
    Crea todas las tablas definidas en Base.
    Borra tablas previas si existen.
    """
    try:
        with engine.connect() as conn:
            Base.metadata.drop_all(bind=engine)
            Base.metadata.create_all(bind=engine)
            print("✅ Tablas creadas correctamente")
    except Exception as e:
        print("❌ Error al crear tablas:", e)