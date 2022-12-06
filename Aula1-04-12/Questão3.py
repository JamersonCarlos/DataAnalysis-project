#Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
import datetime 
try: 
    endPoint = 0
    while endPoint != 1: 
        inicio = input("Hora de Inicio Ex: 10:26 = ").split(":")
        horaInicio = datetime.time(int(inicio[0]), int(inicio[1]), 0)
        final = input("Hora de Termino Ex: 12:03 = ").split(":")
        horaFinal = datetime.time(int(final[0]), int(final[1]), 0)
        duration = [horaFinal.hour - horaInicio.hour, abs(horaFinal.minute - horaInicio.minute)]
        if(duration[0] > 0): 
            print(f"O jogo durou {duration[0]} hora(s) e {duration[1]} minuto(s)")
            endPoint = 1
        elif(duration[0] <= 0): 
            duration[0] = duration[0] + 24
            print(f"O jogo durou {duration[0]} hora(s) e {duration[1]} minuto(s)")
            endPoint = 1
        else: 
            print("Erro de Calculo")
except ValueError or IndexError:
    print("Formato Digitado Incorreto!")
 
    
