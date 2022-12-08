#Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
import datetime 
try: 
    endPoint = 0
    while endPoint != 1: 
        inicio = input("Hora de Inicio Ex: 10:26 = ").split(":")
        final = input("Hora de Termino Ex: 12:03 = ").split(":")
        horaInicial = int(inicio[0])
        minutoInicial = int(inicio[1])
        horaFinal = int(final[0])
        minutoFinal = int(final[1])
        if (horaInicial in range(0,25) and horaFinal in range(0,25)): 
            if (minutoInicial in range(0,60) and minutoFinal in range(0,60)): 
                duration = [horaFinal- horaInicial, abs(minutoFinal - minutoInicial)]
                if(duration[0] > 0): 
                    print(f"O jogo durou {duration[0]} hora(s) e {duration[1]} minuto(s)")
                    endPoint = 1
                elif(duration[0] <= 0): 
                    duration[0] = duration[0] + 24
                    print(f"O jogo durou {duration[0]} hora(s) e {duration[1]} minuto(s)")
                    endPoint = 1
                else: 
                    print("Erro de Calculo")
            else: 
                print("Os minutos são invalidos")
        else: 
            print("A hora informada é invalida")
except ValueError or IndexError:
    print("Formato Digitado Incorreto!")
 
    
