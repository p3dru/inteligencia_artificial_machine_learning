from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import pandas as pd

#dados de exemplo
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Ice cream', 'Eggs']]

#codifica os dados
'''
O TransactionEncoder é uma ferramenta útil para transformar dados de
transaçõesem um formato que pode ser usado por algoritmos de mineração
de regras de associação, como o Apriori.
'''
te = TransactionEncoder()
'''
'te.fit(dataset)' Este método ajusta o TransactionEncoder aos dados de
entrada (dataset). Ele analisa os dados para entender a estrutura e 
prepara o encoder para a transformação.
'.transform(dataset)' Após o ajuste, este método transforma os dados de
entrada em um formato binário, onde cada transação é representada como 
uma linha e cada item é representado como uma coluna. Os valores na matriz
resultante são 1 (indicando a presença do item na transação) ou 0 (indicando
a ausência do item).
'''
te_ary = te.fit(dataset).transform(dataset)
'''
Esta linha cria um DataFrame do pandas a partir da matriz binária te_ary.
O DataFrame terá uma coluna para cada item único encontrado nos dados de entrada,
e cada linha representará uma transação. Os nomes das colunas serão os itens, conforme
determinado pelo TransactionEncoder
'''
df = pd.DataFrame(te_ary, columns=te.columns_)

#aplica o algoritmo Eclat
'''
'min_suport=0.6' Este parâmetro define o suporte mínimo para que um item seja considerado 
frequente. Um item é considerado frequente se estiver presente em pelo menos 60% das transações.
'use_colnames=true' Este parâmetro indica que os nomes das colunas do DataFrame devem ser usados 
como rótulos para os itens, em vez de usar índices numéricos.
'''
frequent_itemsets = fpgrowth(df, min_support=0.6, use_colnames=True)

print(frequent_itemsets)