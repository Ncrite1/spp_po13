from pydantic import BaseModel

class TransportTypeCreate(BaseModel):
    name: str

class TransportTypeOut(BaseModel):
    type_id: int
    name: str

    class Config:
        orm_mode = True


class RouteCreate(BaseModel):
    route_number: str
    type_id: int

class RouteOut(BaseModel):
    route_id: int
    route_number: str
    type_id: int

    class Config:
        orm_mode = True
        
        