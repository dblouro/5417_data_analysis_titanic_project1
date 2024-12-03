"""
Lab ProjectoFinal
Trabalho efetuado por Diogo Louro, Ricardo Conceição e João Pedro Silva
"""

import pandas as pd
import openpyxl
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# ATIVIDADE 3.1

print('\nAtividade 3.1 - Leitura e exploração dos dados')
#carregar o ficheiro csv
df = pd.read_csv('titanic.csv')

#ver os primeiros registos
print("\nPrimeiros 3 registos:")
print(df.head(3))

#ver os ultimos registos
print("\nÚltimos 3 registos:")
print(df.tail(3))

#resumo das colunas numericas
print("\nResumo estatístico só de colunas numéricas:")
print(df.describe())

#resumo das colunas todas
print("\nResumo estatístico só de colunas não-numéricas:")
print(df.describe(include='all'))

#resumo do DataFrame
print("\nInformação geral sobre o DataFrame:")
print(df.info())

# ATIVIDADE 3.2

print('\nAtividade 3.2 - Limpeza e pré-processamento de dados')
#verificar os valores nulos totais em cada coluna
print("Valores nulos por coluna:")
print(df.isnull().sum())

print('\nTratamento dos Dados')
#preencher com mediana o campo AGE
df['Age'].fillna(df['Age'].median(), inplace=True)
#preencher com mediana o campo AGE
df['Fare'].fillna(df['Fare'].median(), inplace=True)
#preencher os nulos com um valor fixo (abordagem para nao por de lado esta coluna)
df['Cabin'].fillna('Unknown', inplace=True)
print("\nValores nulos após tratamento:")
print(df.isnull().sum())
#salvar o tratamento num novo ficheiro CSV
df.to_csv('titanic_tratado.csv', index=False)
print("Novo ficheiro CSV criado: titanic_tratado.csv")

#carregar o ficheiro com os dados tratados
df = pd.read_csv('titanic_tratado.csv')
#verificar tipos de dados após conversão
print("\nTipos de dados após conversão:")
print(df.dtypes)
#Nota: PassengerId, Survived, Pclass: Está como int64, o que está correto. Como é um identificador único, não precisa de conversão.
#Nota: Age, Flare: Estão corretamente como float64.
#Nota: Name, Ticket, Cabin, Embarked, Sex: Mantêm o tipo object (string).


#Função para calcular o tempo em milissegundos desde o Epoch
def idade_para_milissegundos(idade):
    if pd.isna(idade):
        return None  #caso a idade for nula, devolve None    
    idade_int = int(idade)  #garantir que a idade é um número inteiro pois o datatype é float

    #datas anteriores ao Epoc nao aparecem [duvida]
    ano_nascimento = datetime.datetime.now().year - idade_int

    #descomentar, caso nao interessem as idades antes de 1970
    if ano_nascimento < 1970:
        return idade_int #retorna a idade como está para valores antes de 1970

    nascimento = datetime.datetime(ano_nascimento, 1, 1)
    epoch = datetime.datetime(1970, 1, 1)

    idade_milissegundos = int((nascimento - epoch).total_seconds() * 1000)
    return idade_milissegundos

#criaçao da nova coluna 'Idade_Milissegundos'
df['Idade_Milissegundos'] = df['Age'].apply(idade_para_milissegundos)

#verificar as primeiras 10 linhas para confirmar
print(df[['Age', 'Idade_Milissegundos']].head(10))

#salvar o novo dataframe com a nova coluna
df.to_csv('titanic_tratado_com_idade.csv', index=False)

# ATIVIDADE 3.3

print('\nAtividade 3.3 - Análise e manipulação de dados')

#taxa da mortalidade por sexos
print('\nTaxa de Mortalidade por sexo:')
mortalidade_sexo = df.groupby('Sex')['Survived'].apply(lambda x: 1 - x.mean())
print(mortalidade_sexo)
#COnclusao: basicamente, as mulheres sobreviveram e nenhum homem sobreviveu


#taxa de sobrevivência por sexo
taxa_sobrevivencia_sexo = df.groupby('Sex')['Survived'].mean() * 100
print("Taxa de Sobrevivência por Sexo (%):\n", taxa_sobrevivencia_sexo)

#taxa de sobrevivência por classe e sexo [agrupar dados de pClass e Sex e calcular a media da col Survived]
taxa_sobrevivencia = df.groupby(['Pclass', 'Sex'])['Survived'].mean() * 100
print("Taxa de Sobrevivência por Classe e Sexo (%):\n", taxa_sobrevivencia)

#média da idade para passageiros que sobreviveram (Survived = 1) e não sobreviveram (Survived = 0)
media_idade = df.groupby('Survived')['Age'].mean()
print("Média de Idade por Sobrevivência:\n", media_idade)

plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Age', hue='Survived', fill=True, common_norm=False)
plt.title('Distribuição da Idade por Sobrevivência')
plt.xlabel('Idade')
plt.ylabel('Densidade')
plt.legend(['Não Sobreviveu', 'Sobreviveu'])
plt.show()

#se a idade média varia por classe e status de sobrevivência
idade_por_classe = df.groupby(['Pclass', 'Survived'])['Age'].mean()
print("Idade Média por Classe e Sobrevivência:\n", idade_por_classe)

#interpretaçao dos dados da sobrevivencia 

#Classe 1 (Pclass = 1):
#Não sobreviveram (Survived = 0): A idade média dos passageiros que não sobreviveram nesta classe foi de aproximadamente 38,86 anos.
#Sobreviveram (Survived = 1): A idade média dos passageiros que sobreviveram nesta classe foi de aproximadamente 40,76 anos.
#Conclusao: pode indicar que passageiros mais velhos tinham maior probabilidade de sobrevivência nessa classe, ou que havia mais passageiros mais velhos sobreviventes na 1ª classe.

#Classe 2 (Pclass = 2):
#Não sobreviveram (Survived = 0): A idade média foi de 30,69 anos.
#Sobreviveram (Survived = 1): A idade média foi de 24,46 anos.
#COnclusao: Pode indicar que passageiros mais jovens tiveram maior probabilidade de sobreviver nesta classe.

#Classe 3 (Pclass = 3):
#Não sobreviveram (Survived = 0): A idade média foi de 25,37 anos.
#Sobreviveram (Survived = 1): A idade média foi de 24,27 anos.
#Conclusao: os sobreviventes tendem a ser ligeiramente mais jovens.

#Estes padrões podem ser influenciados por fatores como:
#acesso a botes salva-vidas (maior nas classes mais altas).
#prioridades dadas durante o resgate (potencialmente favorecendo crianças e mulheres).


# ATIVIDADE 3.4

print('\nAtividade 3.4 Visualização de dados')

# Configuração de estilo dos graficos
sns.set(style="whitegrid")

#Representar a distribuição dos sobreviventes por classe e sexo (eixo x: Pclass, eixos y: contagem de sobreviventes, diferenciando o sexo).
#Gráfico de linha
sobreviventes_classe_sexo = df[df['Survived'] == 1].groupby(['Pclass', 'Sex']).size().unstack()
print(sobreviventes_classe_sexo)
sobreviventes_classe_sexo.plot(kind='line', marker='o', figsize=(8, 6))
plt.title('Distribuição de Sobreviventes por Classe e Sexo')
plt.xlabel('Classe')
plt.ylabel('Número de Sobreviventes')
plt.legend(title='Sexo')
plt.show()

#Representa a correlaçao entre as variaveis AGE, FARE e SURVIVED
#Gráficos de dispersão
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', ax=axes[0])
axes[0].set_title('Idade vs Tarifa')
sns.scatterplot(data=df, x='Age', y='Survived', ax=axes[1])
axes[1].set_title('Idade vs Sobrevivência')
sns.scatterplot(data=df, x='Fare', y='Survived', ax=axes[2])
axes[2].set_title('Tarifa vs Sobrevivência')
plt.tight_layout()
plt.show()

#Representa a distribuiçao de variaveis onde se pode observar predominancia de faixas etarias ou tarifas nos sobreviventes
#Histogramas
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.histplot(data=df, x='Age', hue='Survived', kde=True, ax=axes[0], bins=20)
axes[0].set_title('Distribuição de Idades')
sns.histplot(data=df, x='Fare', hue='Survived', kde=True, ax=axes[1], bins=20)
axes[1].set_title('Distribuição de Tarifas')
sns.histplot(data=df, x='Survived', kde=False, ax=axes[2], bins=3)
axes[2].set_title('Distribuição de Sobrevivência')
plt.tight_layout()
plt.show()

# ATIVIDADE 3.7

print('\nAtividade 3.7 Análise Adicional - Relação entre Familia e Sobrevivencia')

#criacao da nova coluna Tamanho Familias com as variaveis SibSp[irmaoes] e Parch [filhos]
df['Tamanho_Familia'] = df['SibSp'] + df['Parch'] + 1

taxa_sobrevivencia_familia = df.groupby('Tamanho_Familia')['Survived'].mean()
print(taxa_sobrevivencia_familia)

# Visualizar com um gráfico de barras
taxa_sobrevivencia_familia.plot(kind='bar', figsize=(10, 6))
plt.title('Taxa de Sobrevivência por Tamanho da Família')
plt.xlabel('Tamanho da Família')
plt.ylabel('Taxa de Sobrevivência')
plt.show()


print('\nAtividade 3.7 Análise Adicional - Comparação por Porto de Embarque')

#mapeamento dos portos
portos = {'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'}

#usar a variavel Embarked para visualizar a taxa de sobrevicencia conforme o porto de embarque
sobrevivencia_por_embarque = df.groupby('Embarked')['Survived'].mean()
print(sobrevivencia_por_embarque)

#substitui as letras pelos nomes dos portos
sobrevivencia_por_embarque.index = sobrevivencia_por_embarque.index.map(portos)

# Gráfico de barras
sobrevivencia_por_embarque.plot(kind='bar', figsize=(8, 5), color='skyblue')
plt.title('Taxa de Sobrevivência por Porto de Embarque')
plt.xlabel('Porto de Embarque')
plt.ylabel('Taxa de Sobrevivência')
plt.xticks(rotation=0)
plt.show()

#salvar num novo ficheiro CSV, incluindo todas as colunas novas
df.to_csv('titanic_tratado_com_idade_final.csv', index=False)
print("Novo ficheiro CSV criado: titanic_tratado_com_idade_final.csv")

