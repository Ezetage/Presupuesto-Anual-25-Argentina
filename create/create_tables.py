from sqlalchemy import create_engine, Column, Integer, String, Date, Float, text
from sqlalchemy.orm import declarative_base

# -------------------------
# Conexión a la base
# -------------------------
DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/presupuesto2025"
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

# -------------------------
# Tablas
# -------------------------

class Jurisdiccion(Base):
    __tablename__ = "jurisdiccion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    impacto_presupuestario_fecha = Column(Date)
    impacto_presupuestario_anio = Column(Integer)
    impacto_presupuestario_mes = Column(Integer)
    jurisdiccion_desc = Column(String)
    credito_presupuestado = Column(Float)
    credito_vigente = Column(Float)
    credito_comprometido = Column(Float)
    credito_devengado = Column(Float)
    credito_pagado = Column(Float)

class Subjurisdiccion(Base):
    __tablename__ = "subjurisdiccion"
    id = Column(Integer, primary_key=True, autoincrement=True)
    impacto_presupuestario_fecha = Column(Date)
    impacto_presupuestario_anio = Column(Integer)
    impacto_presupuestario_mes = Column(Integer)
    subjurisdiccion_desc = Column(String)
    credito_presupuestado = Column(Float)
    credito_vigente = Column(Float)
    credito_comprometido = Column(Float)
    credito_devengado = Column(Float)
    credito_pagado = Column(Float)

class Entidad(Base):
    __tablename__ = "entidad"
    id = Column(Integer, primary_key=True, autoincrement=True)
    impacto_presupuestario_fecha = Column(Date)
    impacto_presupuestario_anio = Column(Integer)
    impacto_presupuestario_mes = Column(Integer)
    entidad_desc = Column(String)
    credito_presupuestado = Column(Float)
    credito_vigente = Column(Float)
    credito_comprometido = Column(Float)
    credito_devengado = Column(Float)
    credito_pagado = Column(Float)

class Obra(Base):
    __tablename__ = "obra"
    id = Column(Integer, primary_key=True, autoincrement=True)
    impacto_presupuestario_fecha = Column(Date)
    impacto_presupuestario_anio = Column(Integer)
    impacto_presupuestario_mes = Column(Integer)
    obra_desc = Column(String)
    credito_presupuestado = Column(Float)
    credito_vigente = Column(Float)
    credito_comprometido = Column(Float)
    credito_devengado = Column(Float)
    credito_pagado = Column(Float)

# -------------------------
# Crear tablas
# -------------------------
try:
    with engine.connect() as conn:
        Base.metadata.create_all(bind=engine)
        print("✅ Tablas creadas correctamente")
except Exception as e:
    print("❌ Error al crear tablas:", e)