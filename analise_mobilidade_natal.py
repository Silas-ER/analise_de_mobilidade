# -*- coding: utf-8 -*-
"""Analise_Mobilidade_Natal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1whsqhSwL64ybWqAEnjs9eaLxxMxOe_F6

# Projeto da Unidade 3 da matéria IMD1155 - ANÁLISE DE REDES

O projeto consiste na analise das rotas de ônibus de Natal - RN, utilizando como arestas as ruas dos centros urbanos de Natal e como vértices as trajetorias dos ônibus, também utilizaremos como peso a quantidade de viagens realizadas e/ou a bilhetagem de cada linha.

Realizamos os tratamento de dados em notebooks anteriores:


*   Bilhetagem:
    https://colab.research.google.com/drive/1LknJmhFLuACeentORA0jnbObAjg-lRIm?usp=sharing
*   Itinerarios:
    https://colab.research.google.com/drive/1uYQPaiYeO3_UbIWFVsA1SET7qRr1TsMX?usp=sharing
*   Paradas:
    https://colab.research.google.com/drive/1IMBHfsWi7Yh4_bbnkps0-LPEWarkn_Bb?usp=sharing

Instalação e importação das bibliotecas:
"""

!pip install networkx

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

"""Leitura do arquivo e exibição:"""

data = pd.read_csv('/content/drive/MyDrive/PROJETO_ANALISE_DE_REDES/ANALISADO/Itinerarios/itinerario_geral.csv')

data

"""Criando o grafo, e alocando as variaveis referentes aos nós e vértices:"""

#Criando o grafo direcionado
G = nx.DiGraph()

#Laço para adicionar nós e arestas usando o .loc para armazenar os dados referentes a cada coluna
for i in range(len(data)):
  empresa = data.loc[i, 'EMPRESA']
  linha = data.loc[i, 'LINHA']
  nome = data.loc[i, 'NOME']
  rotas = data.loc[i, 'ROTA']


  G.add_node(rotas)
  G.add_edge(rotas, linha)

#Obter as posições dos nós
pos = nx.spring_layout(G)

#Criar a figura do gráfico, onde fig e ax são as variaveis que recebem
#o retono da função de subplots
fig, ax = plt.subplots(figsize=(20, 18))

#Desenhar os nós
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=200, node_color='b', alpha=0.8)

#Desenhar as arestas
nx.draw_networkx_edges(G, pos, ax=ax, arrows=True, arrowstyle='->', arrowsize=10, edge_color='gray', alpha=0.8)

#Adicionar rótulos aos nós
nx.draw_networkx_labels(G, pos, font_size=3)

#Remover os eixos
ax.axis('off')

#Exibir o gráfico
plt.show()

"""Matriz Adjacência"""

adj_matrix = nx.to_numpy_array(G)
print(adj_matrix)

"""Diâmetro e periferia da rede:
*   Foi necessário a criação de um subgrafo pois os elementos não eram fortemente conectados.
*   Após isso foi calculado o diâmetro e periferia que indicaram sinais que: no subgrafo todos os nós estão desconcetados entre si e que pela periferia ser o 600 ele não está conectado a nenhum outro nó no subgrafo

"""

fortemente_conectados = list(nx.strongly_connected_components(G))

componentes_sconectados = max(fortemente_conectados, key=len)

subgrafo = G.subgraph(componentes_sconectados)

diametro = nx.diameter(subgrafo)
print("Diâmetro do subgrafo:", diametro)

periferia = nx.periphery(subgrafo)
print("Periferia do subgrafo:", periferia)

"""Indice de esparsidade da rede e assortatividade geral da rede:

*   Em relação a esparsidade de rede esse valor indica que é bastante esparsa e possui uma baixa densidade de conexões em relação ao máximo de possibilidades
*   Já a assortatividade negativa indica que os nós com graus diferentes tem maior probilidade de conexão


"""

esparsidade = nx.density(G)
print("Esparsidade da rede:", esparsidade)

assortatividade = nx.degree_assortativity_coefficient(G)
print("Assortatividade geral da rede:", assortatividade)

"""Histograma de distribuição empirica de grau:

"""

degree_sequence = [degree for _, degree in G.degree()]
#degree_sequence = [degree for node, degree in G.degree()]

plt.hist(degree_sequence, bins=10, alpha=0.8)

plt.xlabel('Grau')
plt.ylabel('Frequência')

plt.title('Histograma de Distribuição Empírica de Grau')

plt.show()

"""Calculo dos:
*   Coeﬁciente de clustering local para nós escolhidos.
*   Coeﬁciente de clustering global.
*   Componentes Conectados Fortemente, note que é preciso ter um grafo dirigido para gerar essa métrica.
*   Componentes Conectados Fracamente.

"""

no_selecionado = ['600', 'AV. ENGENHEIRO ROBERTO FREIRE', 'RUA ESTÂNCIA VELHA']

clustering_coeficiente = nx.clustering(G, no_selecionado)
print("Coeficiente de clustering local:")
for node, cc in clustering_coeficiente.items():
    print("Nó:", node, "- Coeficiente de clustering:", cc)

clustering_global = nx.average_clustering(G)
print("Coeficiente de clustering global:", clustering_global)

fortemente_conectados = list(nx.strongly_connected_components(G))
print("Componentes conectados fortemente:", fortemente_conectados)

# Componentes conectados fracamente
fracamente_conectados = list(nx.weakly_connected_components(G))
print("Componentes conectados fracamente:", fracamente_conectados)

"""- Implemente uma visualização para exibir os nós mais importantes, usando e comparando as medidas:
● Eigenvector centrality,
● Degree centrality.
● Closeness centrality.
● Betweenness centrality.
Confira para visualizações dos dados: https://datasciencedojo.com/blog/network-theory-game-of-thrones/

- Implemente o pacote de Detecção de comunidades/partições:
https://python-louvain.readthedocs.io/en/latest/index.html
"""

!pip install community
!pip install python-louvain

import networkx as nx
import community_louvain

# Criar o grafo utilizando o NetworkX
G = nx.DiGraph()

# Adicionar os nós e as arestas do seu dataset ao grafo
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)
# ...

# Caso o seu dataset já esteja em formato de lista de arestas, você pode usar:
# G = nx.read_edgelist('seu_dataset.txt')

# Converter o grafo para o formato esperado pelo pacote python-louvain
G = nx.Graph(G)

# Executar a detecção de comunidades utilizando o Louvain
partition = community_louvain.best_partition(G)

# Imprimir os rótulos de comunidade atribuídos aos nós
print(partition)

# Acessar os nós pertencentes a uma comunidade específica
community_0 = [node for node, community_label in partition.items() if community_label == 0]
print(community_0)