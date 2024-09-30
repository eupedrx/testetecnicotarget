# 2 - Fibonacci
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
numero = int(input("Informe um número: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# 3 - Json

import json

# Suponha que o faturamento esteja em um arquivo 'faturamento.json'
with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)

valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

# Contar dias com faturamento superior à média
dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_da_media}")


# 4 - Calculo Estado

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")


# 5 - Inverter String

def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

# String a ser invertida
string = input("Informe uma string: ")

print(f"String invertida: {inverter_string(string)}")

