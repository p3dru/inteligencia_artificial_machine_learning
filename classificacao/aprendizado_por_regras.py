from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import OneR
from sklearn.metrics import accuracy_score

#carrega o conjunto de dados Iris (presente em um dos datasets do sklearn)
iris = load_iris()
X = iris.data
y = iris.target

#divide os dados em treino e teste (80% teste, 20% treino)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#treina o classificador OneR
classifier = OneR()
classifier.fit(X_train, y_train)

'''
OneR éum algoritmo de aprendizagem por regras que gera uma única regras
para classificar dados. Seu objetivo é encontrar a melhor regra que possa
classificar todos. Sendo a "melhor regra" aquela que minimiza a impureza
dos dados, que é uma medida de quão bem os dados são separados em classes
distintas.
Funcionamento:
- Seleção de características: O algoritmo seleciona a característica que
melhor separa os dados em classes distintas, calculando a impureza dos dados
por cada característica e escolhendo a que resulta na menor impureza.
- Formulação da regra: Com base na característica selecionada, o algoritmo
formula uma regra que pode ser usada na classificação de novos dados. Sendo
a regra, uma condiçãp que verifica se a carcterística de um dado atende à um
determinado critério.
- Aplicação da regra: A regra formulada é aplicada à novos dados para fazer
previsões ou tomar decisões.

Vantagens:
-Simplicidade: O OneR gera uma única regra, tornando o modelo fácil de
entender e interpretar.
-Interpretabilidade: A regra gerada pode ser facilmente interpretada por
humanos, o que é útil em muitos contextos onde a explicabilidade do modelo
é importante.
-Eficácia em Problemas Simples: O OneR pode ser eficaz em problemas de
aprendizado de máquina simples, onde a relação entre as características 
e a variável de saída é relativamente direta.

Desvantagens do OneR
- Limitado pela Complexidade do Problema: O OneR pode não ser eficaz
para problemas complexos ou quando o conjunto de dados é muito grande,
pois ele gera apenas uma regra.
- Sensibilidade à Escala das Características: O OneR pode ser sensível
à escala das características, o que significa que características com
diferentes escalas podem ter um impacto desproporcional na regra gerada.
'''

#Faz previsões no conjunto de teste
y_pred = classifier.predict(X_test)

#calcula a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy}")
