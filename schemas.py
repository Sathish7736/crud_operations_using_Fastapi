from pydantic import BaseModel

class ProductBase(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    class Config:
        orm_mode = True
