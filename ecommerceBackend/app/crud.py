from sqlalchemy.orm import Session
from app import models, schemas

# Função para criar um usuário
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password  # Aqui deveria ser usado um hash de senha
    db_user = models.User(username=user.username, hashed_password=hashed_password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Função para obter um usuário pelo nome de usuário
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Função para criar um produto
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, description=product.description, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Função para criar uma ordem
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(user_id=order.user_id, product_id=order.product_id, quantity=order.quantity, total_price=order.total_price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
