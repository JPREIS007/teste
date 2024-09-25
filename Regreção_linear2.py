from sklearn import linear_model

reg = linear_model.LinearRegression()

X_treino = [[3, 100, 10, 5], [4, 150, 15, 6], [2, 80, 8, 4]]
y_treino = [300, 450, 200]

reg.fit(X_treino, y_treino)

print("Coeficientes:", reg.coef_)
print("Intercepto:", reg.intercept_)

print("Digite os novos dados para previsão:")
novo_dado = []
novo_dado.append(float(input("Valor 1: ")))
novo_dado.append(float(input("Valor 2: ")))
novo_dado.append(float(input("Valor 3: ")))
novo_dado.append(float(input("Valor 4: ")))

consumo_previsto = reg.predict([novo_dado])

print(f"Consumo de energia previsto: {consumo_previsto[0]:.2f} kWh")