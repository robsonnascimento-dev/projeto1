Cores_triagem_tupla = ('VERMELHO', 'AMARELO', 'VERDE', 'AZUL')
name_cadastrados = set()
cpfs_cadastrados = set()
fila_atendimento = []
while True:
    print("\n seja bem vindo a UPA Infinity. \n - digite 1 para cadastrar novo paciente. \n - digite 2 para ver fila de espera. \n - digite 3 para sair.")
    resposta = input("digite sua resposta: ")
    if resposta == '1':
        while True:
            try:
                name = input("digite seu nome: ")
                if name in name_cadastrados:
                    print("Nome ja digitado")
                break
            except ValueError:
                print("Já existem pacientes com esse nome.")

        while True:
            try:
                idade = int(input("digite sua idade: "))
                break
            except ValueError:
                print("Por favor, digite apenas números.")
        while True:
            try:
                cpf = int(input("digite seu cpf: "))
                break
            except ValueError:
                print("Por favor, digite apenas números.")
            if cpf in cpfs_cadastrados:
                print("CPF já cadastrado! Paciente duplicado.")
                continue
            else:
                cpfs_cadastrados.add(cpf)
        while True:
            try:
                Gravidade = int(input("digite sua gravidade de 1 a 10: "))
                if 1 <= Gravidade <= 10:
                    break
                else:
                    print("a gravidade precisa estar de 1 a 10")
            except ValueError:
                print("Por favor, digite apenas números.")
        while True:
            try:
                tempo_espera = int(
                    input("digite seu tempo de espera (EM MINUTOS): "))
                break
            except ValueError:
                print("digite apenas números")

        pontuaçao = (Gravidade * 10) + tempo_espera
        paciente = {'nome': name,
                    'cpf': cpf,
                    'gravidade': Gravidade,
                    'tempo_espera': tempo_espera,
                    'pontuaçao': pontuaçao}

    elif resposta == "2":
        if not fila_atendimento:
            print("fila de atendimento vazia ")
        else:
            fila_ordenada = sorted(
                fila_atendimento, key=lambda
                p: p["pontuação"], reverse=True)
            print(" \n FILA DE ATENDIMENTO (POR PRIORIDADE)")
            for i, p in enumerate(fila_ordenada, start=1):
                print(
                    f"{i}º - {p['nome']} | CPF: {p['cpf']} | "
                    f"Gravidade: {p['gravidade']} | "
                    f"Espera: {p['tempo_espera']} min | "
                    f"Pontuação: {p['pontuacao']}"
                )

    elif resposta == '3':
        print("encerrando sistema. . . .")
        break
    else:
        print("opção inválida. Tente novamente.")
