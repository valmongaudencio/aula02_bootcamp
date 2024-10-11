nome_usuario = input("Digite seu nome de usuário: ")

if nome_usuario.isdigit():
    print("Você digitou seunome errado")
    exit()
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Você digitou apenas espaço")
    exit()