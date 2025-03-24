from pydantic import BaseModel
from typing import Optional

class LaborCulturalBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio_hectaria: Optional[float]
    precio_hectaria_estimada: Optional[float]
    id_etapa_fenologica: Optional[int]  # Relación con PhenologicalStage

class LaborCulturalCreate(LaborCulturalBase):
    nombre: str
    descripcion: Optional[str] = None
    precio_hectaria: Optional[float] = None
    precio_hectaria_estimada: Optional[float] = None
    id_etapa_fenologica: Optional[int] = None

class LaborCulturalUpdate(LaborCulturalBase):
    pass

class LaborCulturalResponse(LaborCulturalBase):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio_hectaria: Optional[float] = None
    precio_hectaria_estimada: Optional[float] = None
    id_etapa_fenologica: Optional[int] = None
    etapa_fenologica: Optional[dict] = None  # Include if you want to return relationship data

class Config:
        orm_mode = True  

