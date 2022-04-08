num = int(input("Digite num: "))

divisor = 1

while divisor <= num:
    if num % divisor == 0:
        soma = soma + divisor
    divisor = divisor + 1
print("A soma dos divisores é", soma)