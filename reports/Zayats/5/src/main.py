"""Основной модуль FastAPI приложения."""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import crud
import schemas
from database import engine, SESSION_LOCAL


# Создание таблиц
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """Создать и закрыть сессию БД."""
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()


@app.post("/transport_types/", response_model=schemas.TransportTypeOut)
def create_type(data: schemas.TransportTypeCreate, db: Session = Depends(get_db)):
    """Создать тип транспорта."""
    return crud.create_transport_type(db, data)


@app.get("/transport_types/", response_model=list[schemas.TransportTypeOut])
def read_types(db: Session = Depends(get_db)):
    """Получить все типы транспорта."""
    return crud.get_transport_types(db)


@app.put("/transport_types/{type_id}")
def update_type(type_id: int, name: str, db: Session = Depends(get_db)):
    """Обновить тип транспорта."""
    obj = crud.update_transport_type(db, type_id, name)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@app.delete("/transport_types/{type_id}")
def delete_type(type_id: int, db: Session = Depends(get_db)):
    """Удалить тип транспорта."""
    obj = crud.delete_transport_type(db, type_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Deleted"}


@app.post("/routes/", response_model=schemas.RouteOut)
def create_route(data: schemas.RouteCreate, db: Session = Depends(get_db)):
    """Создать маршрут."""
    return crud.create_route(db, data)


@app.get("/routes/", response_model=list[schemas.RouteOut])
def read_routes(db: Session = Depends(get_db)):
    """Получить все маршруты."""
    return crud.get_routes(db)
