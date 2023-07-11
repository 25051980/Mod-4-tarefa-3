#!/usr/bin/env python
# coding: utf-8

# # Tarefa 03
# 
# - Leia os enunciados com atenção
# - Saiba que pode haver mais de uma resposta correta
# - Insira novas células de código sempre que achar necessário
# - Em caso de dúvidas, procure os Tutores
# - Divirta-se :)

# In[43]:


import pandas as pd
import requests


# ####  1) Lendo de APIs
# Vimos em aula como carregar dados públicos do governo através de um API (*Application Programming Interface*). No exemplo de aula, baixamos os dados de pedidos de verificação de limites (PVL) realizados por estados, e selecionamos apenas aqueles referentes ao estado de São Paulo.
# 
# 1. Repita os mesmos passos feitos em aula, mas selecione os PVLs realizados por municípios no estado do Rio de Janeiro.
# 2. Quais são os três *status* das solicitações mais frequentes na base? Quais são suas frequências?
# 3. Construa uma nova variável que contenha o ano do **status**. Observe que ```data_status``` vem como tipo *object* no **DataFrame**. Dica: você pode usar o método ```.str``` para transformar o tipo da variável em string, em seguida um método como [**slice()**](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html) ou [**split()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html).
# 4. Indique a frequência de cada ano do campo construído no item (3).

# In[44]:


url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl?uf=RJ&tipo_interessado=Estado'


# In[45]:


requests.get(url)


# In[46]:


r = requests.get(url)


# In[47]:


r.status_code


# In[52]:


data_json = r.json()


# In[49]:


print(data_json['items'])


# In[50]:


pd.DataFrame(data_json['items'])


# In[51]:


print(participacoes_acionarias.columns)


# In[54]:


import pandas as pd
import requests

url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl'
params = {
    'uf': 'RJ',
    'tipo_interessado': 'Estado'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data_json = response.json()
    df = pd.DataFrame(data_json['items'])
    status_counts = df['status'].value_counts().head(3)
    print(status_counts)
else:
    print('Erro ao fazer a solicitação: ', response.status_code)


# In[60]:


# Quais as solicitações mais frequentes na base? Quais são suas frequências?
import pandas as pd
import requests

# Fazer a solicitação HTTP e obter os dados do URL
url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl?uf=RJ&tipo_interessado=Estado'
response = requests.get(url)
data = response.json()

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(data['items'])

# Extrair o ano do campo data_status
df['ano_status'] = df['data_status'].str.split('/').str[-1]

print(df['ano_status'])



# In[61]:


frequencia_anos = df['ano_status'].value_counts()
print(frequencia_anos)


# ####  2) Melhorando a interação com o API
# Observe dois URLs de consultas diferentes, por exemplo o URL utilizado em aula, e o URL feito no exercício anterior. Compare-os e observe as diferenças.
# 
# 1. Faça uma função em Python que recebe como argumento o UF da consulta e o tipo de interessado (```'Estado'```ou ```Município```), e que devolve os dados da consulta no formato *DataFrame*.
# 2. Quantas solicitações para o Estado podem ser consultadas para Minas Gerais com *status* em 'Arquivado por decurso de prazo' estão registradas?
# 3. Qual é o município da Bahia com mais solicitações deferidas?
# 4. Salve um arquivo .csv com os dados de solicitações da Bahia, com interessado = 'Estado'

# In[31]:


url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl?uf=MG&tipo_interessado=Estado'


# In[32]:


requests.get(url)


# In[33]:


r = requests.get(url)


# In[34]:


r.status_code


# In[35]:


#1) Seu código aqui
import pandas as pd

def consultar_dados(UF, tipo_interessado):
    base_url = "URL_BASE"  # Substitua pelo URL base utilizado em aula
    exercicio_url = "URL_EXERCICIO"  # Substitua pelo URL utilizado no exercício anterior

    if tipo_interessado == "Estado":
        url = base_url + "?uf=" + UF
    elif tipo_interessado == "Município":
        url = base_url + "?municipio=" + UF
    else:
        return None  # Retorna None se o tipo de interessado não for válido

    # Faça a requisição HTTP para obter os dados da consulta
    # Utilize a biblioteca requests ou qualquer outra de sua preferência
    # e armazene a resposta na variável 'response'

    # Extraia os dados da resposta e crie um DataFrame
    # Dependendo da estrutura dos dados retornados, você precisará ajustar o código abaixo
    data = response.json()  # Supondo que a resposta é um objeto JSON
    df = pd.DataFrame(data)

    return df


# In[36]:


# 2) Seu código aqui
import requests
import pandas as pd

def consultar_dados(UF, tipo_interessado):
    url = f"https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl?uf={UF}&tipo_interessado={tipo_interessado}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['items'])
        return df
    else:
        return None

# Consultar os dados para Minas Gerais com tipo de interessado 'Estado'
df = consultar_dados('MG', 'Estado')

if df is not None:
    # Filtrar as solicitações arquivadas por decurso de prazo em Minas Gerais
    filtrado = df[(df['uf'] == 'MG') & (df['status'] == 'Arquivado por decurso de prazo')]
    
    # Contar o número de solicitações arquivadas
    num_solicitacoes_arquivadas = len(filtrado)
    print("Número de solicitações arquivadas por decurso de prazo em Minas Gerais:", num_solicitacoes_arquivadas)
else:
    print("Falha ao consultar os dados.")


# In[37]:


# solicitações que podem ser consultadas para Minas Gerais com status em 'Arquivado por decurso de prazo'.

import requests

url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl'
params = {
    'uf': 'MG',
    'tipo_interessado': 'Estado',
    'status': 'Arquivado por decurso de prazo'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    total_solicitacoes = len(data['items'])
    print(f"Total de solicitações com status 'Arquivado por decurso de prazo': {total_solicitacoes}")
else:
    print("Erro ao fazer a solicitação HTTP.")


# In[38]:


# 4) Seu código aqui
url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl?uf=BA&tipo_interessado=Munic%C3%ADpio'


# In[39]:


requests.get(url)


# In[40]:


r = requests.get(url)


# In[41]:


r.status_code


# In[45]:


import requests

url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl'
params = {
    'uf': 'BA',
    'tipo_interessado': 'Município'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    municipios = data['items']

    if municipios:
        municipio_max_solicitacoes = max(municipios, key=lambda x: x.get('quantidade_solicitacoes', 0))
        nome_municipio = municipio_max_solicitacoes.get('municipio')
        total_solicitacoes = municipio_max_solicitacoes.get('quantidade_solicitacoes')

        print(f"Município com mais solicitações deferidas: {nome_municipio}")
        print(f"Total de solicitações deferidas: {total_solicitacoes}")
    else:
        print("Nenhum dado encontrado para os parâmetros especificados.")
else:
    print("Erro ao fazer a solicitação HTTP.")


# In[47]:


import requests

url = 'https://apidatalake.tesouro.gov.br/ords/sadipem/tt/pvl'
params = {
    'uf': 'BA',
    'tipo_interessado': 'Estado'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    items = data['items']

    if items:
        print(items[0])  # Exibe o primeiro item para visualizar a estrutura dos dados
    else:
        print("Nenhum dado encontrado para os parâmetros especificados.")
else:
    print("Erro ao fazer a solicitação HTTP.")


# In[ ]:




