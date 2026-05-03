cotacao_atual_dolar = float(input("Digite a cotacao atual do dolar: "))
cotacao_dolar_semana_passada = float(input("Digite a cotacao do dolar na semana passada: "))
diferenca_cotacao = cotacao_atual_dolar - cotacao_dolar_semana_passada

if cotacao_atual_dolar > cotacao_dolar_semana_passada:
    print(f"A cotação atual é R$ {cotacao_atual_dolar:.2f}" f" e a diferença em relação à semana passada é de R$ {diferenca_cotacao:.2f}")
elif cotacao_dolar_semana_passada < cotacao_atual_dolar:
    print(f"A cotação na semana passada era R$ {cotacao_dolar_semana_passada:.2f}" f" e a diferença em relação à cotação atual é de R$ {diferenca_cotacao:.2f}")
else:
    print("A cotação do dólar está estável em relação à semana passada.")