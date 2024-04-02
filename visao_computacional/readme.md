## Capítulo 15: Visão Computacional

### Conceitos:
_**Classificador Cascade:**_ Também conhecido como Haar Cascade. É um algoritmo de detecção que utiliza máscaras Haar* para caracterizar objetos por meio de variações de luminosidade, sobretudo em bordas. Funciona da seguinte forma:
- Treinamento: O algoritmo é treinado com imagens que contém o objeto de interesse (imagens positivas), e imagens que não contém o objeto de interesse (imagens negativas) (SEPARA EM DOIS GRUPOS CONTENDO E NÃO CONTENDO AS IMAGENS). Utilizando o algoritmo AdaBoost* de machine learning, é gerado vários classificadores, um para cada feature (Haar feature*). Esses classificadores são treinados para identificar se uma região específica da imagem contém ou não o objeto de interesse.
- Definição de janela: O algoritmo define um tamanho de janela que será usada para procurar o objeto na imagem. O tamanho é escolhido de forma a ser eficiente, considerando que é mais fácil escalar features do que a imagem inteira.
- Varredura da imagem: A imagem é varrida utilizando a janela definida. O algoritmo seleciona e executa um dos mini-classificadores (para uma feature selecionada) com base nos valores de pixel na imagem sob aquela janela.
- Avaliação de features: Se a feature retorna falso, indica que a região da janela não é o objeto de interesse, fazendo assim o algoritmo mover-se para a próxima janela. Se a feature retornar verdadeiro, indica que a região da janela é o objeto de interesse, o algoritmo passa para o próximo classificador e repete o processo. Se todos os classificadores retornarem verdadeiro, o algoritmo conclui que encontrou o objeto de interesse naquela janela.
- Economia de tempo: Se um único classificador dizer que o objeto pertence à classe negativa, o algoritmo passa para a próxima janela recomeçando o processo, economizando processamento e tempo.
- Extração de features: As features Haar são extraídas subtraindo diferentes pixels da imagem de acordo com as máscaras Haar. Os atributos LBP* são calculados comparando o pixel central com sua vizinhança de 8 vizinhos (8 pixels vizinhos) binarizando-os e transformando o código binário em um valor decimal.
> - Haar: Técnica de decomposição de sinais que divide uma imagem em regiões de alta e baixa luminosidade.
> - Mascaras Haar: São funções matemáticas que capturam variações de luminosidades em imagem. Utilizadas para extrair características de objetos em imagens, como formas. bordas e texturas.
> - Características Haar/Haar features: São os resultados da aplicação das máscaras Haar em uma imagem. Representam a variação de luminosidade em diferentes partes de uma imagem. Essas características são usadas para distinguir objetos de fundos.
> - Cascata de classificadores: é uma série de classificadores haar, aplicados em sequência cada um focado em uma característica específica do objeto. Esses classificadores são aplicados em sequência, cada um contribuindo para ter a decisão final de se o objeto está presente na imagem ou não, tornando o algoritmo rápido e eficiente na detecção de objetos.

![Classificador Cascade](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYkh0-RIsDMnWScNn2PMlfNyUAeEFBvAcBMw&s)

_**AdaBoosting:**_ AdaBoost ou Adaptive Boosting, é um algoritmo de aprendizado de máquina que combina vários classificadores fracos (um classificador fraco é um modelo que tem um desempenho ligeiramente melhor do que o acaso ou “chute”) para criar um classificador forte (é um modelo que tem um desempenho significativamente melhor que o acaso).
- Inicialização: Começa com um conjunto de dados não rotulados e um conjunto de classificadores fracos pré-definidos
- Treinamento do primeiro classificador: É treinado como o conjunto de dados. Esse classificador é então usado para prever as classes dos dados.
- Ajuste de pesos: Após a previsão, os pesos dos dados são ajustados. Os dados que foram classificados corretamente pelo classificador fraco recebem um peso menor, enquanto os dados que foram classificados incorretamente recebem um peso maior. Isso faz com que os dados que são mais difíceis de classificar tenham uma influência maior no próximo classificador.
- Treinamento de classificadores subsequentes: O próximo classificador fraco é treinado com base nos pesos ajustados dos dados. Esse processo é repetido para cada classificador subsequente.
- Combinação dos classificadores: Após o treinamento de todos os classificadores fracos, são combinados em um único classificador forte. É feita de tal forma que os classificadores que têm um desempenho melhor (que tem menos erros) têm mais influência na decisão final do que os classificadores que fazem mais erros.
- Previsão: O classificador forte é então usado para fazer previsões sobre os novos dados.

![AdaBoosting](https://media.licdn.com/dms/image/D4D12AQGvxIYEYw2jTg/article-cover_image-shrink_720_1280/0/1693504800545?e=2147483647&v=beta&t=PJoAEEr5eNM4BVsqWY4wuXy3vcl_VBR7G-tONggL3Fg)

_**LBP (Local Binary Patterns):**_ Técnica de extração de características usada em visão computacional para descrever a textura local de uma image, baseados na comparação de um pixel central com seus vizinhos e na codificação da diferença de intensidade entre o pixel central e o seus vizinhos em um padrão binário. Funciona (em resumo) assim:
- Definição de vizinhança: Primeiro, um conjunto de vizinhos é definido em torno de um pixel central. A vizinhança pode ser definida de várias maneiras, como em um círculo de raio (r) ao redor do pixel central, um quadrado de lado (2r + 1) ou uma forma personalizada.
- Comparação de intensidades: A intensidade do pixel central é comparada com a intensidade de cada um dos vizinhos. A comparação é feita em um sentido circular, começando com o vizinho imediatamente à direita do pixel central.
- Codificação binária: A comparação de intensidades é codificada em um padrão binário. Se a intensidade do vizinho é maior que a do pixel central, o bit correspondente no padrão binário é definido como 1; se for menor, o bit é definido como 0.
- Criação do padrão binário local: O padrão binário resultante é o Padrão Binário Local do pixel central. Este padrão captura a textura local ao redor do pixel.
- Extração de características: Os Padrões Binários Locais são então usados para extrair características de textura da imagem. Essas características podem ser usadas para classificar imagens, reconhecer objetos ou realizar outras tarefas de visão computacional.
> Em resumo bem grosseiro o LBP, seleciona um pixel central e o compara com os seus pixels vizinhos, onde, em um sentido horário, analiza um a um com a condição: Se a intensidade do pixel (em escalas de cor rgb ou grayscale) for maior ou igual ao central recebe 1, se for menor, recebe zero e ao final, é montado um número binário a partir do vizinho do canto superior direito em sentido horário. Exemplo:
> | 12 | 15 | 18 |
> | ------------- | ------------- | ------------- |
> | 5 | 8 | 3 |
> | 8 | 1 | 2 |
> 
> No exemplo acima, foi gerado o número 11100010 (226 em hex), em uma matriz que tem como central o número 8 e seguindo a ordem 12 -> 15 -> 18 -> 3 -> 2 -> 1 -> 8 -> 5 (iniciando no canto superior esquerdo e seguindo em sentido horário).
> Visualização após aplicação dessa técnica:
> | 1 | 1 | 1 |
> | ------------- | ------------- | ------------- |
> | 0 | 8 | 0 |
> | 1 | 0 | 0 |

![LBP](https://miro.medium.com/v2/resize:fit:724/1*FLFCkrSCgrf4Ps-NmW1OXQ.jpeg)

### Alguns algoritmos de reconhecimento faciais:
_**Facemark:**_ A detecção de pontos faciais é uma técnica avançada que identifica pontos específicos no rosto, com os cantos dos olhos, ponta do nariz e outras características relevantes para identificação facial.É útil para uma variedade de aplicações como reconhecimento de expressões e emoções, detecção de cansaço e sonolência, direção do rosto e alinhamento facial e detecção de piscadas.

_**LBPH (Local Binary Path Histograms):**_ Uma extensão do LBP*, é utilizada para descrever a distribuições de padrões binários nos locais em uma imagem ou região de interesse. A cada pixel em uma imagem (região de interesse), um LBP* é criado e, em seguida é construído com base em todos os LBP's encontrados, o histograma conta a frequência de cada padrão binário local da região. Os Histogramas de Padrões Binários Locais são uma ferramenta poderosa para a extração de características de textura, pois são robustos a variações de iluminação e escala (assim como o LBP), e podem capturar a textura local de uma maneira que é invariante à rotação.

![LBPH](https://miro.medium.com/v2/resize:fit:1400/0*u46rgZKGXlpvuqJO.png)

### Problema base:
Criar um algoritmo que seja capaz de identificar corpos humanos (vivos ok? Não gostaria da polícia federal na minha porta).<br>
[Resolução do exercício](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/visao_computacional/exercicio_deteccao_de_corpo.py)

#

## Chapter 15: Computer Vision

### Concepts:
_**Cascade Classifier:**_ Also known as Haar Cascade. It is a detection algorithm that uses Haar* masks to characterize objects through variations in luminosity, especially at edges. It works as follows:
- Training: The algorithm is trained with images that contain the object of interest (positive images), and images that do not contain the object of interest (negative images) (SEPARATES INTO TWO GROUPS CONTAINING AND NOT CONTAINING THE IMAGES). Using the AdaBoost* machine learning algorithm, several classifiers are generated, one for each feature (Haar feature*). These classifiers are trained to identify whether or not a specific region of the image contains the object of interest.
- Window definition: The algorithm defines a window size that will be used to search for the object in the image. The size is chosen to be efficient, considering that it is easier to scale features than the entire image.
- Image scanning: The image is scanned using the defined window. The algorithm selects and runs one of the mini-classifiers (for a selected feature) based on the pixel values ​​in the image under that window.
- Feature evaluation: If the feature returns false, it indicates that the region of the window is not the object of interest, thus making the algorithm move to the next window. If the feature returns true, indicating that the window region is the object of interest, the algorithm moves to the next classifier and repeats the process. If all classifiers return true, the algorithm concludes that it has found the object of interest in that window.
- Time saving: If a single classifier says that the object belongs to the negative class, the algorithm moves to the next window starting the process again, saving processing and time.
- Feature extraction: Haar features are extracted by subtracting different pixels from the image according to the Haar masks. LBP* attributes are calculated by comparing the central pixel with its neighborhood of 8 neighbors (8 neighboring pixels), binarizing them and transforming the binary code into a decimal value.
> - Haar: Signal decomposition technique that divides an image into regions of high and low luminosity.
> - Haar Masks: These are mathematical functions that capture variations in brightness in an image. Used to extract features of objects in images, such as shapes. edges and textures.
> - Haar features/Haar features: These are the results of applying Haar masks to an image. They represent the variation in luminosity in different parts of an image. These features are used to distinguish objects from backgrounds.
> - Cascade of classifiers: is a series of haar classifiers, applied in sequence, each focused on a specific characteristic of the object. These classifiers are applied in sequence, each one contributing to the final decision of whether the object is present in the image or not, making the algorithm fast and efficient in detecting objects.

![Cascade Classifier](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYkh0-RIsDMnWScNn2PMlfNyUAeEFBvAcBMw&s)

_**AdaBoosting:**_ AdaBoost, or Adaptive Boosting, is a machine learning algorithm that combines multiple weak classifiers (a weak classifier is a model that performs slightly better than chance or “guess”) to create a strong classifier (is a model that performs significantly better than chance).
- Initialization: Starts with a set of unlabeled data and a set of pre-defined weak classifiers
- Training of the first classifier: It is trained as the dataset. This classifier is then used to predict the classes of the data.
- Weight adjustment: After prediction, the data weights are adjusted. Data that was correctly classified by the weak classifier is given a lower weight, while data that was incorrectly classified is given a higher weight. This causes data that is more difficult to classify to have a greater influence on the next classifier.
- Training subsequent classifiers: The next weak classifier is trained based on the adjusted weights of the data. This process is repeated for each subsequent classifier.
- Combination of classifiers: After training all weak classifiers, they are combined into a single strong classifier. It is done in such a way that the classifiers that perform better (that have fewer errors) have more influence on the final decision than the classifiers that make more errors.
- Prediction: The strong classifier is then used to make predictions about the new data.

![AdaBoosting](https://media.licdn.com/dms/image/D4D12AQGvxIYEYw2jTg/article-cover_image-shrink_720_1280/0/1693504800545?e=2147483647&v=beta&t=PJoAEEr5eNM4BVsqWY4wuXy3vcl_VBR7G-tONggL3Fg)

_**LBP (Local Binary Patterns):**_ Feature extraction technique used in computer vision to describe the local texture of an image, based on comparing a central pixel with its neighbors and encoding the difference in intensity between the central pixel and its neighbors in a binary pattern. It works (in summary) like this:
- Neighborhood definition: First, a set of neighbors is defined around a central pixel. The neighborhood can be defined in several ways, such as a circle of radius (r) around the center pixel, a square of side (2r + 1), or a custom shape.
- Intensity comparison: The intensity of the central pixel is compared with the intensity of each of its neighbors. The comparison is done in a circular direction, starting with the neighbor immediately to the right of the center pixel.
- Binary coding: The comparison of intensities is encoded in a binary pattern. If the intensity of the neighbor is greater than that of the central pixel, the corresponding bit in the binary pattern is set to 1; if it is smaller, the bit is set to 0.
- Creation of the local binary pattern: The resulting binary pattern is the Local Binary Pattern of the central pixel. This pattern captures the local texture around the pixel.
- - Feature extraction: Local Binary Patterns are then used to extract texture features from the image. These features can be used to classify images, recognize objects, or perform other computer vision tasks.
> In a very rough summary, LBP selects a central pixel and compares it with its neighboring pixels, where, in a clockwise direction, it analyzes one by one with the condition: If the intensity of the pixel (in rgb or grayscale color scales) is greater than or equal to the central one, it receives 1, if it is smaller, it receives zero and at the end, a binary number is assembled starting from the neighbor in the upper right corner in a clockwise direction. Example:
> | 12 | 15 | 18 |
> | ------------- | ------------- | ------------- |
> | 5 | 8 | 3 |
> | 8 | 1 | 2 |
>
> In the example above, the number 11100010 (226 in hex) was generated, in a matrix whose center is the number 8 and following the order 12 -> 15 -> 18 -> 3 -> 2 -> 1 -> 8 - > 5 (starting in the top left corner and going clockwise).
> Visualization after applying this technique:
> | 1 | 1 | 1 |
> | ------------- | ------------- | ------------- |
> | 0 | 8 | 0 |
> | 1 | 0 | 0 |

![LBP](https://miro.medium.com/v2/resize:fit:724/1*FLFCkrSCgrf4Ps-NmW1OXQ.jpeg)

### Some facial recognition algorithms:
_**Facemark:**_ Facial point detection is an advanced technique that identifies specific points on the face, such as the corners of the eyes, tip of the nose and other features relevant to facial identification. It is useful for a variety of applications such as recognition of expressions and emotions, detection of tiredness and drowsiness, face direction and facial alignment and blink detection.

_**LBPH (Local Binary Path Histograms):**_ An extension of LBP*, it is used to describe the distribution of binary patterns at locations in an image or region of interest. For each pixel in an image (region of interest), an LBP* is created and then constructed based on all LBP's found, the histogram counts the frequency of each local binary pattern in the region. Local Binary Pattern Histograms are a powerful tool for extracting texture features, as they are robust to variations in lighting and scale (just like LBP), and can capture local texture in a way that is rotation invariant.

![LBPH](https://miro.medium.com/v2/resize:fit:1400/0*u46rgZKGXlpvuqJO.png)

### Base problem:
Create an algorithm that is capable of identifying human bodies (alive, ok? I wouldn't want the FBI on my door).<br>
[Exercise resolution](https://github.com/p3dru/inteligencia_artificial_machine_learning/blob/main/visao_computacional/exercicio_deteccao_de_corpo.py)
