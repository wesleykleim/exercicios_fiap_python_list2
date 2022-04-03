rm = int(input("Informe o rm: "))
soma = 0
resto = rm % 10
quoc = rm // 10
soma = soma + resto
resto = quoc % 10
quoc = quoc // 10
soma = soma + resto
resto = quoc % 10
quoc = quoc // 10
soma = soma + resto
resto = quoc % 10
quoc = quoc // 10
soma = soma + resto
resto = quoc % 10
quoc = quoc // 10
soma = soma + resto
print('A soma do RM:', rm, "é", soma)