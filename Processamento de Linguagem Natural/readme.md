## Capítulo 11 - Processamento de Linguagem Natural (NLP)

### Conceito
É um campo da inteligência artificial que se concentra na interação entre computadores e humanos usando a linguagem natural. O objetivo da NLP é permitir que as máquinas entendam, interpretem, gerem e respondam a textos humanos de maneira significativa. Algumas de suas principais tarefas são:
- Reconhecimento de Entidades Nomeadas (NER): Identificar e classificar entidades mencionadas em textos, como nomes de pessoas, organizações, locais, datas, etc.
- Análise de Sentimento: Determinar a atitude ou sentimento expresso em um texto, geralmente classificando-o como positivo, negativo ou neutro.
- Extração de Informação: Identificar informações específicas e relevantes em textos não estruturados e extrair essas informações para um formato estruturado.
- Sumarização de Texto: Gerar um resumo conciso e informativo de um texto mais longo, capturando as informações-chave e eliminando detalhes desnecessários.
- Tradução Automática: Traduzir textos de uma língua para outra de forma automática, mantendo o significado e a intenção original.
- Processamento de Linguagem Natural Conversacional: Desenvolver sistemas que possam interagir com os usuários de forma natural em linguagem humana, como chatbots e assistentes virtuais.

Algumas aplicações:
- Busca na Web: Melhorar os resultados de pesquisa na web através da compreensão da intenção do usuário expressa em linguagem natural.
- Análise de Mídias Sociais: Monitorar e analisar conversas e opiniões dos usuários em plataformas de mídia social para fins de marketing, inteligência de mercado, entre outros.
- Assistência Médica: Auxiliar no diagnóstico médico, análise de registros de saúde eletrônicos e extração de informações relevantes de literatura médica.
- Processamento de Linguagem Natural em Dispositivos Móveis: Permitir comandos de voz e assistência virtual em dispositivos móveis, como smartphones e tablets.

### Outros onceitos relacionados
#### Marcação POS
Também conhecida como etiquetagem de partes do discurso ou marcação gramatical, é uma técnica usada para atribuir uma classe gramatical a cada palavra de um texto com base em sua função sintática (substantivos, verbos, adjetivos, advérbios, preposições… etc). Funcionamento:
- Identificação de Classe Gramatical: Cada palavra em um texto é identificada e atribuída a uma classe gramatical específica com base em seu contexto e função sintática na frase.
- Atribuição de Tags: As classes são representadas por tags que as identificam
- Processo de Anotação: A marcação pode ser realizada manualmente por linguistas ou automaticamente por algoritmos de processamento de linguagem natural.

#### Tokens
Em NLP, são as unidades básicas de texto, que são usadas para analisar a linguagem natural, podendo ser uma palavra, número, símbolo ou qualquer outra unidade de texto que tenha significado no contexto. Importância da Tokenização:
- Pré-processamento de Texto: A tokenização é uma etapa essencial no pré-processamento de texto em muitas tarefas de NLP, pois permite que o texto seja dividido em unidades menores e mais gerenciáveis para análise.
- Construção de Vocabulário: A tokenização é usada para construir o vocabulário de um modelo de linguagem, onde cada token único é representado por um índice único no vocabulário.
- Análise de Texto: Ao dividir o texto em tokens, é possível realizar uma série de análises, como contagem de palavras, extração de características, marcação POS, entre outras.

#### Lematização e Stemização
São técnicas utilizadas na NLP para reduzir as palavras à sua forma base ou raiz, facilitando a análise e a comparação de texto. 
- Lematização:
  - Definição: A lematização é o processo de reduzir palavras à sua forma base, conhecida como "lema". O lema é a forma canônica ou o dicionário de uma palavra.
  - Precisão: A lematização é uma abordagem mais precisa do que a stemização, pois considera o contexto gramatical das palavras ao determinar o lema.
  > Exemplo: O lema da palavra "correr" é "correr", e o lema da palavra "melhores" é "melhor".
  - Uso de Dicionários e Regras Gramaticais: A lematização geralmente envolve o uso de dicionários de palavras e regras gramaticais para determinar a forma base correta de uma palavra.
- Stemização:
  - Definição: A stemização é o processo de remover os sufixos ou prefixos de uma palavra para reduzi-la à sua forma raiz, conhecida como "stem".
  - Precisão: A stemização é uma abordagem mais simples e geralmente menos precisa do que a lematização, pois não leva em consideração o contexto gramatical das palavras.
  > Exemplo: O stem da palavra "correr" pode ser "corr", e o stem da palavra "melhores" pode ser "melhor".
  - Heurísticas de Remoção de Afixos: A stemização utiliza heurísticas simples para remover sufixos e prefixos das palavras, o que pode resultar em stems que não são palavras reais.

Quando usar cada uma?
A lematização é preferida em casos onde a precisão é crucial, como em tarefas de análise de sentimentos ou tradução automática.<br>
A stemização é útil em casos onde a simplicidade e a velocidade são mais importantes do que a precisão, como em mecanismos de busca ou indexação de documentos.

#### Urllib
é uma biblioteca padrão do Python que permite acessar URLs. Ela pode ser usada para fazer requisições HTTP e manipular URLs. Com urllib, você pode abrir URLs, ler o conteúdo de páginas da web, enviar dados para servidores, entre outras operações relacionadas à web.

#### BeautifulSoup4 (BS4)
É uma biblioteca que facilita a extração de dados de arquivos HTML e XML. Ela transforma o código HTML em uma árvore de objetos Python, permitindo que você navegue e pesquise essa árvore de forma fácil e intuitiva. BS4 é frequentemente usado em conjunto com urllib para baixar páginas da web e, em seguida, analisar o conteúdo HTML dessas páginas para extrair informações específicas.

#### Nuvem de Palavras
São representações visuais de um conjunto de palavras onde o tamanho de cada palavra é proporcional à sua frequência de ocorrência no conjunto de dados original (podendo o conjunto de dados ser um texto), essas representações são usadas para visualizar e destacar as palavras mais frequentes em um texto ou conjunto de textos de forma rápida e intuitiva. Como funciona:
- Preparação dos dados: O texto é processado para remover pontuações, caracteres especiais e palavras comuns que não agregam muito no sentido do texto como “é”, “de”, “se”... que geralmente envolve o uso de *tokentização* e remoção de *stop words*.
- Contagem de frequência: As palavras restantes serão contadas para determinar a frequência de ocorrência de cada uma.
- Visualização: As palavras são exibidas em uma “nuvem”, onde o tamanho é proporcional à sua frequência. Palavras mais frequentes aparecem maiores, enquanto menos frequentes, menores

#### Stop Words
São palavras comuns que geralmente são removidas durante a etapa de pré-processamento de texto em análise de linguagem natural, pois não contribuem significativamente para o significado do texto e podem distorcer as análises. Exemplos comuns de stop words incluem artigos definidos e indefinidos (como "o", "a", "um"), preposições (como "de", "para", "em"), conjunções (como "e", "ou", "mas"), entre outras.
A remoção de stop words é uma etapa importante na preparação de dados para muitas tarefas de análise de texto, incluindo a criação de nuvens de palavras. Isso ajuda a reduzir o ruído nos dados e a destacar as palavras mais significativas e distintas no texto.

[Exemplo de criação de nuvens de palavras](https://colab.research.google.com/drive/103i_QxFEqzObA_J05KYa0UB-2iHOW8T0#scrollTo=K_FNkudaCMwb )

#### Classificações de sentimentos
As classificações de sentimentos são realizadas usando técnicas de análise de texto e aprendizado de máquina para determinar o sentimento associado a um texto, como positivo, negativo ou neutro. Existem várias abordagens e métodos para realizar classificações de sentimentos, sendo algumas das mais comuns:
- Abordagens para Classificação de Sentimentos:
  - Análise de Sentimento Baseada em Regras: Esta abordagem utiliza regras gramaticais e léxicas para determinar o sentimento de um texto. Por exemplo, palavras-chave positivas e negativas são identificadas e contadas no texto, e o sentimento final é determinado com base na frequência e intensidade dessas palavras.
  - Aprendizado de Máquina Supervisionado: Nesta abordagem, modelos de aprendizado de máquina, como classificadores de Naive Bayes, Support Vector Machines (SVM), ou Redes Neurais, são treinados em um conjunto de dados rotulado com exemplos de textos e seus sentimentos correspondentes. Os modelos aprendem padrões nos dados de treinamento e são capazes de generalizar para classificar o sentimento de novos textos.
  - Análise de Sentimento Baseada em Aspectos: Esta abordagem visa identificar o sentimento associado a aspectos específicos mencionados em um texto. Por exemplo, em uma análise de sentimento de avaliações de produtos, o objetivo pode ser identificar o sentimento associado a diferentes aspectos do produto, como preço, qualidade, atendimento ao cliente, etc.
- Etapas no Processo de Classificação de Sentimentos:
  - Pré-processamento de Texto: O texto é pré-processado para remover ruídos, como pontuações, caracteres especiais e stop words. Além disso, pode envolver a tokenização, lematização ou stemização das palavras.
  - Extração de Características: As características relevantes são extraídas do texto, como palavras-chave, n-gramas, ou vetores de palavras (word embeddings), para representar o texto de forma apropriada para o modelo.
  - Treinamento do Modelo: Um modelo de classificação, como um classificador de Naive Bayes, SVM, ou uma rede neural, é treinado usando um conjunto de dados rotulado contendo exemplos de texto e seus sentimentos correspondentes.
  - Avaliação do Modelo: O desempenho do modelo é avaliado em um conjunto de dados de teste separado para verificar sua precisão e generalização.
  - Classificação de Novos Textos: Uma vez treinado e avaliado, o modelo pode ser usado para classificar o sentimento de novos textos, atribuindo-lhes uma etiqueta de sentimento (positivo, negativo, neutro).
- Avaliação da Classificação de Sentimentos:
A avaliação da classificação de sentimentos é realizada usando métricas como precisão, recall, F1-score, entre outras, que avaliam o quão bem o modelo é capaz de classificar corretamente os sentimentos nos textos.

[Exemplo simples de classificação de sentimentos](https://colab.research.google.com/drive/1YF0GOR3R2IPio34hKpJ1o-H4X-1cUpd- )

[Exercício do módulo](https://colab.research.google.com/drive/102CkX915zk7mHYn-SQIhOQ7qL5_wEPwB )

#

## Chapter 11 - Natural Language Processing (NLP)

### Concept
It is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. The goal of NLP is to enable machines to understand, interpret, generate, and respond to human text in a meaningful way. Some of its main tasks are:
- Named Entity Recognition (NER): Identify and classify entities mentioned in texts, such as names of people, organizations, locations, dates, etc.
- Sentiment Analysis: Determine the attitude or feeling expressed in a text, generally classifying it as positive, negative or neutral.
- Information Extraction: Identify specific and relevant information in unstructured texts and extract this information into a structured format.
- Text Summarization: Generate a concise and informative summary of a longer text, capturing key information and eliminating unnecessary details.
- Automatic Translation: Translate texts from one language to another automatically, maintaining the original meaning and intention.
- Conversational Natural Language Processing: Develop systems that can interact with users naturally in human language, such as chatbots and virtual assistants.

Some applications:
- Web Search: Improve web search results by understanding user intent expressed in natural language.
- Social Media Analysis: Monitor and analyze conversations and user opinions on social media platforms for marketing purposes, market intelligence, among others.
- Medical Assistance: Assist with medical diagnosis, analysis of electronic health records and extraction of relevant information from medical literature.
- Natural Language Processing on Mobile Devices: Enable voice commands and virtual assistance on mobile devices, such as smartphones and tablets.

### Other related concepts
#### POS Marking
Also known as part-of-speech tagging or grammatical marking, it is a technique used to assign a grammatical class to each word in a text based on its syntactic function (nouns, verbs, adjectives, adverbs, prepositions... etc). Operation:
- Grammatical Class Identification: Each word in a text is identified and assigned to a specific grammatical class based on its context and syntactic function in the sentence.
- Tag Assignment: Classes are represented by tags that identify them
- Annotation Process: Marking can be performed manually by linguists or automatically by natural language processing algorithms.

#### Tokens
In NLP, these are the basic text units, which are used to analyze natural language, which can be a word, number, symbol or any other text unit that has meaning in the context. Importance of Tokenization:
- Text Preprocessing: Tokenization is an essential step in text preprocessing in many NLP tasks, as it allows text to be broken down into smaller, more manageable units for analysis.
- Vocabulary Construction: Tokenization is used to build the vocabulary of a language model, where each unique token is represented by a unique index in the vocabulary.
- Text Analysis: By dividing the text into tokens, it is possible to perform a series of analyses, such as word counting, feature extraction, POS marking, among others.

#### Lemmatization and Stemization
These are techniques used in NLP to reduce words to their base or root form, facilitating text analysis and comparison.
- Lemmatization:
  - Definition: Lemmatization is the process of reducing words to their base form, known as a "lemma". The lemma is the canonical or dictionary form of a word.
  - Accuracy: Lemmatization is a more precise approach than stemming because it considers the grammatical context of words when determining the lemma.
  > Example: The motto of the word "racer" is "run", and the motto of the word "melhores" is "better".
  - Use of Dictionaries and Grammatical Rules: Lemmatization generally involves using word dictionaries and grammar rules to determine the correct base form of a word.
- Stemization:
  - Definition: Stemization is the process of removing suffixes or prefixes from a word to reduce it to its root form, known as the "stem."
  - Accuracy: Stemization is a simpler and generally less accurate approach than lemmatization, as it does not take into account the grammatical context of words.
  > Example: The stem of the word "correr" can be "corr", and the stem of the word "melhores" can be "better".
  - Affix Removal Heuristics: Stemization uses simple heuristics to remove suffixes and prefixes from words, which can result in stems that are not real words.

When to use each one?
Lemmatization is preferred in cases where accuracy is crucial, such as in sentiment analysis or machine translation tasks.<br>
Stemization is useful in cases where simplicity and speed are more important than accuracy, such as in search engines or document indexing.

#### Urllib
is a standard Python library that allows you to access URLs. It can be used to make HTTP requests and manipulate URLs. With urllib, you can open URLs, read the content of web pages, send data to servers, among other web-related operations .

#### BeautifulSoup4 (BS4)
It is a library that facilitates the extraction of data from HTML and XML files. It turns HTML code into a tree of Python objects, allowing you to navigate and search that tree easily and intuitively. BS4 is often used in conjunction with urllib to download web pages and then parse the HTML content of those pages to extract specific information.

#### Word Cloud
They are visual representations of a set of words where the size of each word is proportional to its frequency of occurrence in the original data set (the data set may be text), these representations are used to visualize and highlight the most frequent words in a text or set of texts quickly and intuitively. How it works:
- Data preparation: The text is processed to remove punctuations, special characters and common words that do not add much to the meaning of the text such as “is”, “of”, “if”... which generally involves the use of *tokentization* and removal of *stop words*.
- Frequency counting: The remaining words will be counted to determine the frequency of occurrence of each one.
- Visualization: Words are displayed in a “cloud”, where the size is proportional to their frequency. More frequent words appear larger, while less frequent words appear smaller

#### Stop Words
These are common words that are often removed during the text preprocessing step in natural language analysis, as they do not contribute significantly to the meaning of the text and can distort analyses. Common examples of stop words include definite and indefinite articles (such as "the", "a", "one"), prepositions (such as "of", "for", "in"), conjunctions (such as "and", "or ", "but"), among others.
Removing stop words is an important step in preparing data for many text analysis tasks, including creating word clouds. This helps reduce noise in the data and highlight the most significant and distinct words in the text.

[Example of creating word clouds](https://colab.research.google.com/drive/103i_QxFEqzObA_J05KYa0UB-2iHOW8T0#scrollTo=K_FNkudaCMwb )

#### Feelings classifications
Sentiment classifications are performed using text analysis and machine learning techniques to determine the sentiment associated with a text, such as positive, negative, or neutral. There are several approaches and methods for performing sentiment classifications, some of the most common being:
- Approaches for Classifying Feelings:
  - Rule-Based Sentiment Analysis: This approach uses grammatical and lexical rules to determine the sentiment of a text. For example, positive and negative keywords are identified and counted in the text, and the final sentiment is determined based on the frequency and intensity of these words.
  - Supervised Machine Learning: In this approach, machine learning models, such as Naive Bayes classifiers, Support Vector Machines (SVM), or Neural Networks, are trained on a labeled dataset with text examples and their corresponding sentiments. Models learn patterns in training data and are able to generalize to classify the sentiment of new texts.
  - Aspect-Based Sentiment Analysis: This approach aims to identify the sentiment associated with specific aspects mentioned in a text. For example, in a sentiment analysis of product reviews, the objective might be to identify the sentiment associated with different aspects of the product such as price, quality, customer service, etc.
- Steps in the Sentiment Classification Process:
  - Text Pre-processing: Text is pre-processed to remove noise such as punctuation, special characters and stop words. Furthermore, it may involve the tokenization, stemming or stemming of words.
  - Feature Extraction: Relevant features are extracted from the text, such as keywords, n-grams, or word vectors (word embeddings), to represent the text in an appropriate way for the model.
  - Model Training: A classification model, such as a Naive Bayes classifier, SVM, or a neural network, is trained using a labeled dataset containing text examples and their corresponding sentiments.
  - Model Evaluation: Model performance is evaluated on a separate test dataset to check its accuracy and generalization.
  - New Text Classification: Once trained and evaluated, the model can be used to classify the sentiment of new texts by assigning them a sentiment label (positive, negative, neutral).
- Assessment of Sentiment Classification:
The evaluation of sentiment classification is carried out using metrics such as precision, recall, F1-score, among others, which evaluate how well the model is able to correctly classify sentiments in texts.

[Simple example of sentiment classification](https://colab.research.google.com/drive/1YF0GOR3R2IPio34hKpJ1o-H4X-1cUpd- )

[Module exercise](https://colab.research.google.com/drive/102CkX915zk7mHYn-SQIhOQ7qL5_wEPwB )
