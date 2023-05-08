
ano_nascimento = int(input("Informe seu ano de nascimento"))
print(ano_nascimento)
ano_atual = int(input("Informe o ano atual"))
print(ano_atual)
idade =  ano_atual - ano_nascimento 
print(idade)

if idade < 16:
  print("Não Vota")
elif idade >= 16 and idade == 17:
  print("Voto Facultativo")
elif idade >= 18 and idade <=60:
  print("Voto Obrigatório")
else:
  print("Voto Não Obrigatório")
  
  

