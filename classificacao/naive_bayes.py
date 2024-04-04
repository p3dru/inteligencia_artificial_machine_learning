from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

#dados fictícios (e muito simples a ponto de afetar a classificação)
emails = [
    "Este é um exemplo de email de spam",
    "Este é um exemplo de email de não spam",
    "Outro exemplo de spam",
    "Outro exemplo de não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
    "spam",
    "não spam",
]

#1 para spam, 0 para não spam
labels = [1, 0, 1, 0, 1, 0, 1, 0 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

#divide os dados em treino e teste (80% treino 20% para teste)
X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.2, random_state=42)

#converte os emails em vetores de características
vectorizer = CountVectorizer()
X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)

#treina o classificador Naive Bayes
classifier = MultinomialNB()
classifier.fit(X_train_transformed, y_train)

#faz previsões no conjunto de teste
y_pred = classifier.predict(X_test_transformed)

#calcula a acurácia
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy}")


#A acurácia é definida ente 0 e 1.
