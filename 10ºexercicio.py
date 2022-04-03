distancia_percorrida = float(input("Distancia / metros percorridos"))
tempo_de_prova = float(input("Tempo de prova"))

velocidade_ms = distancia_percorrida / tempo_de_prova

velocidade_km = float(velocidade_ms * 3.6)
print(velocidade_ms)
print(velocidade_km)