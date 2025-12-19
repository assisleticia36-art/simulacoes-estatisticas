import numpy as np
import matplotlib.pyplot as plt

media = 5000
desvio = 1000
min_val = 2000
max_val = 8000

amostras = []

while len(amostras) < 10000:
    valor = np.random.normal(media, desvio)
    if min_val <= valor <= max_val:
        amostras.append(valor)

amostras = np.array(amostras)

print("Média:", np.mean(amostras))
print("Mediana:", np.median(amostras))
print("Variância:", np.var(amostras))

plt.hist(amostras, bins=30)
plt.title("Distribuição Normal Truncada")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()
