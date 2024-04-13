## Capítulo 9: Aprendizagem por reforço

### Conceito:
É uma abordagem de machine learning que se baseia no conceito de recompensas e penalidades para treinar agentes para tomar decisões que busquem a maior recompensa possível. Difere do aprendizado supervisionado pois ao invés do agente prever a saída correta com base em entradas conhecidas, o agente irá explorar o ambiente e aprender uma política ótima (política que maximiza a recompensa cumulativa). Possui como principais componentes:
 - Agente: É a entidade que toma decisões e interage com o ambiente.
 - Ambiente: É o contexto no qual o agente opera, é o “espaço” onde o problema é descrito.
 - Ações: São as possíveis decisões que o agente deve tomar (Subir, descer, observar, pegar, comprar, vender…).
 - Estado: É a representação do ambiente no momento atual, cada ação do agente ambiente gera um novo estado.
 - Recompensa: É uma medida de quão bem o agente está fazendo, baseado nas ações que toma.

### Algumas técnicas:
#### Deep Q-learning:
É uma técnica que combina redes neurais profundas (Deep Learning) com o algoritmo Q-Learning* (algoritmo que aprende uma função de valor q, que estima a recompensa esperada para ação em cada estado) para treinar agentes para tomar decisões que maximizem uma recompensa cumulativa em uma ambiente. A Deep Q-Learning, usa redes neurais profundas com a função de valor Q*, permitindo que o agente aprenda com as experiências passadas e faça previsões mais precisas sobre a recompensa futura. Como funciona:
- Inicialização: O agente começa com uma política aleatória (sem um objetivo definido) e uma função de valor Q inicializada aleatoriamente.
- Exploração vs Explotação: O agente explora o ambiente, tomando ações aleatórias para coletar experiências. Á medida que o agente coleta mais experiências, ele começa a explorar menos o ambiente e começa a seguir as ações que parecem ser mais promissoras (as que possuem um maior valor).
- Atualização da função de valor de Q: Após cada ação, o agente atualiza a função de valor Q com base na recompensa recebida e na melhor ação que poderia ter tomado no próximo estado, de acordo com a política atual (que no caso, seria buscar a maximização da recompensa).
- Iteração: O processo de exploração e atualização da função de valor Q é repetido muitas vezes até que o agente aprenda uma política ótima (a maior maximização possível).

<br>[Implementação Explicada](https://colab.research.google.com/drive/1yav1jLsQXPAbk9bhRKCSrK8US75JR-Zd#scrollTo=sbORaqPO0noD)

#### Política de Gradiente:
 Visa otimizar a política de um agente, que é a distribuição de probabilidade sobre as ações que o agente deve tomar em cada estado. É uma abordagem alternativa à aprendizagem por reforço com valor. Ela otimiza diretamente a política tornando-as mais eficientes em termos de tempos de treinamento e eficácia. Funciona atualizando a política de um agente com base no gradiente da recompensa esperada. A recompensa esperada é a média ponderada das recompensas futuras, ponderadas pela política atual visando maximizar a recompensa esperada, esse processo envolve geralmente os seguintes passos:
 - Exploração: O agente explora o ambiente, coletando experiências.
 - Avaliação: A política é avaliada para determinar a recompensa esperada.
 - Atualização: A política é atualizada para maximizar a recompensa esperada.
 - Iteração: O processo é repetido até que a política se converta para uma política ótima.

#### Aprendizagem por reforço com entropia:
É uma extensão da aprendizagem por reforço que incorpora um termo de entropia na função de perda. A entropia é uma medida de desordem ou aleatoriedade em um conjunto de dados, e nesse contexto é usada para incentivar a exploração. Ao adicionar um termo de entropia á função de perda, o algoritmo de aprendizagem por reforço é incentivado a explorar uma ampla gama de ações, em vez de se concentrar em ações que já são conhecidas por produzir recompensas altas. Pode ser particularmente útil em ambientes onde a exploração é crucial para aprender a política ótima. Funciona adicionando um termo de entropia à função de perda, que é calculado com base na distribuição de probabilidade da política atual. O objetivo é maximizar a recompensa esperada (geralmente através da função de valor Q ou de uma política direta) e minimizar a entropia da política. Isso é feito através de um processo iterativo de ajuste dos parâmetros da política, onde a política é atualizada para maximizar a recompensa esperada e minimizar a entropia. Assim:
- Exploração: O agente explora o ambiente, coletando experiências.
- Avaliação: A política atual é avaliada para determinar a recompensa esperada e a entropia da política.
- Atualização: A política é atualizada para maximizar a recompensa esperada e minimizar a entropia.
- Iteração: O processo é repetido até que a política converja para uma política ótima.


#### Aprendizagem por esforço com experiência:
Também conhecida como aprendizagem por esforço com memória de replay, é uma técnica de aprendizagem que usa memória para armazenar e reutilizar experiências passadas. A ideia principal é que, em vez de aprender diretamente dos estados atuais e suas ações subsequentes, o agente aprende dos estados, ações e recompensas armazenados na memória de replay. Tem como vantagens:
- Estabilidade do treinamento: Ao utilizar experiências passadas, a aprendizagem por reforço com experiência pode ser mais estável e menos propensa a oscilações e instabilidades que podem ocorrer durante o treinamento.
- Eficiência: A memória de replay permite que o agente aprenda experiência passadas, o que pode ser mais eficiente do que aprender diretamente dos estados atuais.
- Exploração: Ao utilizar experiências passadas, o agente pode explorar uma ampla gama de ações e estados, mesmo que essas experiências não sejam imediatamente relevantes para o estado atual.
Funciona da seguinte forma:
- Coleta de Experiências: O agente interage com o ambiente, coletando experiências (estados, ações, recompensas e estados seguintes).
- Armazenamento em Memória de Replay: As experiências coletadas são armazenadas em uma memória de replay
- Amostragem de Experiências: Durante o treinamento, o agente amostra experiências da memória de replay em vez de usar as experiências mais recentes.
- Atualização do Modelo: O agente atualiza seu modelo (por exemplo, a função de valor Q ou a política) com base nas experiências amostradas da memória de replay.

#

## Chapter 9: Reinforcement Learning

### Concept:
It is a machine learning approach that relies on the concept of rewards and penalties to train agents to make decisions that seek the highest possible reward. It differs from supervised learning in that instead of the agent predicting the correct output based on known inputs, the agent will explore the environment and learn an optimal policy (a policy that maximizes the cumulative reward). Its main components are:
 - Agent: It is the entity that makes decisions and interacts with the environment.
 - Environment: It is the context in which the agent operates, it is the “space” where the problem is described.
 - Actions: These are the possible decisions that the agent must make (Go up, go down, observe, take, buy, sell…).
 - State: It is the representation of the environment at the current moment, each action of the environment agent generates a new state.
 - Reward: It is a measure of how well the agent is doing, based on the actions it takes.

### Some techniques:
#### Deep Q-learning:
It is a technique that combines deep neural networks (Deep Learning) with the Q-Learning* algorithm (algorithm that learns a value function q, which estimates the expected reward for action in each state) to train agents to make decisions that maximize a reward cumulative in an environment. Deep Q-Learning uses deep neural networks with the Q* value function, allowing the agent to learn from past experiences and make more accurate predictions about future reward. How it works:
- Initialization: The agent starts with a random policy (without a defined objective) and a randomly initialized Q-valued function.
- Exploration vs Exploitation: The agent explores the environment, taking random actions to collect experiences. As the agent collects more experiences, it begins to explore the environment less and begins to follow the actions that seem to be more promising (those that have greater value).
- Update of the Q value function: After each action, the agent updates the Q value function based on the reward received and the best action it could have taken in the next state, according to the current policy (which in this case would be seek to maximize the reward).
- Iteration: The process of exploring and updating the Q value function is repeated many times until the agent learns an optimal policy (the highest possible maximization).

<br>[Implementation Explained](https://colab.research.google.com/drive/1yav1jLsQXPAbk9bhRKCSrK8US75JR-Zd#scrollTo=sbORaqPO0noD)

#### Gradient Policy:
 It aims to optimize an agent's policy, which is the probability distribution over the actions that the agent should take in each state. It is an alternative approach to reinforcement learning with value. It directly optimizes the policy making them more efficient in terms of training times and effectiveness. It works by updating an agent's policy based on the gradient of the expected reward. The expected reward is the weighted average of future rewards, weighted by the current policy to maximize the expected reward. This process generally involves the following steps:
 - Exploration: The agent explores the environment, collecting experiences.
 - Evaluation: The policy is evaluated to determine the expected reward.
 - Update: The policy is updated to maximize the expected reward.
 - Iteration: The process is repeated until the policy converts to an optimal policy.

#### Reinforcement Learning with Entropy:
It is an extension of reinforcement learning that incorporates an entropy term into the loss function. Entropy is a measure of disorder or randomness in a data set, and in this context it is used to encourage exploration. By adding an entropy term to the loss function, the reinforcement learning algorithm is encouraged to explore a wider range of actions, rather than focusing on actions that are already known to produce high rewards. It can be particularly useful in environments where exploration is crucial to learning the optimal policy. It works by adding an entropy term to the loss function, which is calculated based on the probability distribution of the current policy. The goal is to maximize the expected reward (usually through the Q-value function or a direct policy) and minimize the entropy of the policy. This is done through an iterative process of adjusting policy parameters, where the policy is updated to maximize expected reward and minimize entropy. Like this:
- Exploration: The agent explores the environment, collecting experiences.
- Evaluation: The current policy is evaluated to determine the expected reward and entropy of the policy.
- Update: The policy is updated to maximize expected reward and minimize entropy.
- Iteration: The process is repeated until the policy converges to an optimal policy.

#### Effortful learning with experience:
Also known as effortful learning with replay memory, it is a learning technique that uses memory to store and reuse past experiences. The main idea is that, instead of learning directly from current states and their subsequent actions, the agent learns from states, actions and rewards stored in replay memory. Its advantages are:
- Training stability: By using past experience, reinforcement learning with experience can be more stable and less prone to fluctuations and instabilities that can occur during training.
- Efficiency: Replay memory allows the agent to learn from past experiences, which can be more efficient than learning directly from current states.
- Exploration: By using past experiences, the agent can explore a wide range of actions and states, even if these experiences are not immediately relevant to the current state.
How works:
- Collection of Experiences: The agent interacts with the environment, collecting experiences (states, actions, rewards and subsequent states).
- Storage in Replay Memory: Collected experiences are stored in a replay memory
- Experience Sampling: During training, the agent samples experiences from replay memory instead of using the most recent experiences.
- Model Update: The agent updates its model (e.g., the Q-value function or the policy) based on the experiences sampled from the replay memory.
