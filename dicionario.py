dic = dict()
meses ={
    '1': "Janeiro",
    '2': "Fevereiro",
    '3': "Março",
    '4': ["Abril", "Maio", "Junho"]
}

inv = { 
    "armas": ["Escudo", "Espada"],
    "pocoes": ["Magia", "Velo"],
    "comida": ["Frutas", "Amêndoas"],
    "armas": ["ArcoFlecha", "Machado"]

}

print(inv)

chaves = list( inv.keys())
print(chaves)

print( inv.values())

inv["pocoes"] = ["Força", "Destreza"]
inv["roupas"] = "capa"
print(inv)

chaves = list( inv.values() )
inv["pocoes"] = ["Força", "Destreza"]
inv["roupas"] = ['capa',]

print(inv)

copia=inv["armas"].pop(1)
print(inv)
print(copia)

lista = [x**3 for x in range(10) if  x%2==1]
print(lista)

print("objetos"  not in inv)

invBackup = inv

novo = {}

