# ==========================
# SISTEMA DE TRIAGEM INTELIGENTE (S.T.I.)

CORES_TRIAGEM = ('VERMELHO', 'AMARELO', 'VERDE', 'AZUL')


cpfs_cadastrados = set()


fila_atendimento = []


def calcular_pontuacao(gravidade, tempo):
    return (gravidade * 10) + tempo


def definir_cor(gravidade):
    if gravidade >= 8:
        return CORES_TRIAGEM[0]  # VERMELHO
    elif gravidade >= 5:
        return CORES_TRIAGEM[1]  # AMARELO
    elif gravidade >= 3:
        return CORES_TRIAGEM[2]  # VERDE
    else:
        return CORES_TRIAGEM[3]  # AZUL


def cadastrar_paciente():
    cpf = input("CPF do paciente: ").strip()

    if cpf in cpfs_cadastrados:
        print("❌ ERRO: CPF já cadastrado!\n")
        return

    nome = input("Nome do paciente: ").strip()

    try:
        gravidade = int(input("Gravidade (1 a 10): "))
        tempo = int(input("Tempo de espera (minutos): "))

        if not (1 <= gravidade <= 10):
            print("❌ Gravidade inválida!\n")
            return

    except ValueError:
        print("❌ Entrada inválida!\n")
        return

    pontuacao = calcular_pontuacao(gravidade, tempo)
    cor = definir_cor(gravidade)

    paciente = {
        "nome": nome,
        "cpf": cpf,
        "gravidade": gravidade,
        "tempo_espera": tempo,
        "pontuacao": pontuacao,
        "cor": cor
    }

    fila_atendimento.append(paciente)
    cpfs_cadastrados.add(cpf)

    print(f"✅ Paciente cadastrado | Cor: {cor} | Pontuação: {pontuacao}\n")


def exibir_fila():
    if not fila_atendimento:
        print("📭 Fila vazia.\n")
        return

    fila_ordenada = sorted(
        fila_atendimento,
        key=lambda p: p["pontuacao"],
        reverse=True
    )

    print("\n📋 FILA DE ATENDIMENTO (POR PRIORIDADE)")
    print("-" * 50)

    for i, p in enumerate(fila_ordenada, start=1):
        print(
            f"{i}º | {p['nome']} | CPF: {p['cpf']} | "
            f"Cor: {p['cor']} | Pontuação: {p['pontuacao']}"
        )

    print("-" * 50 + "\n")


while True:
    print("🏥 SISTEMA DE TRIAGEM INTELIGENTE")
    print("1 - Cadastrar paciente")
    print("2 - Exibir fila de atendimento")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        exibir_fila()
    elif opcao == "3":
        print("👋 Sistema encerrado.")
        break
    else:
        print("❌ Opção inválida!\n")
