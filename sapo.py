# N = 1 -> [ 1 ] = 1
# N = 2 -> [1, 1], [ 2 ] = 2
# N = 3 -> [1, 1, 1], [ 1, 2 ], [ 2, 1 ] = 3
# N = 4 -> [ 1, 1, 1, 1,], [ 2, 1, 1 ], [ 1, 2, 1 ], [ 1, 1, 2 ], [ 2, 2 ] = 5
# N = 5 -> [ 1, 1, 1, 1, 1,], [ 1, 1, 1, 2 ], [ 1, 1, 2, 1 ], [ 1, 2, 1, 1 ], [ 2, 1, 1, 1 ], [ 1, 2, 2 ], [ 2, 1, 2 ], [ 2, 2, 1 ] = 8

def contar_caminhos(num_predas):
    if num_predas <= 1:
        return 1
    return contar_caminhos(num_predas - 1 ) + contar_caminhos(num_predas - 2)

print(contar_caminhos(9))    