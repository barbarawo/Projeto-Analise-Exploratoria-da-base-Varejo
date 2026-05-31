import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Sprint 1 - Importação dos dados
#Sprint 2 - Transformação de Strings, Integer e Float e Datetime
#Sprint 3 - Limpeza de Nulos e Duplicatas
#Sprint 4 - Estatística Descritiva
#Sprint 5 - Relatório e Documentação
#Sprint 6 - Versionamento

df = pd.read_csv("Base Varejo.csv", sep=";", encoding='utf-8') #lendo CSV de um arquivo brasileiro

# Mostrar: número de registros, colunas e tipos de dados
def diagnostico(df, nome="Analise"):
    """
    Mostra um relatório completo de qualidade dos dados.
    Use sempre antes de começar a limpeza!
    """
    print("=" * 55)
    print(f"  📊 DIAGNÓSTICO: {nome}")
    print("=" * 55)
    print(f"  Linhas:           {df.shape[0]:,}")
    print(f"  Colunas:          {df.shape[1]}")
    print(f"  Linhas duplicadas:{df.duplicated().sum():,}") #verificar linhas duplicadas
    print()
    
    nulos = df.isnull().sum() #verificar nulos por colunas
    pct   = (nulos / len(df) * 100).round(1)
    
    print("  Coluna           | Tipo       | Nulos | % Nulos")
    print("  " + "-"*50)
    for col in df.columns:
        tipo = str(df[col].dtype)
        print(f"  {col:<18}| {tipo:<10} | {nulos[col]:<5} | {pct[col]}%")
    print("=" * 55)

diagnostico(df, "Dados analisados") #Rodando o diagnóstico

#Verificar e reportar ao menos dois problemas básicos:
#valores nulos por coluna, duplicatas e possíveis inconsistências
#(ex.: datas inválidas ou categorias vazias)

#Fazer as três etapas de limpeza mínima necessária:
#remover ou imputar nulos (explique a escolha),
#eliminar duplicatas relevantes e
#ajustar tipos de dados (ex.: converter coluna DATA para datetime).


print(df.columns) #Visualizar colunas

#Remover colunas com valores 100% nulos em float
df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])
print(f"Colunas após limpeza: {list(df.columns)}")


#Possíveis inconsistências, normalização colunas PR_CAT e PR_NOME
df['PR_CAT'] = df['PR_CAT'].str.strip().str.lower() #remover espaços invisíveis no início e fim, e colocar minúsculo

df['PR_NOME'] = df['PR_NOME'].str.strip().str.lower() #remover espaços invisíveis no início e fim, e colocar minúsculo


#Possíveis inconsistências, n/d, nulos
df[['PR_CAT', 'PR_NOME']] = df[['PR_CAT', 'PR_NOME']].replace(['#N/D', '#n/d', 'NULL', '', ' '], np.nan)

df['PR_CAT'] = df['PR_CAT'].fillna('não informado') #Imputação de nulos (não remove linhas); minúsculo, pois é o padrão utilizado
df['PR_NOME'] = df['PR_NOME'].fillna('não informado')

print("\nDistribuição após tratamento:")
print(df['PR_CAT'].value_counts(dropna=False))
print(df['PR_NOME'].value_counts(dropna=False))

df['CL_FHL'] = pd.to_numeric(df['CL_FHL'], errors='coerce') #Se houve nulos na coluna CL_FHL converte para 0 para posterior estatística
df['CL_FHL'] = df['CL_FHL'].fillna(0).astype(int)


# Datetime - Data no formato brasileiro DD/MM/AAAA
df['DATA'] = pd.to_datetime(
    df['DATA'],
    dayfirst=True,
    errors='coerce'
)

print("Datas inválidas:") #datas impossíveis viram NaT (nulo de data)
print(df['DATA'].isna().sum())


df = df.drop_duplicates(subset=['CL_ID', 'PR_ID', 'DATA'], keep='first') #Remover duplicatas, mantendo apenas a primeira aparição
print(f"Registros após remoção de duplicatas: {len(df):,}")  #Aponta o total de linhas após a remoção de duplicatas

#Alterando coluna CL_EC de int por categorias str
map_ec = {
    1: "Casado/União estável",
    2: "Divorciado",
    3: "Separado",
    4: "Solteiro",
    5: "Viúvo"
}
df['CL_EC'] = df['CL_EC'].map(map_ec).fillna("Não informado")


df = df.reset_index(drop=True) #Reindexar


#Gerar estatísticas descritivas básicas para coluna de número de filhos do cliente
#(média; mediana; desvio padrão; moda; máximo; mínimo; e contagem, quartis)
print("Estatísticas básicas da coluna filhos do cliente - CL_FHL") #Estatística coluna filhos
print(df['CL_FHL'].describe()) 

print("Estatísticas específicas manuais da coluna filhos do cliente - CL_FHL")
print("Média:", df['CL_FHL'].mean())
print("Mediana:", df['CL_FHL'].median())
print("Desvio padrão:", df['CL_FHL'].std())
print("Moda:", df['CL_FHL'].mode()[0]) 
print("Máximo:", df['CL_FHL'].max())
print("Mínimo:", df['CL_FHL'].min())
print("Contagem:", df['CL_FHL'].count())
print("1º Quartil:", df['CL_FHL'].quantile(0.25)) #25%
print("2º Quartil:", df['CL_FHL'].quantile(0.50)) #50%
print("3º Quartil:", df['CL_FHL'].quantile(0.75)) #75%


#Explorar padrões de agrupamento com pelo menos dois agrupamentos
#(por exemplo: gênero com mais vendas, compras), usando groupby() ou pivot_table().
compras_genero = df.groupby('CL_GENERO')['CO_ID'].count().sort_values(ascending=False) #Agrupar coluna compras por gênero, utilizando a coluna identificação do cliente para contagem dos registros, e apresentar por ordem decrescente
print("Compras por gênero:")
print(compras_genero)

compras_categoria = df.groupby('PR_CAT')['CO_ID'].count().sort_values(ascending=False) #Agrupar coluna compras por categorias de produtos, utilizando a coluna identificação do cliente para contagem dos registros, e apresentar por ordem decrescente
print("Compras por categoria:")
print(compras_categoria)

pivot = pd.pivot_table( #Cruzamento dos dados: compras por categoria x gênero
    df,
    values='CO_ID', #o que contar
    index='PR_CAT', #linhas: categorias
    columns='CL_GENERO', #colunas: gênero
    aggfunc='count', #função de agregação
    fill_value=0
)

#Ordenar as categorias de maior número de compras para o menor
pivot['TOTAL'] = pivot.sum(axis=1)
pivot = pivot.sort_values('TOTAL', ascending=False)
pivot = pivot.drop(columns='TOTAL')

print("\nCruzamento categoria x gênero:")
print(pivot)


# Salvar DataFrame em CSV
df.to_csv('Base Varejo_limpo.csv', index=False)
print('Arquivo salvo com sucesso!')


##Visualização dos dados

#Gráfico de barras para compras categorias por gênero
categorias = pivot.index.tolist()
generos = pivot.columns.tolist() 

cores = sns.color_palette('Set2', n_colors=2) #uma cor distinta para cada categoria

ax = pivot.plot(
    kind='bar',
    stacked=False,
    figsize=(10, 6),
    colormap='Set2',
    edgecolor='white'
)

ax.set_title("Compras por categoria e gênero", fontsize=14, fontweight='bold')
ax.set_xlabel("Categoria de produto")
ax.set_ylabel("Número de compras")

ax.yaxis.grid(True, linestyle='--', alpha=0.4)
ax.set_axisbelow(True) #a grade fica atrás (abaixo) das barras

plt.xticks(rotation=45, ha='right')
plt.legend(title="Gênero")

plt.tight_layout()

plt.savefig("compras_categoria_genero.png", dpi=150, bbox_inches='tight') #salvar imagem do gráfico em png

plt.show() #mostrar