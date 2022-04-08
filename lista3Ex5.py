dias_uteis = int(input("Dias úteis: "))
horas_trabalhadas = float(input("Quantidade de horas trabalhadas: "))
valor_hora = float(input("informe o valor hora: "))

jornada = dias_uteis * 8

hora_extra = 0

if horas_trabalhadas > jornada:
    qtd_horas_extras = horas_trabalhadas - jornada
    hora_extra = qtd_horas_extras * valor_hora / 2

salario_mensal = horas_trabalhadas * valor_hora + hora_extra

print("O trabalhador receberá {:.2f}".format(salario_mensal))

if hora_extra > 0:
    print("E recebeu {:.2f} relativo às horas-extras".format(hora_extra))
    
