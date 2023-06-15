Qtd_deLitros = float(input("Informe a quantidade de litros de combustível".strip()))
print(Qtd_deLitros)
print("Bem-vindo! A gasolina custa R$ 5.50 \n O álcool custa R$ 4.18")
tipo =input("Informe o tipo de combustível que deseja usar \n A: Álcool e G: Gasolina".strip())
print(tipo)


if tipo == 'A':
    valor = Qtd_deLitros * 4.18

elif tipo == 'B':
    valor = Qtd_deLitros * 5.50

else:
    print("Operação Inválida")
    exit()
print(f"O valor total a ser pago será de R$ {valor}")