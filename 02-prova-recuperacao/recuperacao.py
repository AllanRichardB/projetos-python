import pandas as pd
df = pd.read_csv('P1P2.csv')
ID = int(input())
media = (df.loc[ID]['Prova 1'] + df.loc[ID]['Prova 2'] + df.loc[ID]['Trabalho']) / 3
sub = input()
print(f'Notas originais — Prova 1: {df.loc[ID]['Prova 1']}, Prova 2: {df.loc[ID]['Prova 2']}, Trabalho: {df.loc[ID]['Trabalho']}')
print(f'Média original: {media:.2f}')
if sub == 'S':
    Nsub = float(input())
    if df.loc[ID]['Prova 2'] > df.loc[ID]['Prova 1']:
        medianova = (Nsub + df.loc[ID]['Prova 2'] + df.loc[ID]['Trabalho']) / 3
    elif df.loc[ID]['Prova 1'] > df.loc[ID]['Prova 2']:
        medianova = (df.loc[ID]['Prova 1'] + Nsub + df.loc[ID]['Trabalho']) / 3
    print(f'Média após recuperação {medianova:.2f}')
    if media < medianova:
        print('O aluno melhorou.')
        D = medianova - media
        print(f'Diferença: {D:.2f} pontos')
    if media == medianova:
        print('O aluno manteve a média.')
    if media > medianova:
        print('O aluno piorou.')
        D = media - medianova
        print(f'Diferença: {D:.2f} pontos')
elif sub == 'N':
    print('O aluno manteve a média.')
