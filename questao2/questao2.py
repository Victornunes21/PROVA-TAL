list = []
X = int(input("Informe um valor para X: "))
list.append(X)
lista1 = list
list.reverse()
lista2 = list

if lista1 ==lista2:
    print("Verdadeiro")
else:
    print("Falso")