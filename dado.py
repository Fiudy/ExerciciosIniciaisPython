import random

def rolar_dado():
    return random.randint(1, 6)

while True:
    input("Pressione Enter para rolar o dado...")

    resultado = rolar_dado()

    print("O resultado do dado é:", resultado)

    if resultado >= 5:
        print("Número Alto")
     

    elif resultado == 3 or resultado == 4:
        print("Número Mediano")
    
    else:
        print("Número baixo!")
    

    
