# Quantos números de 4 dígitos eu posso formar com números de 0 a 9?

# _  _  _  _
# 10 10 10 10
#
# Combinatória: 10 x 10 x 10 x 10 = 10000
#
# _  _ _ _
# 10 9 8 7
#
# Permutação: 10 x 9 x 8 x 7 = 5040
#
# Simulação: Executar as possibilidades:
#

count = 0

for n1 in range(10):
    for n2 in range(10):
        if n2 == n1:
            continue
        for n3 in range(10):
            if n3 == n1 or n3 == n2:
                continue
            for n4 in range(10):
                if n4 == n1 or n4 == n2 or n4 == n3:
                    continue
                count += 1
                # print(f'{n1}{n2}{n3}{n4}')

print(count)                