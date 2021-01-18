N: int = int(input('Digite o número de níveis da sua árvore: '))

nlinhas_1a_etapa = N

base = 6 * N - 5

nestrelas_1alinha_da_estrut = 1

for i in range(N):

    nlinhas_etapa_atual = nlinhas_1a_etapa + i
    nestrelas_linha_atual = nestrelas_1alinha_da_estrut + 2 * i

    for k in range(nlinhas_etapa_atual):
        estrelas = "*" * nestrelas_linha_atual
        print(f'{estrelas.center(base)}')
        nestrelas_linha_atual += 2
