from scipy import stats

dias_trabalhados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Ganhos = [3, 4, 9, 18, 20, 25, 21, 24, 27, 30, 33, 36, 39, 41, 43, 50, 53, 58, 62, 65]

slop, intercept, r, p, std_err = stats.linregress(dias_trabalhados, Ganhos)

print(slop)
print(intercept)
print(r)
print(p)
print(std_err)

def prever(x):
    return slop * x + intercept

previsao = prever(1)

print(round(r,2))

print(previsao)