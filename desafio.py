capacidade_atual, aumento_percentual = map(int, input().split())


nova_capacidade = int(capacidade_atual/100*aumento_percentual)

print(f"{capacidade_atual+nova_capacidade}")