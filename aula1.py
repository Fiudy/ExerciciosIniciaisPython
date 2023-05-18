


n1 = int(input("Informe o primero número"))
print(n1)
n2 = int(input("Informe o segundo número"))
print(n2)
operacao = input("Escolha uma operação: +, -, /")


if operacao == '+':
    print('{} + {}'.format(n1, n2))
    print(n1+n2)


elif operacao == '-':
     print('{} - {}'.format(n1, n2))
     print(n1-n2)

elif operacao == '/':
    print('{} / {}'.format(n1, n2))
    print(n1/n2)

else:
    print('Você está usando uma operação inválida')






