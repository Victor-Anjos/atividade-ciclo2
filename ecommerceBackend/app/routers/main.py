/*
* Curso de Engenharia de Software - UniEVANGÉLICA
* Disciplina de Programação Web
* Dev: Victor César
* Data: 06 - 06 - 2024
*/

from fastapi import FastAPI
from app.routers import user, product, order, auth

app = FastAPI()

# Inclui as rotas dos diferentes módulos
app.include_router(user.router)
app.include_router(product.router)
app.include_router(order.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
