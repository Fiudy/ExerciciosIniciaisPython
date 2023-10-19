from random import randint
import random

while True:
    def rolaDados(qtDados):
        match (qtDados):
            case 1:
                return random.randint(1,6)
            case 2:
                return random.randint(2,12)
            case 3:
                return random.randint(3,18)
            case _:
                return "Número e dados inválidos"

    print("-" * 60)
    dados = int(input("Digite a quantidade de dados que deseja rolar: "))
    print("Rolando os dados...")
    print("-" * 60)
    print(rolaDados(dados))