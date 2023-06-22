

while True:
    opcao = input(" [I]ncluir - \n [A]lterar - \n [E]xcluir -  \n [L]istar - \n [S]air - \n").upper()

    if(opcao == 'I'):
        nome = input("Digite o nome do clente: ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")
        saldo = float(input("Digite o saldo: "))
        print(" ")
        print('=' * 30)

    elif(opcao == 'A'):
        endereco = input("Digite o endereço: ")
        cpf = int(input("Digite o cpf: "))
        saldo = float(input("Digite o saldo: "))
        print(" ")
        print('=' * 30)

    elif(opcao == 'E'):
        nome = input("Digite o nome do clente: ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")
        saldo = float(input("Digite o saldo: "))
        print(" ")
        print('=' * 30)

    elif(opcao == 'L'):
        print(f" Nome: {nome} \n CPF: {cpf} \n Endereço: {endereco} \n Saldo: Atual  = R$ {saldo} ")
        print(" ")
        print('=' * 30)


    elif(opcao == 'S'):
        print("Saindo...")
        print(" ")
        print('=' * 30)
        break

    else:
        print("Opção Inváida!!")