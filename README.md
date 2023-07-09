<body>
  <header>
    <h1>Análise de Mobilidade dos Ônibus em Natal RN</h1>
  </header>
  
  <main>
    <h3>Introdução</h3>
    <p>
      O trabalho foi proposto pela disciplina de ANÁLISE DE REDES - IMD1155 e consiste em aplicar os conteúdos vistos nas aulas a um dataset escolhido pela dupla e assim escolhemos o Dataset publico disponibilizado pela prefeitura de Natal relacionado a os dados de transporte publico, focando nos dados de 2022 e através de um notebook do Google Colab.
    </p>
    <h3>Desenvolvimento</h3>
    <p>
      Realizamos como dito anteriormente o trabalho por meio de notebook do Google Colab, utilizando as bibliotecas:
    <pre><code>
      pandas
      matplotlib.pyplot
      networkx
    </code></pre>
      A partir do arquivo csv obtido nos [dados publicos](http://dados.natal.br), retiramos os valores nulos ou vazios e após isso criamos o grafo pela biblioteca networkx. Após a criação do grafo, partimos para as especificações do projeto, calculando a Matriz de adjacência, Diâmetro e periferia da rede, Esparsidade/Densidade da Rede, Assortatividade geral da rede e Histograma de distribuição empírica de grau com a biblioteca matplotlib.pyplot.
    <br>
      Assim partimos para os calculos de Coeﬁciente de clustering local para nós escolhidos (onde escolhemos ruas que consideramos que são maiores e com mais paradas), Coeﬁciente de clustering global, Componentes Conectados Fortemente e Componentes Conectados Fracamente. Por fim exibimos métodos de comparação tanto em terminal quanto tentativas graficas das metricas de Eigenvector centrality, Degree centrality, Closeness centrality e Betweenness centrality.
    <br>
      Também tentamos realizar outras analises utilizando a mesma biblioteca grafica matplotlib.pyplot e por fim realizamos duas exibições uma com pyvis e outra através do Gephi e que pode ser vista [aqui]()
    </p>
    <h3>Conclusões</h3>
    <p>
      A partir dos gráficos plotados e das análises realizadas podemos deduzir por exemplo quais são as ruas mais movimentadas da cidade, já que onde os ônibus mais passam em teoria teriam maiores demandas de transporte, tanto de publico quanto de privado como uber e carona, ao analisar os dados também conseguimos ver que a maioria das ruas movimentadas seriam as com maior concentração de centros de compra ou prédios de escritório. 
      <br>
      Também optamos por fazer analises extras explorando além das ruas que mais aparecem tanto na ida quanto na volta, os bairros que aparecem como nomes das linhas assim conseguindo ver quais são os mais explorados pelas linhas, também conseguimos ver a divisão da frota por empresa, media de passageiros mensal por empresa e por linha, além do perfil dos usuários que utilizam o transporte público. 
    </p>
  </main>
</body>

