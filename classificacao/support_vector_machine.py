from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#carrega o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

#divide os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#treina o classificador SVM
'''
cria uma instância SVC (que é o nome da classe sklearn que implementa o algoritmo SVM para
classificação)
"kernel='linear'" é o parâmetro que especifica o tipo de kernel a ser usado no SVM.
'Kernel' é uma função que transforma os dados de entrada de uma forma que pode ser mais
facilmente separados por uma linha ou plano
'kernel linar' indica que o SVM deve usar uma fronteira de separação linear entre as classes.
é o mais simples e adequad para problemas que são linearmente separáveis.
c=1.0 é o parâmetro de regularização do SVM, também conhecido como parâmetro de penalidade.
Controla o equilíbrio entre a maximização da margem de decisão e a minimização do erro de
classificação. Um valor maior de C resulta em um modelo que tenta maximizar o margem de 
decisão, mesmo que isso signifique cometer mais erros de classificação. Por outro lado,
um valor menor de C permite que o modelo faça mais erros de classificação para aumentar
o margem de decisão. O valor padrão de C é 1.0, o que é um bom ponto de partida, mas pode
precisar ser ajustado dependendo do problema específico.
'''
classifier = SVC(kernel='linear', C=1.0)
classifier.fit(X_train, y_train)

#faz previsões no conjunto de teste
y_pred = classifier.predict(X_test)

#calcula a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy}")
