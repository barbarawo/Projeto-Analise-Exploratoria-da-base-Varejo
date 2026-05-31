# Projeto de Análise Exploratória da base de dados Varejo
Mini-Projeto Avaliativo do Curso de Análise de Dados com Python oferecido por SCTEC



## Contextualização do mini-projeto
Trata-se de projeto desenvolvido com o objetivo de realizar uma Análise Exploratória de Dados (AED) de varejo, utilizando a linguagem Python e as bibliotecas Pandas, NumPy, Matplotlib e Seaborn.

O propósito principal foi transformar dados brutos em informações úteis, permitindo a identificação de padrões, comportamentos e insights relevantes.

O mini-projeto teve como foco a aplicação prática de tarefas comuns na área de dados, tais como: identificar problemas nos dados fornecidos (valores nulos, tipos incorretos, duplicados), tratar essas inconsistências com ferramentas como pandas, gerar estatísticas simples e funções de agrupamento, para responder perguntas operacionais (quem compra mais, quais categorias vendem mais, como variam as vendas ao longo do tempo), além da criação de gráficos para a melhor visualização de insights.

A base de dados Varejo foi extraída da plataforma [Kaggle](https://www.kaggle.com/datasets/namespaiva/base-varejo/data)

A base contém registros de compras no varejo disponibilizados para fins de análise de dados, incluindo informações sobre datas, clientes, produtos, categorias e valores.

O projeto foi executado utilizando a IDE Visual Studio Code (VsCode) e contém comentários explicativos ao longo do código-fonte, detalhando o desenvolvimento da atividade e as escolhas adotadas no tratamento dos dados. Este documento complementa tal explicação.



## Dicionário de dados
A base de dados analisada é composta pelas seguintes variáveis:
|  Coluna      |  Descrição |
| ---------- | ------- |
|  DATA      | Data em que a compra foi realizada.
|  CO_ID     | Identificação da compra, correspondente ao número da nota fiscal.
|  CL_ID     | Identificação única do cliente.
|  CL_GENERO | Sexo biológico informado pelo cliente (Feminino ou Masculino).
|  CL_EC     | Estado civil do cliente.
|  CL_FHL    | Quantidade de filhos informada pelo cliente.
|  CL_SEG    | Segmentação econômica do cliente, classificada em classes A, B ou C.
|  PR_ID     | Código identificador do produto (SKU).
|  PR_CAT    | Categoria à qual o produto pertence.
|  PR_NOME   | Nome do produto adquirido.



## Objetivos executados no projeto
   - Análise prévia e importação da base de dados de varejo para IDE, evidenciando o número de registros, colunas e tipos de dados;
   - Identificação de inconsistências nos dados e realização de tratamentos, tais como transformação de strings, integer, float e datetime;
   - Aplicação de condicionais e/ou funções para limpeza ou imputação de dados nulos e remoção de registros duplicados;
   - Aplicação de funções de estatísticas descritivas básicas para coluna de número de filhos do cliente (CL_FHL), incluindo média, mediana, desvio padrão, moda, máximo, mínimo, contagem, além de quartis;
   - Explorar padrões por meio de, pelo menos, dois agrupamentos, utilizando groupby() e/ou pivot_table();
   - Construção de relatório final, contendo conclusões, insights e eventuais problemas remanescentes na base. A visualização gráfica para apoio da interpretação dos resultados é opcional, mas adotada no caso para melhor assertividade de entendimento do resultado.


