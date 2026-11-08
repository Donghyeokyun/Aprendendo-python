lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_nomes = {"Marcelo","Fernanda","Osso","Macarrao"}
lista_ano = {2000,2026}

soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    media = soma/len(lista_numeros)
    print(f"A media é: {media}")
except TypeError:
    print("A lista contém um elemento que não é aceito.")