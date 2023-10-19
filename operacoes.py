def soma(args):
    return sum( args )

def produto(args):
    produto = 1
    for n in args:
        produto *= n # produto = produto * n
    return produto


def subtracao(args):
    resultado = args[0]
    for n in args[1:]:
      resultado -= n 
    return resultado


def divisao(args):
    resultado = args[0]
    for n in args[1:0]:
        resultado/=n
    return resultado

def linha():
    return print("-" * 60)

def potenciacao(args):
    return args[0] ** args[1]
    