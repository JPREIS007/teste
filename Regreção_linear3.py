import matplotlib.pyplot as plt
from scipy import stats

x = [6, 7, 5, 8, 4, 9, 7]
y = [70, 80, 60, 90, 50, 95, 85]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def predict_energy(hours):
    return slope * hours + intercept

novo_x = float(input("Digite o novo valor de x para previsão: "))

consumo_previsto = predict_energy(novo_x)

print(f"Consumo de energia previsto para x = {novo_x}: {consumo_previsto:.2f} kWh")

predicted_energy = list(map(predict_energy, x))

plt.scatter(x, y, label='Dados Originais')
plt.plot(x, predicted_energy, color='red', label='Linha de Regressão')
plt.show()