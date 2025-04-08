from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando um "banco de dados"
dados = [
    {"id": 1, "nome": "João"},
    {"id": 2, "nome": "Maria"}
]

# Rota GET - listar todos
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(dados)

# Rota GET - buscar por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = next((u for u in dados if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota POST - adicionar novo
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo = request.get_json()
    dados.append(novo)
    return jsonify(novo), 201

# Rota PUT - atualizar
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = next((u for u in dados if u["id"] == id), None)
    if usuario:
        novo = request.get_json()
        usuario.update(novo)
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota DELETE - deletar
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    global dados
    dados = [u for u in dados if u["id"] != id]
    return jsonify({"mensagem": "Usuário removido"}), 200

if __name__ == '__main__':
    app.run(debug=True)