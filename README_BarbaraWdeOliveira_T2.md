

# Projeto de Análise Exploratória da base de dados Varejo

________________________________________
### 📑 Contextualização do mini-projeto
<p align="justify">Trata-se de projeto desenvolvido com o objetivo de realizar uma Análise Exploratória de Dados (AED) de varejo, utilizando a linguagem Python e as bibliotecas Pandas, NumPy, Matplotlib e Seaborn.</p>

<p align="justify">O propósito principal foi transformar dados brutos em informações úteis, permitindo a identificação de padrões, comportamentos e insights relevantes.</p>

<p align="justify">O mini-projeto teve como foco a aplicação prática de tarefas comuns na área de dados, tais como: identificar problemas nos dados fornecidos (valores nulos, tipos incorretos, duplicados), tratar essas inconsistências com ferramentas como pandas, gerar estatísticas simples e funções de agrupamento, para responder perguntas operacionais (quem compra mais, quais categorias vendem mais, como variam as vendas ao longo do tempo), além da criação de gráficos para a melhor visualização de insights.</p>

<p align="justify">A base de dados Varejo foi extraída da plataforma [Kaggle](https://www.kaggle.com/datasets/namespaiva/base-varejo/data)</p>

<p align="justify">A base contém registros de compras no varejo disponibilizados para fins de análise de dados, incluindo informações sobre datas, clientes, produtos, categorias e valores.</p>

<p align="justify">O projeto foi executado utilizando a IDE Visual Studio Code (VsCode) e contém comentários explicativos ao longo do código-fonte, detalhando o desenvolvimento da atividade e as escolhas adotadas no tratamento dos dados. Este documento complementa tal explicação.</p>



________________________________________
### 📌 Dicionário de dados
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


________________________________________
### 🎯 Objetivos executados no projeto
- Análise prévia e importação da base de dados de varejo para IDE, evidenciando o número de registros, colunas e tipos de dados;
  
- Identificação de inconsistências nos dados e realização de tratamentos, tais como transformação de strings, integer, float e datetime;
  
- Aplicação de condicionais e/ou funções para limpeza ou imputação de dados nulos e remoção de registros duplicados;
  
- <p align="justify">Aplicação de funções de estatísticas descritivas básicas para coluna de número de filhos do cliente (CL_FHL), incluindo média, mediana, desvio padrão, moda, máximo, mínimo, contagem, além de quartis;</p>
  
- Explorar padrões por meio de, pelo menos, dois agrupamentos, utilizando groupby() e/ou pivot_table();
  
- <p align="justify">Construção de relatório final, contendo conclusões, insights e eventuais problemas remanescentes na base. A visualização gráfica para apoio da interpretação dos resultados é opcional, mas adotada no caso para melhor assertividade de entendimento do resultado.</p>

________________________________________
### 💻 Estrutura do projeto
```
Projeto/
│     
├── Base Varejo_limpo.csv             # Dados limpos após tratamento
├── Base Varejo.csv                   # Dados originais, sem tratamento
├── compras_categoria_genero.png      # Gráfico gerado no projeto
├── mini_projeto_avaliativo.py        # Código-fonte principal do projeto
├── README_BarbaraWdeOliveira_T2.md   # Documentação principal e completa explicando o projeto
├── README.md                         # Documentação da tela principal do GitHub remetendo ao arquivo completo
```

________________________________________
### ⚡ Como rodar o projeto

1. Abra o terminal na IDE VsCode, através do menu Terminal > Novo Terminal. Em seguida, execute o seguinte comando:

       git clone https://github.com/barbarawo/Projeto-Analise-Exploratoria-da-base-Varejo.git
                
2.	Acesse a pasta do projeto através do comando:

        cd Projeto-Analise-Exploratoria-da-base-Varejo
  	
3.	Caso não possua, instale as bibliotecas necessárias para a correta execução do projeto no terminal do VsCode:

        pip install pandas numpy matplotlib seaborn
   
4.	Execute o script do projeto também pelo terminal do VsCode:

        python mini_projeto_avaliativo.py
  	
5.	Por fim, será possível visualizar:
   
        O relatório estatístico no próprio terminal do VsCode;
        O arquivo CSV com os dados tratados ("limpos");
        Um gráfico de barras para visualização de compras por categoria e gênero.
  	
________________________________________
### ▶️🧹 Etapas de desenvolvimento do projeto e tratamento de dados

**1. Importação das bibliotecas e leitura do arquivo CSV**

A primeira etapa do script do código-fonte consiste na importação das bibliotecas necessárias para a execução do projeto. Utilizou-se:
* Pandas, para manipulação de dados tabulares;
* NumPy, para operações numéricas;
* Matplotlib, para criação do gráfico; e
* Seaborn, usado também para a criação do gráfico. 

<p align="justify">Em seguida, foi realizada a leitura da base de dados utilizando a função read_csv() do Pandas, considerando o separador de colunas utilizado no arquivo (;) e a codificação UTF-8 (Brasil, em razão de possível acentuação gráfica).


**2.	Diagnóstico preliminar**
<p align="justify">Antes de qualquer tratamento, foi criada uma função denominada diagnostico(), responsável por apresentar informações gerais sobre a qualidade dos dados.
A função exibe:
   
* Quantidade de linhas e colunas;
* Número de registros duplicados;
* Tipo de dado de cada coluna;
* Quantidade e percentual de valores nulos por coluna. 

<p align="justify">Tal diagnóstico permitiu identificar inconsistências existentes na base, servindo como ponto de partida para as etapas de limpeza e preparação dos dados. Durante essa etapa foram identificados:

* 830.000 registros;
* 14 colunas; 
* 96.553 registros duplicados; 
* 4 colunas contendo 100% de valores nulos (Unnamed: 10, Unnamed: 11, Unnamed: 12 e Unnamed: 13). 

**3. Remoção das colunas irrelevantes/nulas**
<p align="justify">Considerando a constatação de 4 colunas com valores integralmente nulos, estas foram removidas por não agregarem valores para análise.

**4. Padronização de dados**
<p align="justify">Para evitar inconsistências em razão de espaços invisíveis e formatação (maiúsculo/minúsculo), padronizou-se as colunas PR_CAT e PR_NOME.

**5. Valores ausentes e/ou nulos**
<p align="justify">Em análise preliminar, verificou-se a existência de linhas com valores "#N/D". Para evitar inconsistências, transformou-se "'#N/D', '#n/d', 'NULL', '', ' '" para o padrão NaN do Pandas.

<p align="justify">Importante registrar que como as colunas PR_CAR e PR_NOME são relevantes para a análise de vendas no varejo, optou-se pela imputação de valores ausentes utilizando a categoria "não informado", ao invés de sua remoção, preservando a quantidade de registros ausentes existentes na base para posterior identificação individualizada.

<p align="justify">A mesma lógica conservativa foi utilizada na coluna CF_FHL, que corresponde ao número de filhos do cliente. Todas as informações foram convertidas para formato numérico e caso algum valor inválido fosse constatado, seria transformado para o padrão NaN do Pandas. Para, em seguida, ser substituído por zero.

**6. Conversão da coluna DATA**
<p align="justify">A coluna DATA foi convertida para o tipo datetime, respeitando o formato brasileiro (dia/mês/ano), conforme requisitado pelo enunciado da atividade avaliativa.
   
<p align="justify">O parâmetro "errors='coerce'" garante que datas inválidas sejam convertidas para valores nulos (NaT), permitindo sua identificação. Em seguida foi realizada a verificação da quantidade de datas inválidas, cujo resultado constatou a inexistência de datas inválidas na base Varejo analisada.

**7. Remoção de duplicatas**
<p align="justify">O diagnóstico inicial identificou 96.553 registros duplicados, razão pela qual foi adotado o critério de considerar como duplicidade registros que possuíssem simultaneamente mesmo cliente (CL_ID), mesmo produto (PR_ID) e mesma data (DATA), sendo mantida apenas a primeira ocorrência.
   
Com a remoção das duplicatas, a base passou a conter 729.234 registros válidos.

**8. Transformação da coluna CL_EC**
<p align="justify">Constatou-se em diagnóstico inicial que a coluna CL_EC estava classificada como "int64" (números inteiros). À vista disso, para melhor interpretação dos dados, converteu-se os números para strings com as respectivas descrições, visando especialmente a análise de agrupamentos posterior.

Em seguida, reindexou-se a base para melhor organização da estrutura dos dados.

**9. Estatísticas**
<p align="justify">Após a limpeza e padronização dos dados, conforme requisitado no enunciado da atividade avaliativa, foi realizada uma análise estatística descritiva básica da coluna CL_FHL (quantidade de filhos do cliente), através da função describe(), objetivando a identificação de características dos clientes.
   
<p align="justify">Realizou-se, também, de forma manual e individualizada, as estatísticas de média, mediana, desvio padrão, moda, máximo, mínimo, contagem e quartis.

**10. Análise exproratória**
<p align="justify">Em seguida, utilizou-se as funções groupby() e pivot_table() para identificar padrões de comportamento dos clientes, o que demonstrou uma participação levemente maior do público feminino nas compras registradas e também permitiu identificar os produtos com maiores vendas dentro da base analisada.
   
<p align="justify">A função pivot_table() permitiu aprofundar a análise de quais categorias possuem maior participação masculina ou feminina, para identificar o perfil de consumo por categoria de produto, sendo ordenadas de forma decrescente conforme o volume de compras.

**11. Exportação da base tratada**

Com todas as etapas acima finalizadas, a base foi exportada para um novo arquivo .CSV nomeado como "Base Varejo_limpo".

**12. Visualização de dados**
<p align="justify">Por fim, embora opcional, preferiu-se desenvolver um gráfico de barras agrupadas, utilizando as bibliotecas Matplotlib e Seaborn, para facilitar a interpretação dos resultados.
O gráfico demonstra:
   
* Categorias de produtos no eixo horizontal;
* Quantidade de compras no eixo vertical;
* Separação por gênero (masculino e feminino) e por cor.


Antes da exibição em tela, o gráfico é salvo na estrutura do projeto como "compras_categoria_genero.png".

________________________________________
### 📐 Gráfico
![Gráfico](https://github.com/barbarawo/Projeto-Analise-Exploratoria-da-base-Varejo/blob/main/compras_categoria_genero.png)

________________________________________
### ✨ Conclusões
<p align="justify">A análise exploratória permitiu concluir pela predominância de compras de categorias recorrentes, sendo o maior volume em ordem decrescente de alimentos, higiene e limpeza. Disso se extrai que a base de dados é essencialmente contemplada por registros de consumo do dia a dia dos clientes.
  
Por sua vez, a análise por gênero evidenciou que a maior quantidade de compras registradas na base foram realizadas por mulheres.

Da coluna CL_EC (estado civil) se extrai a predominância de clientes casados ou em união estável.

<p align="justify">Outrossim, é possível deduzir da coluna CL_SEG (segmentação econômica) que os clientes casados da classe B representam os clientes com maior quantidade de registros na base.

________________________________________
### 🚀 Insights

1. <p align="justify">Através do agrupamento foi possível verificar que a categoria de alimentos representa o maior volume de vendas nos dois gêneros;
2. Embora ligeiramente superior o público feminino, o público masculino também representa grande volume de compras;
3. <p align="justify">A estatística descritiva demonstra concentração de clientes sem filhos (moda = 0), contudo, a média de 1,14 indica que famílias maiores influenciam o resultado geral;
4. <p align="justify">A transformação de dados em "não informado" foi a melhor decisão, demonstrando que representam uma pequena parcela da base, sem comprometer o resultado final.

________________________________________
### 👥 Contato
Estou à disposição para dúvidas ou sugestões.

_Mini-Projeto elaborado como atividade avaliativa do Curso de Análise de Dados com Python oferecido pela SCTEC em parceria com o SENAI._

Jun/2026.
