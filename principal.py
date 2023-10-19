from operacoes import *
print( linha() )
print("C A L C U L A D O R A")
print( linha() )
print("[A]dição")
print("[S]ubtração")
print("[M]ultiplicação")
print("[D]ivisão")
print("[P]otenciação")
opcao = input("Digite Opção: ").strip().upper()
if opcao == 'S': exit()
if opcao in ['A', 'S', 'M', 'D', 'P']:
    listaValores = []
    valor = 1
    while valor != 0:
        valor = float( input("Digite o valor: ") )
        listaValores.append(valor)
    del listaValores[-1]
    match (opcao):
        case 'A':
            print( soma(listaValores) )
        case 'S':
            print( subtracao(listaValores) )
        case 'M':
            print( produto(listaValores) )
        case 'D':
            print( divisao(listaValores) )
        case 'P':
            print( potenciacao(listaValores))
            