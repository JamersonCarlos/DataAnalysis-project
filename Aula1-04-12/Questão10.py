#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valorAtrasado, diasAtraso = 0): 
    if (diasAtraso != 0): 
        return valorAtrasado + valorAtrasado * 0.03 + valorAtrasado * (diasAtraso * 0.001)
    else: 
        return valorAtrasado 

endPoint = 1
totalPrestAtrasados = 0
valorAtrasado = 0  

while endPoint != 0: 
    valorAtrasado = float(input("Valor da Prestação R$"))
    if (valorAtrasado == 0): 
        endPoint = valorAtrasado 
        break
    diasAtraso = int(input("Dias Atrasados: "))
    totalPrestAtrasados += valorPagamento(valorAtrasado, diasAtraso)

print("Total de Valor Atrasado R$%.2f" %(totalPrestAtrasados))



