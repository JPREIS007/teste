# Definição dos valores
valor_investido = 10000.00
bem_adquirido = 10000.00
rendimento_mensal = 0.01
numero_parcelas = 10

# Calculo do valor da parcela
valor_parcela = bem_adquirido / numero_parcelas

# Inicialização de variáveis
saldo_investimento = valor_investido
total_rendimentos = 0
total_pago = 0

# Simulação mês a mês
print(" Simulação mês a mês:\n")
print("Mes | Saldo Investimento | Rendimento | Parcela Paga | Saldo Final")

for mes in range(1, numero_parcelas + 1):
    # Cálculo do rendimento mensal
    rendimento = saldo_investimento * rendimento_mensal

    # Atualização do saldo do investimento
    saldo_investimento += rendimento

    # Pagamento da parcela
    saldo_final = saldo_investimento - valor_parcela

    # Atualização dos totais
    total_rendimentos += rendimento
    total_pago += valor_parcela

    # Exibição dos resultados mensais em uma linha
    print(f"{mes:3d} | R${saldo_investimento:16.2f} | R${rendimento: 8.2f} | R${valor_parcela: 10.2f} | R${saldo_final: 9.2f}")

    # Atualização do saldo do investimento  para o proximo mês
    saldo_investimento = saldo_final

# Cálculo e exibição dos resultados finais
economia = saldo_investimento - {valor_investido - bem_adquirido}
print(f"\nEconomia em relação à compra à vista: R$ {economia:.2f}")