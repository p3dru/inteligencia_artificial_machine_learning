import pandas as pd

#criando um DataFrame com valores contínuos
df = pd.DataFrame({
    'A': [1.2, 2.5, 3.7, 4.9, 5.1, 6.3, 7.5, 8.7, 9.9, 10.1]
})

#discretiza os valores em 3 pontos, atribuindo todos os valores aos intervalos criados (bins)
df['A_discretized'] = pd.cut(df['A'], bins=3, labels=['Low', 'Medium', 'High'])

print(df)
