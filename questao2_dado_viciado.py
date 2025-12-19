import numpy as np

# Probabilidades não uniformes (soma = 1)
probabilidades_reais = [0.10, 0.15, 0.20, 0.20, 0.25, 0.10]

n = 100_000
faces = np.arange(1, 7)

lancamentos = np.random.choice(faces, size=n, p=probabilidades_reais)

valores, contagens = np.unique(lancamentos, return_counts=True)
prob_estimada = contagens / n

print("Distribuição empírica do dado viciado:")
for v, p in zip(valores, prob_estimada):
    print(f"Face {v}: {p:.4f}")

print("Soma das probabilidades estimadas:", prob_estimada.sum())
