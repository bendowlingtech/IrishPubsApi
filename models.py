from pydantic import BaseModel

class Pub(BaseModel):
    id: int
    title: str
    name: str
    address: str
    county: str

