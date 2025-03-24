from pydantic import BaseModel, Field
from typing import Optional

# Esquema para la creación de variedades
class VarietyArrozCreate(BaseModel):
    nombre: str
    numero_registro_productor_ica: str
    caracteristicas_variedad: Optional[str] = None

    class Config:
        orm_mode = True

# Esquema para la respuesta de variedades (incluye ID)
class VarietyArrozResponse(VarietyArrozCreate):
    id: int
    name: Optional[str] = Field(None)

    class Config:
        orm_mode = True