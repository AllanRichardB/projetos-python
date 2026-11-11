import pandas as pd
import numpy as np

df = pd.read_csv('TemperaturaVendas.csv', sep=';')
(a, b) = np.polyfit(x=df['Temperatura'],y=df['Vendas'], deg = 1)
ccor = df['Temperatura'].corr(df['Vendas'])
cdet = ccor**2
(A, B, C) = np.polyfit(x=df['Temperatura'], y=df['Vendas'], deg = 2)
X = float(input())
Y1 = a * X + b
Y2 = A*X**2 + B*X + C
y = df['Vendas']
x = df['Temperatura']
dif = (y - (A*x**2 + B*x + C))**2
media = y.mean()
dif_media = (y - media)**2
cdet2 = 1 - (dif.sum() / dif_media.sum())

print('Modelo linear:')
print(f'Coeficientes (a, b): {a:.2f}, {b:.2f}')
print(f'Coeficiente de determinação (R²): {cdet:.2f}')

print('Modelo polinomial grau 2:')
print(f'Coeficientes (a, b, c): {A:.2f}, {B:.2f}, {C:.2f}')
print(f'Coeficiente de determinação (R²): {cdet2:.2f}')

if cdet2 > cdet:
    print('Modelo que melhor se ajusta aos dados: Polinomial')
else:
    print('Modelo que melhor se ajusta aos dados: Linear')
print(f'Previsão para temperatura {X:.2f} °C:')
print(f'Vendas (modelo linear): {Y1:.2f}')
print(f'Vendas (modelo polinomial): {Y2:.2f}')
