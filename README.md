# Trabalho final de Graduação (TFG) - Universidade Federal de Itajubá

## Link para a aplicação criada com o Streamlit

https://heartdiseasepredict.streamlit.app/

## Objetivos

O presente trabalho teve o objetivo de realizar uma análise exploratória em uma base de dados para a detecção de doenças cardíacas em um paciente, verificando a integridade e consistência dos dados. <br>
Logo após, foram usados algoritmos de aprendizado de máquina para realizar a classificação entre pessoas que possuem ou não uma doença cardíaca, levando em consideração os dados de entrada já analisados previamente. 
Diferentes algoritmos foram utilizados com a finalidade de verificar qual possuiria o melhor desempenho, levando em consideração diferentes métricas de avaliação para os modelos. <br>
Por fim, foi desenvolvida uma interface gráfica de usuário que poderá ser utilizada com os dados necessários para a classificação do paciente segundo sua condição cardíaca. 
Assim, o melhor modelo, fornecendo uma verificação inicial instantânea de alguma possível doença cardíaca, poderia ser usado antes do resultado dos exames.

## Metodologia

O conjunto de dados escolhido foi desenvolvido combinando 5 datasets, a partir de 11 características comuns, contendo 1190 entradas de dados, no total.<br>
Primeiramente, foi usada a biblioteca Pandas para realizar a análise exploratória, de modo a obter informações iniciais sobre os dados. <br>
Em seguida, usou-se a biblioteca Scikit Learn para a criação, processamento e validação dos modelos de aprendizado de máquina. <br>
Por fim, a biblioteca Streamlit foi empregada na construção de uma interface gráfica responsiva para utilização do melhor modelo.

## Resultados

Na etapa de análise, foi realizada a limpeza dos dados, removendo os registros com dados inconsistentes. Logo após, foram desenvolvidos gráficos com as variáveis de entrada, obtendo assim informações importantes sobre o dataset. Além disso, verificou-se o balanceamento na variável de saída, analisando o total de registros para cada classe. <br>
Para a criação dos modelos, os dados foram separados em conjuntos de treino e teste. Os modelos foram desenvolvidos de três maneiras: sem o pré-processamento dos dados, com os dados tratados e com um ajuste fino nos hiperparâmetros, tendo uma melhora significativa em cada uma das etapas. O melhor modelo foi obtido com o algoritmo de floresta aleatória, alcançando 91,95% de acurácia nos dados de teste.<br>
Por fim, usando o modelo citado anteriormente, uma interface web responsiva foi elaborada. Assim, com as informações necessárias, o preenchimento é fácil de ser realizado.
