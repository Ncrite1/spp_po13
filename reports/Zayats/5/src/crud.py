"""Модуль CRUD-операций для транспортной системы."""

from sqlalchemy.orm import Session
from models import TransportType, Route
from schemas import TransportTypeCreate, RouteCreate


# =========================
# TRANSPORT TYPE CRUD
# =========================

def create_transport_type(db: Session, obj: TransportTypeCreate):
    """Создать тип транспорта."""
    db_obj = TransportType(name=obj.name)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_transport_types(db: Session):
    """Получить все типы транспорта."""
    return db.query(TransportType).all()


def update_transport_type(db: Session, type_id: int, name: str):
    """Обновить тип транспорта."""
    obj = (
        db.query(TransportType)
        .filter(TransportType.type_id == type_id)
        .first()
    )

    if obj:
        obj.name = name
        db.commit()

    return obj


def delete_transport_type(db: Session, type_id: int):
    """Удалить тип транспорта."""
    obj = (
        db.query(TransportType)
        .filter(TransportType.type_id == type_id)
        .first()
    )

    if obj:
        db.delete(obj)
        db.commit()

    return obj


# =========================
# ROUTE CRUD
# =========================

def create_route(db: Session, obj: RouteCreate):
    """Создать маршрут."""
    db_obj = Route(route_number=obj.route_number, type_id=obj.type_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_routes(db: Session):
    """Получить все маршруты."""
    return db.query(Route).all()
