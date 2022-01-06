# imports necessários
import numpy as np
import pandas as pd

# importando dados uma url para um dataframe

# url a importar
url_dados = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# labels dos atributos do dataset
atributos = ['comprimento_sepala', 'largura_sepala', 'comprimento_petala', 'largura_petala', 'especie']

# carga do dataset através da url - há diversos parâmetros no read_csv que podem ser interessantes, como sep, usecols e header
iris = pd.read_csv(url_dados, names=atributos)

print(type(iris))