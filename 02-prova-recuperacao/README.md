# Prova de recuperação

Programa que lê as notas de um aluno em uma planilha (CSV) e calcula a média. Depois, simula uma prova de recuperação que substitui a menor nota entre a Prova 1 e a Prova 2, mostrando a nova média e se o aluno melhorou, piorou ou manteve a média.

## Arquivos

- recuperacao.py: o programa
- P1P2TFaltas.csv: planilha de exemplo com as colunas Prova 1, Prova 2 e Trabalho (uma linha por aluno)

## Como rodar

Requisitos: Python 3.12 ou mais novo e a biblioteca pandas (`pip install pandas`).

Dentro desta pasta, execute `python recuperacao.py` e digite, um por linha:

1. o ID do aluno (a posição dele na planilha, começando em 0)
2. S para fazer a recuperação ou N para não fazer
3. se a resposta foi S, a nota da recuperação

## Exemplo

Entrada: 12, S e 80 (um por linha)

Saída:
Notas originais — Prova 1: 53, Prova 2: 76, Trabalho: 100
Média original: 76.33
Média após recuperação 85.33
O aluno melhorou.
Diferença: 9.00 pontos

## O que pratiquei

- leitura de CSV e seleção de dados com pandas
- condicionais para aplicar uma regra de negócio
- cálculo de médias e formatação de números
