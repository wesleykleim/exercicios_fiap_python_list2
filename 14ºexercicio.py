# As casas de São Paulo estão recebendo o carnê do IPTU com duas opções de pagamento:
#à vista ou em 10 vezes. Sua tarefa é desenvolver um programa/algoritmo onde o usuário
#informa (digita) o valor total à vista e o valor de cada parcela. Seu programa imprime o
#desconto em percentual dado pela prefeitura para pagamento à vista.

input_avista = float(input("Digite o valor do IPTU a vista: "))
vl_parcela = float(input("Digite o valor da parcela"))
valor_parcelado = vl_parcela * 10
valor_desconto = valor_parcelado - input_avista
desconto_porcentagem = valor_desconto /input_avista *100

print("Você obteve", desconto_porcentagem, "%")
