from test_login import testar_login
from bug_report import criar_bug
from client_response import responder_cliente

# Lista de usuários simulando um sistema real 
usuarios = [
     {"nome": "Michelle", "user": "michelle", "senha": "0000"},
     {"nome": "João", "user": "admin", "senha": "1234"},
     {"nome": "Ana", "user": "ana", "senha": "1111"},
     {"nome": "Carlos", "user": "admin", "senha": "0000"},

]

for u in usuarios:
    print("\n=============================")
    print(f"Testando usuário: {u[ 'nome']}")

    resultado = testar_login(u["user"], u["senha"])
    print("Resultado:", resultado)

if "Erro" in resultado:
    bug = criar_bug(resultado)
    responder_cliente(u["nome"], resultado)

