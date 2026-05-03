cotacao_atual_dolar = float(input("Digite a cotacao atual do dolar: "))
cotacao_dolar_semana_passada = float(input("Digite a cotacao do dolar na semana passada: "))

if cotacao_atual_dolar > cotacao_dolar_semana_passada:
    print(f"A cotação atual é R$ {cotacao_atual_dolar:.2f}")
elif cotacao_dolar_semana_passada < cotacao_atual_dolar:
    print(f"A cotação na semana passada era R$ {cotacao_dolar_semana_passada:.2f}")
else:
    print("A cotação do dólar diminuíu em relação à semana passada.")