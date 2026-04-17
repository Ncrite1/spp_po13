from sqlalchemy.orm import Session
import models, schemas

# CREATE
def create_transport_type(db: Session, obj: schemas.TransportTypeCreate):
    db_obj = models.TransportType(name=obj.name)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# READ
def get_transport_types(db: Session):
    return db.query(models.TransportType).all()

# UPDATE
def update_transport_type(db: Session, type_id: int, name: str):
    obj = db.query(models.TransportType).filter(models.TransportType.type_id == type_id).first()
    if obj:
        obj.name = name
        db.commit()
    return obj

# DELETE
def delete_transport_type(db: Session, type_id: int):
    obj = db.query(models.TransportType).filter(models.TransportType.type_id == type_id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj


# ROUTES
def create_route(db: Session, obj: schemas.RouteCreate):
    db_obj = models.Route(route_number=obj.route_number, type_id=obj.type_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_routes(db: Session):
    return db.query(models.Route).all()