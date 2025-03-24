# src/schemas/phenologicalStageSchema.py
from pydantic import BaseModel
from typing import List, Optional

class PhenologicalStageBase(BaseModel):
    nombre: str
    fase: str

class PhenologicalStageCreate(PhenologicalStageBase):
    pass

class PhenologicalStageUpdate(PhenologicalStageBase):
    pass


class PhenologicalStageResponse(BaseModel):
    id: int
    nombre: str
    fase: str

    # Optional: Include the relationship if needed
    #varieties: Optional[List["VarietyRiceStageResponse"]] = None

    class Config:
        orm_mode = True  # Enable ORM mode for SQLAlchemy compatibility
