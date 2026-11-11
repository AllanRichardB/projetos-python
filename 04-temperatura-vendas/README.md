# Temperatura e vendas de sorvete

Programa que ajusta dois modelos aos dados de uma sorveteria, um linear e um polinomial de grau 2, calcula o coeficiente de determinação (R²) de cada um, indica qual se ajusta melhor e prevê as vendas para uma temperatura informada.

Os dados do arquivo CSV são de exemplo, criados para demonstrar o programa.

## Arquivos

- vendas.py: o programa
- TemperaturaVendas.csv: planilha de exemplo com as colunas Temperatura e Vendas, separadas por ponto e vírgula

## Como rodar

Requisitos: Python e as bibliotecas pandas e NumPy (`pip install pandas numpy`).

Dentro desta pasta, execute `python vendas.py` e digite a temperatura (em °C) para a qual quer a previsão.

## Exemplo

Entrada: 30

Saída:
Modelo linear:
Coeficientes (a, b): 5.07, -9.71
Coeficiente de determinação (R²): 0.85
Modelo polinomial grau 2:
Coeficientes (a, b, c): -0.36, 24.69, -265.47
Coeficiente de determinação (R²): 0.98
Modelo que melhor se ajusta aos dados: Polinomial
Previsão para temperatura 30.00 °C:
Vendas (modelo linear): 142.37
Vendas (modelo polinomial): 154.75

## O que pratiquei

- leitura de CSV com separador personalizado
- regressão linear e polinomial com NumPy
- comparação de modelos usando o R²
