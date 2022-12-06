#Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
countPares = 0
for i in range(5): 
    valor = int(input(f"{i + 1}º valor: "))
    if (valor % 2 == 0 ): 
        countPares += 1 

print(f"Foram digitados {countPares} números pares")
