import numpy as np

# Simulação do lançamento de um dado justo
n = 1_000_000
lancamentos = np.random.randint(1, 7, size=n)

# Estimativa das probabilidades
valores, contagens = np.unique(lancamentos, return_counts=True)
probabilidades = contagens / n

print("Distribuição empírica do dado justo:")
for v, p in zip(valores, probabilidades):
    print(f"Face {v}: {p:.4f}")
