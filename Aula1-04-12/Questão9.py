def salarioBruto(salarioLiquido): 
    salarioDescontoINSS = salarioLiquido * 0.11
    DescontoDoIR = (salarioLiquido - salarioDescontoINSS) * 0.15
    return salarioLiquido - (salarioDescontoINSS + DescontoDoIR)

salarioLiquido = float(input(f"Digite o salário Liquido R$"))
print(f"Salário Bruto R$%.2f" %(salarioBruto(salarioLiquido)))