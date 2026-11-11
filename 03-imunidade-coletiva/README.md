# Imunidade coletiva

Simulação simples da propagação de uma doença em uma cidade. A cada dia, o número de contaminados é multiplicado pela taxa de contágio, e o total acumulado de imunizados vai sendo somado. O programa informa em quantos dias a cidade atinge a porcentagem de imunidade coletiva desejada.

## Como rodar

Não precisa instalar nada além do Python. Dentro desta pasta, execute `python imunidade.py` e digite, um por linha:

1. a população da cidade
2. o número inicial de contaminados
3. a taxa de contágio diária (por exemplo, 1.23)
4. a porcentagem de imunidade coletiva desejada

## Exemplo

Entrada: 1064000, 1040, 1.23 e 72 (um por linha)
Saída: 24

## O que pratiquei

- laço while com condição de parada
- crescimento exponencial e acumuladores
- modelagem de um problema real em código
