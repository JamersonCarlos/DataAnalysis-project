#Paulo e Pedro fizeram uma longa viagem para a copa e tiveram que ajustar seus relógios por causa do fuso horário.
#Assim, para melhor se organizarem para as próximas viagens, eles pediram que você fizesse um aplicativo para celular que, dada a hora de saída, tempo de viagem e o fuso do destino #com relação à origem, você informe a hora de chegada de cada voo no destino.
print("Obedeça os intervalos a seguir \n -> Hora de Saída: (0 a 23) \n -> Tempo de Viagem: (1 a 12) \n -> Fuso Horário: (-5 a 5) \n")
horaSaida = int(input("Hora de Saída: "))
tempoViagem = int(input("Tempo Viagem: "))
fusoHorario = int(input("Fuso Horário: "))


if (horaSaida >= 0 and horaSaida <= 23 and tempoViagem >= 1 and tempoViagem <= 12 and fusoHorario >= -5 and fusoHorario <= 5): 
    if (horaSaida + tempoViagem + fusoHorario > 24): 
        horaFinal = (horaSaida + tempoViagem + fusoHorario) - 24

    if (horaSaida + tempoViagem + fusoHorario < 0): 
        horaFinal = 24 + (horaSaida + tempoViagem + fusoHorario)
else: 
    print("Os valores digitados não satisfaz os intervalos")

