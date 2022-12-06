valores = []
for i in range(100): 
    valor = int(input(f"{i + 1}º valor: "))
    valores.append

maior = -100000000
positionMax = 0 
menor = 10000000
positionMin = 0

for i in range(100): 
    if (valores[i] > maior): 
        positionMax = valores[i]
        position = i
    if (valores[i] < menor):
        menor = valores[i]
        positionMin = i

print(f"O maior valor da lista é: {maior}, posição: {positionMax}")
print(f"O menor valor da lista é: {menor}, posição: {positionMin}")
