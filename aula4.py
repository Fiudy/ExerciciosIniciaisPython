#Faça um Programa que peça 4 números e imprima o maior deles.

n1 = int(input("Digite o primeiro número: "))
print(n1)
n2 = int(input("Digite o segundo número: "))
print(n2)
n3 = int(input("Digite o terceiro número: "))
print(n3)

if n1 > n2 and n1 > n3:
     print(f"{n1} é o maior")

elif n2 > n1 and n2 > n3:
     print(f"{n2} é o maior")

else:
     print(f"{n3} é o maior")


if n1 < n2 and n1 < n3:
     print(f"{n1} é o menor")

elif n2 < n2 and n2 < n3:
     print(f"{n2} é o menor")

else:
     print(f"{n3} é o menor")


if n1 == n2 and n1 == n3:
     print(f"{n1} é igual")

elif n2 == n1 and n2 == n3:
     print(f"{n2} é igual")

else:
     print(f"{n3} é igual ")



# n4 = int(input("Digite o quarto número: "))
# print(n4)

# if n1 > n2 and n1 > n3 and n1 > n4 :
#     print(f"{n1} é o maior")

# elif n2 > n1 and n2 > n3 and n2 > n4:
#     print(f"{n2} é o maior")

# elif n3 > n1 and n3 > n2 and n3 > n4:
#     print(f"{n3} é o maior")

# else:
#     print(f"{n4} é o maior")