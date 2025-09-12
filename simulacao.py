# Se eu jogar dois dados mil vezes, quantas vezes dará a soma 7?

import random

numero_de_vezes = 0

for _ in range(1000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    if soma == 7 or soma == 11:
        numero_de_vezes += 1

print(f'A soma dos dados deu 7 {numero_de_vezes} vezes')        