#Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.
endPoint = 0; 
count = 0; 
idades = []

print("Para Sair Digite (-1)")

while endPoint != -1: 
    count += 1
    newIdade = int(input(f"{count}º idade: "))
    if(newIdade > 0): 
        idades.append(newIdade)
    else: 
        endPoint = newIdade

print(f"A média das notas é {sum(idades)/len(idades)}")
