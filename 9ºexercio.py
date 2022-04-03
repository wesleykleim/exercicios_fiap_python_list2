produto = float(input("Digite o valor do rpoduto "))
desconto = float(input("Digite o valor do desconto "))

vl_desconto = produto * desconto / 100

vl_comdesc = produto - vl_desconto

vl_acrecimo = produto + vl_desconto

print("Valor do descont ", vl_desconto, "Valor com desconto ", vl_comdesc, "Valor com acrecimo  ", vl_acrecimo)