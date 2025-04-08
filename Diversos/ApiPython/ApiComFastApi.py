from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str

dados: List[Usuario] = [
    Usuario(id=1, nome="João"),
    Usuario(id=2, nome="Maria")
]

@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return dados

@app.get("/usuarios/{id}", response_model=Usuario)
def obter_usuario(id: int):
    for usuario in dados:
        if usuario.id == id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.post("/usuarios", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    dados.append(usuario)
    return usuario

@app.put("/usuarios/{id}", response_model=Usuario)
def atualizar_usuario(id: int, usuario_atualizado: Usuario):
    for i, usuario in enumerate(dados):
        if usuario.id == id:
            dados[i] = usuario_atualizado
            return usuario_atualizado
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/usuarios/{id}")
def deletar_usuario(id: int):
    global dados
    dados = [u for u in dados if u.id != id]
    return {"mensagem": "Usuário deletado com sucesso"}


