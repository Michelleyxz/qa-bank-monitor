def criar_bug(erro):
    bug = {
        "titulo": "Falha no login",
        "descricao": erro,
        "prioridade": "Alta"
    }
    
    print("\nBUG REGISTRADO:")
    print(bug)
    
    return bug
