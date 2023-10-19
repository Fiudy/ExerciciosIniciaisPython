def maior(a, b):
    if a>b:
        return f"{a} é o maior"
    elif b>a:
        return f"{b} é o maior" 
    else:
        return f"Valores Iguais"
    

def menor (a,b):
    pass


def colorir(texto:str, cor:str) -> str:
    match(cor.upper() ):
        case "AZUL_PISCINA":
            return "\033[96m]" + texto + "\033[0m"
        case "AZUL":
            return "\033[94m" + texto + "\033[0m"
        case "VERDE":
            return "\033[92m" + texto + "\033[0m"
        case "AMARELO":
            return "\033[93m" + texto + "\033[0m"
        case "VERMELHO":
            return "\033[91m" + texto + "\033[0m"
        case "NEGRITO":
            return "\033[1m" + texto + "\033[0m"
        case "SUBLINHADO":
            return "\033[4m" + texto + "\033[0m"

    

def imprimirNomes(*nomes:str)->None:
    for nome in nomes:
        print(nome)
    
    

def aumentarSalario(*salarios:float) -> tuple:
    lista=[]
    for valor in salarios:
        novoValor = valor * 1.1
        lista.append(novoValor)
    return tuple (lista)

def aumentarSal(*salarios: float):
    return (map(lambda v:v*1.1, salarios))

print(aumentarSal(1000))

   













imprimirNomes("Vinicius", 'ana')    










