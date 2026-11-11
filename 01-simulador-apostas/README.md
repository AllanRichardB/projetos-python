# Simulador de apostas

Programa que simula as rodadas de um jogador de apostas. A cada rodada, ele aposta um valor fixo e tem 40% de chance de ganhar. No final, o programa informa se terminou com lucro, prejuízo ou com o dinheiro inicial.

A simulação é reprodutível: o número sorteado depende de uma semente (seed) que é informada como entrada.

## Como rodar

Dentro desta pasta, execute `python apostas.py` e digite os quatro valores, um por linha:

1. a semente do gerador aleatório
2. o saldo inicial
3. o valor de cada aposta
4. o número de rodadas

## Exemplo

Entrada: 1, 100, 10 e 20 (um valor por linha)
Saída: Prejuízo, ficando com 40 reais

## O que pratiquei

- geração de números aleatórios com seed
- laços (for) e condicionais
- controle de fluxo com break
