import random

print("-" * 40,
      "\n" + " " * 16 + "Jokempo",
      "\n" + "-" * 40)
print("Digite o nome do Jogador")
nomeJogador = input().lower()

mao = ["pedra", "papel", "tesoura"]

deveContinuar = True

while deveContinuar:
    print("Escolha pedra, papel ou tesoura")
    maoJogador = input().lower()

    if maoJogador == "parar":
        deveContinuar = False

    elif maoJogador not in mao:
        print("Escolha inválida")

    else:
        indiceMaoDoJogador = mao.index(maoJogador)
        indiceMaoDoComputador = random.randint(0, 2)
        maoComputador = mao[indiceMaoDoComputador]

        print(f"{nomeJogador.capitalize()} jogou {maoJogador}")
        print(f"Computador jogou {maoComputador}")

        if indiceMaoDoJogador == indiceMaoDoComputador:
            print("EMPATE")
        elif maoJogador == "pedra":
            if maoComputador == "tesoura":
                print("Pedra amassa tesoura"
                      f"\n{nomeJogador.capitalize()} venceu")
            else:
                print("Papel embrulha pedra"
                      "\nComputador Venceu")

        elif maoJogador == "papel":
            if maoComputador == "tesoura":
                print("Tesoura corta papel"
                      "\nComputador venceu")
            else:
                print("Papel embrulha pedra"
                      f"\n{nomeJogador.capitalize()} venceu")

        else:
            maoJogador == "tesoura"
            if maoComputador == "pedra":
                print("Pedra amassa tesoura")
                print("Computador Venceu")
            else:
                print("Tesoura corta papel"
                      f"\n {nomeJogador.capitalize()} Venceu")
