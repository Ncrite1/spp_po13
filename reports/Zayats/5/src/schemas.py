# pylint: disable=too-few-public-methods
"""Pydantic схемы для API транспортной системы."""

from pydantic import BaseModel


class TransportTypeCreate(BaseModel):
    """Схема создания типа транспорта."""

    name: str


class TransportTypeOut(BaseModel):
    """Схема вывода типа транспорта."""

    type_id: int
    name: str

    class Config:
        """Настройки Pydantic модели."""
        orm_mode = True


class RouteCreate(BaseModel):
    """Схема создания маршрута."""

    route_number: str
    type_id: int


class RouteOut(BaseModel):
    """Схема вывода маршрута."""

    route_id: int
    route_number: str
    type_id: int

    class Config:
        """Настройки Pydantic модели."""
        orm_mode = True
