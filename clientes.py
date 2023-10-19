clientes = []

def geraCodigo():
    if len(clientes)>0:
        novoCodigo = clientes[-1]["codigo"] + 1
        return novoCodigo
    else:
        return 1





while True:
    print("-" * 60)
    print("1- Inclusão")
    print("2- Exclusão")
    print("3- Alteração")
    print("4- Listagem Geral")
    print("S - Sair")
    print("-" * 60) 
    opcao = input("Digite Opção: ").strip().upper()
    if opcao == '1': #Inclusão
        codigo = geraCodigo()
        nome = input("Informe seu nome: ").strip().upper()
        endereco = input("Informe seu endereço: ").strip().upper()
        tipo = input("[F]ísica ou [J]urídica: ").strip().upper()
        if tipo == 'F':
            cpfCnpj = input("Digite CPF: ").strip().upper()
        elif tipo == 'J':
            cpfCnpj = input("Digite CNPJ: ").strip().upper()
        else:
            print("Opção Inválida")
        # [codigo, nome,..., cpfCnpj] Errado
        clientes.append({ 
                            "codigo": codigo,
                            "nome": nome,
                            "endereco": endereco,
                            "tipo": tipo,
                            "cpfCnpj": cpfCnpj,
                         })     

    elif opcao == '2': #Exclusão
        codigo = int(input("Digite o código a excluir: ").strip().upper() )
        for posicao in range(len(clientes)):
            if clientes[posicao]["codigo"] == codigo:
                 copia = clientes.pop(posicao)
                 break

    elif opcao == '3':
        
    elif opcao == '4':
        for cliente in clientes:
            print(clientes)
    elif opcao == 'S':
        print("Saindo...")
        break
    else:
        print("Operação Inválida")