from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.controller.varietyArrozController import (
    createVariety, getVariety, listVarieties, updateVariety, deleteVariety
)
from src.database.database import get_db
from src.schemas.varietyArrozSchema import VarietyArrozCreate, VarietyArrozResponse
from typing import List

VARIETY_ARROZ_ROUTES = APIRouter()

# Ruta para crear una nueva variedad de arroz
@VARIETY_ARROZ_ROUTES.post('/register-variety', response_model=VarietyArrozResponse)
def register_variety(variety: VarietyArrozCreate, db: Session = Depends(get_db)):
    return createVariety(variety, db)

@VARIETY_ARROZ_ROUTES.get('/list-varieties', response_model=List[VarietyArrozResponse])
def list_varieties(db: Session = Depends(get_db)):
    # Assuming listVarieties returns a list of ORM objects, not dicts
    varieties = listVarieties(db)  # This should be a list of ORM objects or dicts
    # Convert ORM models to Pydantic models (VarietyArrozResponse)
    return [VarietyArrozResponse.from_orm(variety) for variety in varieties]

# Ruta para obtener una variedad de arroz por ID
@VARIETY_ARROZ_ROUTES.get('/get-variety/{variety_id}', response_model=VarietyArrozResponse)
def get_variety(variety_id: int, db: Session = Depends(get_db)):
    return getVariety(variety_id, db)

# Ruta para actualizar una variedad de arroz
@VARIETY_ARROZ_ROUTES.put('/update-variety/{variety_id}', response_model=VarietyArrozResponse)
def update_variety(variety_id: int, variety: VarietyArrozCreate, db: Session = Depends(get_db)):
    return updateVariety(variety_id, variety, db)

# Ruta para eliminar una variedad de arroz
@VARIETY_ARROZ_ROUTES.delete('/delete-variety/{variety_id}')
def delete_variety(variety_id: int, db: Session = Depends(get_db)):
    return deleteVariety(variety_id, db)
