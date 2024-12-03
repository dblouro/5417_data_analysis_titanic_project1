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

print('\nAtividade 3.3 - Análise e manipulação de dados')

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



