from pydantic import BaseModel

# Esquema para criação de usuário
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Esquema para exibir usuário
class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True

# Esquema para criação de produto
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

# Esquema para exibir produto
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True

# Esquema para criação de ordem
class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    total_price: float

# Esquema para exibir ordem
class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total_price: float

    class Config:
        orm_mode = True
