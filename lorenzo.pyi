import random
import statistics
maior = aux =0
menor = 100
lista = []
for contadora in range(1,21):
    aux = int(random.randint(1,20))
    lista.append(aux)
    if(aux > maior):
        maior = aux
    if (aux < menor ):
        menor = aux
print(lista)
print(f"o maior numero foi: {maior} ")
print(f"o menor numero foi:{menor} ")


