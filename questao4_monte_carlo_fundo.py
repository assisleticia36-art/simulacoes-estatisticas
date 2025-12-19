import numpy as np

capital_inicial = 100_000
simulacoes = 1000
clientes_atendidos = []

for _ in range(simulacoes):
    capital = capital_inicial
    clientes = 0

    while capital > 0:
        emprestimo = np.random.uniform(500, 5000)
        if emprestimo > capital:
            break
        capital -= emprestimo
        clientes += 1

    clientes_atendidos.append(clientes)

print("Número médio de clientes atendidos:", np.mean(clientes_atendidos))
print("Desvio padrão:", np.std(clientes_atendidos))
