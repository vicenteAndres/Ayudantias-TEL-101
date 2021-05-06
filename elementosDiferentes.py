lista1 = [1,2,3,4,5,6,10]
lista2= [4,5,6,7,8,9,10]

listaIguales = list()
listaDistintos = list()

for i in lista1:
    for j in lista2:
        if i != j:
            if i not in (lista1 and lista2):
                    if i not in listaDistintos:
                        listaDistintos.append(i)
        else:
            listaIguales.append(i)


print("Elementos en ambas listas: ", listaIguales)

print("Elementos diferentes en listas: ", listaDistintos)