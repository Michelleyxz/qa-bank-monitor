def testar_login(usuario, senha):
    if usuario != "admin" or senha != "1234":
        return "Erro: usuário ou senha inválidos"
    return "Login realizado com sucesso"
