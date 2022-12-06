#Faça um programa que leia três números inteiros indicando o número de vitórias, empates e derrotas (nesta ordem) e calcule a quantidade de pontos.
while True: 
    try: 
        informations = input("Digite seguinto o formato vitorias/empates/derrotas: ").split("/")
        totalPontos = int(informations[0]) * 3 + int(informations[1] * 1)
        print(f"Total de pontos: {totalPontos}")
        break
    except IndexError as Error: 
        print("Formato de dados Incorreto! Digite Novamente")
    except ValueError as Error: 
        print("Formato de dados Incorreto! Digite Novamente")
