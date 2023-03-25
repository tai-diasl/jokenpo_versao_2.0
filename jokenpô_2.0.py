from time import sleep
import random
import emoji

# Crie um programa que faça o computador jogar Jokenpô com você.

# import random
print("-=-"*3)
print(" Jokenpô")
print("-=-"*3)

resp = ""

while resp == "":
    pc = random.randint(0, 2)
    opcoes = ["PEDRA", "PAPEL", "TESOURA"]
    random.choice(opcoes[pc])

    elogio = random.randint(0, 3)
    elogios = ["Você é fera, hein? Você pratica o dia todo?", "Você joga muito bem! Me conta o segredo?",
               "Vou ficar de olho para ver se você não está 'roubando' haha",
               "Quando eu crescer, quero jogar como você!"]
    random.choice(elogios)

    print("""Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    """)

    jogador = int(input("Qual é a sua jogada? "))

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!\n")

    print("-=" * 11)
    print(f"Computador jogou {opcoes[pc]}")
    print(f"Jogador jogou {opcoes[jogador]}")
    print("-=" * 11)

    if pc == 0 and jogador == 1 or pc == 1 and jogador == 2:
        print("JOGADOR VENCE")
        print(elogios[elogio])
    elif pc == 0 and jogador == 2:
        print("COMPUTADOR VENCE ", end="")
        print(emoji.emojize(":sunglasses:", language="alias"))
    elif jogador == 0 and pc == 1 or jogador == 1 and pc == 2:
        print("COMPUTADOR VENCE ", end="")
        print(emoji.emojize(":sunglasses:", language="alias"))
    elif jogador == 0 and pc == 2:
        print("JOGADOR VENCE")
        print(elogios[elogio])
    elif jogador == pc:
        print("EMPATE")
        print("Humm... precisamos desempatar! Estamos bons, hein?")
    resp = input("\nVamos jogar de novo? \nAperte ENTER para CONTINUAR ou S para SAIR: ")
    print()
