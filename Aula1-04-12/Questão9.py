def salarioBruto(salarioLiquido): 
    salarioDescontoINSS = salarioLiquido * 0.11
    return salarioLiquido - salarioDescontoINSS - salarioDescontoINSS * 0.15

salarioLiquido = float(input(f"Digite o salário Liquido R$"))
print(f"Salário Bruto R${salarioBruto(salarioLiquido)}")