## Capítulo 13: Sistemas Multiagente
Sistemas multiagente (MAS, do inglês "Multi-Agent Systems") referem-se a sistemas compostos por múltiplos agentes interativos, onde cada agente é uma entidade autônoma capaz de perceber seu ambiente e tomar decisões independentes para atingir objetivos específicos. Esses agentes podem cooperar, competir ou negociar uns com os outros, dependendo de seus objetivos e das regras do sistema.

#### Principais Características:
- *Autonomia:* Cada agente possui sua própria capacidade de controle e não é necessário que sejam estritamente controlados por uma entidade central. Eles operam de forma independente com base em suas próprias percepções ou informações.
- *Interatividade:*  Os agentes em um MAS interagem uns com os outros através de comunicação ou observação direta de ações. A interação pode ser colaborativa, onde os agentes trabalham juntos para alcançar um objetivo comum, ou competitiva, onde eles têm objetivos conflitantes.
- *Racionalidade:* Os agentes são tipicamente projetados para operar de forma racional, ou seja, eles tomam decisões que maximizam suas chances de atingir seus objetivos, dados seus conhecimentos e capacidades.
- *Capacidade de resolução de problemas:* Os agentes em sistemas multiagente são capazes de resolver problemas complexos dividindo tarefas, compartilhando conhecimentos, ou negociando soluções.

#### Aplicações:
- *Robótica:* Sistemas de robôs que trabalham juntos em tarefas como montagem em fábricas ou exploração espacial.
- *Simulação de tráfego:* Simular o tráfego em grandes áreas urbanas, onde cada veículo ou pedestre pode ser modelado como um agente com comportamentos específicos.
- *Gerenciamento de recursos:* Aplicações em gerenciamento de energia, como na distribuição de eletricidade em smart grids, onde cada distribuidor de energia atua como um agente.
- *Jogos e entretenimento:* Criação de personagens ou entidades interativas em ambientes virtuais que podem interagir com jogadores humanos ou outros agentes de forma inteligente.

#### Desafios:
- *Coordenação:* Garantir que os agentes trabalhem juntos de forma eficaz sem conflitos desnecessários ou ineficiências.
- *Comunicação:* Desenvolver protocolos eficientes de comunicação que permitam aos agentes compartilhar informações de maneira oportuna e segura.
- *Negociação:* Criar métodos que permitam aos agentes negociar e chegar a acordos de maneira eficaz, especialmente em ambientes dinâmicos ou competitivos.

##

### Inteligência Artificial Distribuída
Inteligências Artificiais Distribuídas (IAD) são um ramo da inteligência artificial que foca no desenvolvimento de sistemas compostos por múltiplos agentes inteligentes que interagem em um ambiente compartilhado. Essa abordagem permite que tarefas complexas sejam divididas em sub-tarefas menores, que podem ser resolvidas de maneira cooperativa ou competitiva por diferentes agentes. Os agentes em um sistema de IAD podem ser autônomos e podem incluir tanto software (como programas de computador) quanto hardware (como robôs).

#### Principais Características:
- *Distribuição de Processamento:* Ao invés de centralizar o processamento em uma única unidade ou sistema, a IAD espalha o processamento através de vários agentes que podem estar localizados fisicamente em diferentes lugares.
- *Autonomia dos Agentes:* Cada agente em IAD possui capacidade de operar de forma independente, tomar decisões e realizar ações sem a necessidade de intervenção humana constante.
- *Cooperação entre Agentes:* Os agentes em um sistema de IAD muitas vezes precisam cooperar uns com os outros para alcançar objetivos comuns, partilhando informações e recursos.
- *Comunicação:* Os agentes em sistemas de IAD comunicam-se entre si usando protocolos definidos para trocar informações e coordenar ações.
- *Descentralização:* Ao invés de depender de uma entidade central para controle e decisão, IAD promove uma abordagem descentralizada, permitindo uma maior escalabilidade e flexibilidade.

#### Desafios:
- *Coordenação e Sincronização:* Manter os agentes sincronizados e coordenados, especialmente em ambientes dinâmicos e em tempo real, é um desafio significativo.
- *Complexidade de Comunicação:* Garantir uma comunicação eficiente e segura entre agentes distribuídos pode ser complicado, especialmente quando as redes são inseguras ou não confiáveis.
- *Escalabilidade:* À medida que o número de agentes em um sistema aumenta, gerenciar e escalonar o sistema se torna progressivamente mais desafiador.

##
### PADE
O PADE (Plataforma de Apoio ao Desenvolvimento de Sistemas Multiagentes baseados em Python) é uma ferramenta desenvolvida para facilitar a criação, execução e gerenciamento de sistemas multiagentes. Especificamente, é uma plataforma que permite aos desenvolvedores implementar agentes que podem comunicar-se e interagir uns com os outros em diferentes ambientes de execução.

#### Características:
- *Flexibilidade:* O PADE permite que os usuários criem sistemas multiagentes de acordo com suas necessidades específicas, oferecendo suporte a diferentes tipos de comunicação e interação entre agentes.
- *Baseado em Python:* Por ser baseado em Python, o PADE tira proveito da facilidade de uso e da vasta biblioteca de recursos do Python, tornando mais acessível a programação de sistemas complexos.
- *Comunicação Eficiente:* Os agentes no PADE podem comunicar-se usando o protocolo de comunicação ACL (Agent Communication Language), que é padrão na indústria para sistemas multiagentes e facilita a troca de mensagens de maneira estruturada e compreensível.
- *Ambiente de Desenvolvimento Integrado:* O PADE oferece um ambiente que facilita o desenvolvimento, a depuração e o teste de agentes multiagentes, o que ajuda os desenvolvedores a criar sistemas mais robustos e eficientes.
- *Suporte para Execução Distribuída:* A plataforma permite a execução distribuída de agentes em diferentes máquinas ou processos, o que é essencial para sistemas escaláveis e distribuídos geograficamente.

#### Aplicações:
- *Automação Industrial:* Sistemas multiagentes podem ser utilizados para gerenciar processos complexos em fábricas, onde diferentes agentes controlam diferentes partes do processo de produção.
- *Pesquisa Acadêmica:* O PADE é frequentemente usado em contextos acadêmicos para pesquisa em sistemas multiagentes, permitindo a simulação de cenários complexos e o teste de teorias em um ambiente controlado.
- *Desenvolvimento de Software Distribuído:* Empresas que desenvolvem software que requer alta disponibilidade e distribuição podem usar o PADE para gerenciar a complexidade associada à comunicação e coordenação entre diferentes componentes de software.

#### Benefícios:
- *Redução do Tempo de Desenvolvimento:* A utilização de uma plataforma como o PADE pode diminuir significativamente o tempo necessário para desenvolver e implementar sistemas multiagentes.
- *Aumento da Confiabilidade:* A padronização da comunicação entre agentes e o ambiente integrado para testes contribuem para a criação de sistemas mais confiáveis.
- *Escalabilidade:* Com o suporte para execução distribuída, os sistemas desenvolvidos no PADE podem ser facilmente escalados para lidar com um maior volume de dados ou uma maior complexidade de processamento.

##
### Comunicação entre Agentes
#### Protocolos:
Agentes em sistemas multiagentes frequentemente utilizam protocolos de comunicação pré-definidos para trocar mensagens. Esses protocolos estipulam como as mensagens devem ser formatadas, enviadas e recebidas, garantindo uma comunicação eficiente e entendível entre agentes.

#### Linguagem de Comunicação de Agentes (ACL)
Uma das linguagens mais comuns é a ACL (Agent Communication Language), desenvolvida pela Foundation for Intelligent Physical Agents (FIPA). ACL permite que agentes troquem mensagens que não apenas transmitem dados, mas também intenções, como solicitações, informações, confirmações, e negociações. Cada mensagem ACL pode incluir:
- *Performative:* O tipo da ação que a mensagem está realizando (por exemplo, informar, perguntar, solicitar).
- *Content:* O conteúdo real da mensagem, que pode ser dados, uma query ou um comando.
- *Sender/Receiver:* Identificações do emissor e do receptor.
- *Language:* O idioma em que o conteúdo da mensagem é codificado (como SL ou Prolog).
- *Ontology:* O contexto ou o domínio de conhecimento ao qual a mensagem se refere.

#### Protocolos de Interação
Além dos formatos de mensagem, agentes muitas vezes seguem protocolos de interação que definem a sequência e o comportamento das mensagens em uma conversação. Exemplos incluem:
- *Contract Net Protocol:* Um protocolo para negociação em que um agente (o iniciador) envia um convite para outros agentes (participantes) para fazerem propostas para uma tarefa. O agente então seleciona a melhor proposta.
- *English Auction Protocol:* Um protocolo de leilão em que o preço é aumentado progressivamente até que apenas um participante esteja disposto a pagar o preço solicitado.

#### Middleware de Agentes
Muitos sistemas multiagentes utilizam uma camada de middleware que facilita a comunicação entre os agentes, independentemente de suas localizações ou das plataformas subjacentes. Esses middlewares gerenciam a transmissão de mensagens, roteamento, e podem até lidar com aspectos de segurança e autenticação.

#### Sincronização e Timing
Em muitos casos, a comunicação entre agentes também precisa ser sincronizada, especialmente em ambientes dinâmicos onde o timing da informação pode ser crítico para a tomada de decisão.

#### Comunicação Indireta
Em alguns sistemas, agentes podem também comunicar-se de maneira indireta através do ambiente, um conceito conhecido como stigmergy. Isso é comum em simulações de colônias de formigas, onde as formigas (agentes) comunicam-se através de feromônios no ambiente, em vez de trocar mensagens diretas.<br>
FIPA (Foundation for Intelligent Physical Agents) é uma organização que estabelece padrões para sistemas multiagente, incluindo protocolos de comunicação entre agentes. Três protocolos importantes desenvolvidos pela FIPA são o FIPA Request, o FIPA Contract-Net e o FIPA Subscribe. Vamos explorar cada um desses protocolos, explicando como funcionam e onde são usados.

##### FIPA-REQUEST:
O protocolo FIPA Request é um dos protocolos básicos para interações entre agentes. Ele é usado para solicitar a execução de uma ação por parte de um agente destinatário. Este protocolo segue uma estrutura simples, com um agente solicitando uma ação a outro e esperando uma resposta sobre o resultado dessa ação. Funcionamento:
- *Solicitação:* O agente solicitante envia uma mensagem de pedido para um agente receptor, especificando a ação que deve ser realizada.
- *Aceitação ou Recusa:* O agente receptor pode aceitar ou recusar o pedido. Se aceitar, ele tenta realizar a ação solicitada.
- *Resultado:* O agente receptor responde ao solicitante com o resultado da ação, indicando sucesso ou falha, ou fornecendo alguma informação adicional, se aplicável.

**Aplicações do FIPA Request:**
- Usado quando um agente deseja que outro agente execute uma tarefa específica ou forneça informações.
- Pode ser utilizado para solicitar serviços ou recursos em um sistema multiagente.

##### FIPA Contract-Net:
O FIPA Contract-Net é um protocolo mais complexo, projetado para alocação de tarefas por meio de um processo de negociação. Ele é frequentemente usado em cenários onde um agente precisa encontrar o melhor agente para realizar uma tarefa, como em sistemas de contratação ou leilões. Funcionamento:
- *Anúncio:* O agente iniciador envia uma proposta para vários agentes, convidando-os a enviar propostas para realizar uma tarefa.
- *Propostas:* Os agentes que recebem o convite podem enviar suas propostas ao agente iniciador, indicando seu interesse e a forma como pretendem executar a tarefa.
- *Avaliação e Seleção:* O agente iniciador avalia as propostas recebidas e escolhe a melhor (ou as melhores), com base em critérios como custo, tempo de execução, ou outros fatores.
- *Aceitação ou Rejeição:* O agente iniciador aceita a proposta escolhida e rejeita as outras. Os agentes cujas propostas foram rejeitadas recebem um aviso de rejeição.
- *Execução:* O agente selecionado executa a tarefa e reporta o resultado ao agente iniciador.

**Aplicações do FIPA Contract-Net:**
- Ideal para processos de leilão, onde um agente precisa escolher entre várias propostas.
- Usado para alocação de tarefas em sistemas multiagente, como em robótica ou sistemas de gerenciamento de recursos.

##### FIPA Subscribe:
O FIPA Subscribe é um protocolo usado quando um agente quer se inscrever para receber notificações ou atualizações de outro agente sobre eventos ou informações específicas. Esse protocolo é útil quando um agente deseja monitorar uma fonte de dados ou receber alertas sobre mudanças em um sistema. Funcionamento:
- *Inscrição:* O agente solicitante envia uma mensagem de inscrição ao agente destinatário, indicando o que ele deseja monitorar ou para o que ele quer ser notificado.
- *Confirmação ou Rejeição:* O agente destinatário pode aceitar ou rejeitar a inscrição. Se aceitar, ele mantém uma lista de inscritos e envia notificações quando ocorrerem eventos relevantes.
- *Notificações:* O agente destinatário envia mensagens de notificação aos inscritos quando eventos ou mudanças significativas ocorrem.

**Aplicações do FIPA Subscribe:**
- Ideal para cenários de monitoramento, como em sistemas de vigilância ou em fluxos de dados em tempo real.
- Pode ser usado para alertas e notificações em sistemas de gestão de eventos.

#

## Chapter 13: Multiagent Systems
Multi-Agent Systems (MAS) refer to systems composed of multiple interacting agents, where each agent is an autonomous entity capable of perceiving its environment and making independent decisions to achieve specific objectives. These agents can cooperate, compete or negotiate with each other, depending on their objectives and the rules of the system.

#### Main features:
- *Autonomy:* Each agent has its own control capacity and it is not necessary for them to be strictly controlled by a central entity. They operate independently based on their own perceptions or information.
- *Interactivity:* Agents in a MAS interact with each other through communication or direct observation of actions. Interaction can be collaborative, where agents work together to achieve a common goal, or competitive, where they have conflicting goals.
- *Rationality:* Agents are typically designed to operate rationally, that is, they make decisions that maximize their chances of achieving their objectives, given their knowledge and capabilities.
- *Problem-solving ability:* Agents in multi-agent systems are able to solve complex problems by dividing tasks, sharing knowledge, or negotiating solutions.

#### Applications:
- *Robotics:* Systems of robots that work together on tasks such as assembly in factories or space exploration.
- *Traffic simulation:* Simulate traffic in large urban areas, where each vehicle or pedestrian can be modeled as an agent with specific behaviors.
- *Resource management:* Applications in energy management, such as electricity distribution in smart grids, where each energy distributor acts as an agent.
- *Games and entertainment:* Creation of characters or interactive entities in virtual environments that can interact with human players or other agents in an intelligent way.

#### Challenges:
- *Coordination:* Ensure that agents work together effectively without unnecessary conflicts or inefficiencies.
- *Communication:* Develop efficient communication protocols that allow agents to share information in a timely and secure manner.
- *Negotiation:* Create methods that allow agents to negotiate and reach agreements effectively, especially in dynamic or competitive environments.

##
### Distributed Artificial Intelligence
Distributed Artificial Intelligence (IAD) is a branch of artificial intelligence that focuses on the development of systems composed of multiple intelligent agents that interact in a shared environment. This approach allows complex tasks to be divided into smaller sub-tasks, which can be solved cooperatively or competitively by different agents. Agents in an IAD system can be autonomous and can include both software (such as computer programs) and hardware (such as robots).

#### Main features:
- *Processing Distribution:* Instead of centralizing processing in a single unit or system, IAD spreads processing across several agents that can be physically located in different places.
- *Agent Autonomy:* Each agent in IAD has the ability to operate independently, make decisions and carry out actions without the need for constant human intervention.
- *Cooperation between Agents:* Agents in an IAD system often need to cooperate with each other to achieve common goals, sharing information and resources.
- *Communication:* Agents in IAD systems communicate with each other using defined protocols to exchange information and coordinate actions.
- *Decentralization:* Instead of relying on a central entity for control and decision-making, IAD promotes a decentralized approach, allowing for greater scalability and flexibility.

#### Challenges:
- *Coordination and Synchronization:* Keeping agents synchronized and coordinated, especially in dynamic and real-time environments, is a significant challenge.
- *Communication Complexity:* Ensuring efficient and secure communication between distributed agents can be complicated, especially when networks are insecure or unreliable.
- *Scalability:* As the number of agents in a system increases, managing and scaling the system becomes progressively more challenging.

##
### PADE
PADE (Support Platform for the Development of Multi-Agent Systems based on Python) is a tool developed to facilitate the creation, execution and management of multi-agent systems. Specifically, it is a platform that allows developers to implement agents that can communicate and interact with each other in different execution environments.

#### Characteristics:
- *Flexibility:* PADE allows users to create multi-agent systems according to their specific needs, supporting different types of communication and interaction between agents.
- *Based on Python:* Being based on Python, PADE takes advantage of Python's ease of use and vast library of resources, making programming complex systems more accessible.
- *Efficient Communication:* Agents in PADE can communicate using the ACL (Agent Communication Language) communication protocol, which is an industry standard for multi-agent systems and facilitates the exchange of messages in a structured and understandable way.
- *Integrated Development Environment:* PADE offers an environment that facilitates the development, debugging and testing of multi-agent agents, which helps developers create more robust and efficient systems.
- *Support for Distributed Execution:* The platform allows distributed execution of agents on different machines or processes, which is essential for scalable and geographically distributed systems.

#### Applications:
- *Industrial Automation:* Multi-agent systems can be used to manage complex processes in factories, where different agents control different parts of the production process.
- *Academic Research:* PADE is often used in academic contexts for research into multi-agent systems, allowing the simulation of complex scenarios and the testing of theories in a controlled environment.
- *Distributed Software Development:* Companies that develop software that requires high availability and distribution can use PADE to manage the complexity associated with communication and coordination between different software components.

#### Benefits:
- *Reduction in Development Time:* Using a platform like PADE can significantly reduce the time needed to develop and implement multi-agent systems.
- *Increased Reliability:* The standardization of communication between agents and the integrated testing environment contribute to the creation of more reliable systems.
- *Scalability:* With support for distributed execution, systems developed in PADE can be easily scaled to deal with a greater volume of data or greater processing complexity.

##
### Communication between Agents
#### Protocols:
Agents in multi-agent systems often use predefined communication protocols to exchange messages. These protocols stipulate how messages should be formatted, sent and received, ensuring efficient and understandable communication between agents.

#### Agent Communication Language (ACL)
One of the most common languages ​​is ACL (Agent Communication Language), developed by the Foundation for Intelligent Physical Agents (FIPA). ACL allows agents to exchange messages that not only convey data, but also intentions, such as requests, information, confirmations, and negotiations. Each ACL message can include:
- *Performative:* The type of action the message is performing (e.g. inform, ask, request).
- *Content:* The actual content of the message, which can be data, a query or a command.
- *Sender/Receiver:* Identifications of the sender and receiver.
- *Language:* The language in which the message content is encoded (such as SL or Prolog).
- *Ontology:* The context or domain of knowledge to which the message refers.

#### Interaction Protocols
In addition to message formats, agents often follow interaction protocols that define the sequence and behavior of messages in a conversation. Examples include:
- *Contract Net Protocol:* A protocol for negotiation in which an agent (the initiator) sends an invitation to other agents (participants) to make proposals for a task. The agent then selects the best proposal.
- *English Auction Protocol:* An auction protocol in which the price is progressively increased until only one participant is willing to pay the requested price.

#### Agent Middleware
Many multi-agent systems use a middleware layer that facilitates communication between agents, regardless of their locations or the underlying platforms. These middlewares manage message transmission, routing, and can even handle security and authentication aspects.

#### Synchronization and Timing
In many cases, communication between agents also needs to be synchronized, especially in dynamic environments where the timing of information can be critical for decision making.

#### Indirect Communication
In some systems, agents can also communicate indirectly through the environment, a concept known as stigmergy. This is common in ant colony simulations, where ants (agents) communicate through pheromones in the environment, rather than exchanging direct messages.<br>
FIPA (Foundation for Intelligent Physical Agents) is an organization that establishes standards for multi-agent systems, including communication protocols between agents. Three important protocols developed by FIPA are FIPA Request, FIPA Contract-Net and FIPA Subscribe. Let's explore each of these protocols, explaining how they work and where they are used.

##### FIPA-REQUEST:
The FIPA Request protocol is one of the basic protocols for interactions between agents. It is used to request the execution of an action by a recipient agent. This protocol follows a simple structure, with one agent requesting an action from another and waiting for a response about the result of that action. Operation:
- *Request:* The requesting agent sends a request message to a receiving agent, specifying the action that must be performed.
- *Acceptance or Refusal:* The receiving agent can accept or reject the request. If it accepts, it tries to perform the requested action.
- *Result:* The receiving agent responds to the requester with the result of the action, indicating success or failure, or providing some additional information, if applicable.

**FIPA Request Applications:**
- Used when an agent wants another agent to perform a specific task or provide information.
- Can be used to request services or resources in a multi-agent system.

##### FIPA Contract-Net:
FIPA Contract-Net is a more complex protocol designed for task allocation through a negotiation process. It is often used in scenarios where an agent needs to find the best agent to perform a task, such as in contracting systems or auctions. Operation:
- *Advertisement:* The initiating agent sends a proposal to several agents, inviting them to submit proposals to perform a task.
- *Proposals:* Agents who receive the invitation can send their proposals to the initiating agent, indicating their interest and how they intend to carry out the task.
- *Evaluation and Selection:* The initiating agent evaluates the proposals received and chooses the best one (or the best ones), based on criteria such as cost, execution time, or other factors.
- *Acceptance or Rejection:* The initiating agent accepts the chosen proposal and rejects the others. Agents whose proposals are rejected receive a rejection notice.
- *Execution:* The selected agent executes the task and reports the result to the initiating agent.

**FIPA Contract-Net applications:**
- Ideal for auction processes, where an agent needs to choose between several proposals.
- Used for task allocation in multi-agent systems, such as in robotics or resource management systems.

##### FIPA Subscribe:
FIPA Subscribe is a protocol used when an agent wants to subscribe to receive notifications or updates from another agent about specific events or information. This protocol is useful when an agent wants to monitor a data source or receive alerts about changes to a system. Operation:
- *Registration:* The requesting agent sends a subscription message to the receiving agent, indicating what he wants to monitor or what he wants to be notified for.
- *Confirmation or Rejection:* The recipient agent can accept or reject the application. If you accept, it maintains a list of subscribers and sends notifications when relevant events occur.
- *Notifications:* The recipient agent sends notification messages to subscribers when significant events or changes occur.

**FIPA Subscribe Applications:**
- Ideal for monitoring scenarios, such as surveillance systems or real-time data streams.
- Can be used for alerts and notifications in event management systems.
