def calcular_preco_final(preco_inicial, **adicionais):
    if 'desconto' in adicionais:
        preco_inicial *= (1 - adicionais['desconto'])
    if 'garantia extra' in adicionais:
        preco_inicial += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco_inicial *= (1 + adicionais['imposto'])
    return preco_inicial


print(calcular_preco_final(1000, desconto=0.05, garantia_extra=100, imposto=0.30))
print(calcular_preco_final(1000, garantia_extra=100, imposto=0.20))
print(calcular_preco_final(1000, desconto=0.05, imposto=0.15))
print(calcular_preco_final(1000, imposto=0.35))
print(calcular_preco_final(1000))
