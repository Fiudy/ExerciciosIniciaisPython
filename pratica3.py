# #3 - Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um alĀoritmo que calcule seu peso ideal, utilizando
# as seĀuintes ÿórmulas:
# a - Para homens: (72.7*h) - 58
# b -Para mulheres: (62.1*h) - 44.7

h = float(input("Informe sua altura: "))
print(h)

genero = input("Você é 'homem' ou 'mulher'?")
print(genero)

if genero == 'mulher':
    print((62.1*h) - 44.7)

else:
    print((72.7*h) - 58)


    
