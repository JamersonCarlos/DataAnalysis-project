#Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
valores = []
for i in range(100): 
    valor = int(input(f"{i + 1}º valor: "))
    valores.append(valor)

maior = -100000000
position = 0 
for i in range(100): 
    if (valores[i] > maior): 
        maior = valores[i]
        position = i

print(f"O maior valor da lista é: {maior}, posição: {position}")

