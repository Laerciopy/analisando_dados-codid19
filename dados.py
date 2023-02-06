import requests
import json
import pandas as pd
import numpy as np

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "1480463e2fmsh8e36a206b024325p148ff8jsn10e19d646092",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

#acessando dados
info = json.loads(response.text) #lista que retorna dicionarios com informacoes  
lista_info = []
for i in info['response']:
    temp = []
    continente = i['continent']
    pais = i['country']
    casos_total = i['cases']['total']
    casos_recuperado = i['cases']['recovered']
    casos_ativo = i['cases']['active']
    mortes = i['deaths']['total']
    dia = i['day']
    temp.append(continente)
    temp.append(pais)
    temp.append(casos_total)
    temp.append(casos_recuperado)
    temp.append(mortes)
    temp.append(dia)

    lista_info.append(temp)


#conectando lista com pandas
df = pd.DataFrame(lista_info, columns=['continent', 'pais', 'casos', 'recuperados', 'mortes', 'dia'])

############# Organizando por continentes e geral #######
df_total = df.groupby(['continent']).sum()

# adicionado index na tabela
df_total['nome'] = df_total.index

#convertendo o dataframe em dicionario
dic_total = df_total.to_dict('recorde')

# lista que contém os dados
Total = []

for i in dic_total:
    Total.append(i)

#dados para continentes
lista_continentes_valor = [Total[0]['casos'], Total[2]['casos'], Total[3]
                           ['casos'], Total[4]['casos'], Total[5]['casos'], Total[6]['casos']]
lista_continentes_nome = [Total[0]['nome'], Total[2]['nome'], Total[3]
                          ['nome'], Total[4]['nome'], Total[5]['nome'], Total[6]['nome']]



########## Organizando por paises ##########
df_pais = df.groupby(['pais', 'dia']).sum()

# adicionado index na tabela
df_pais['nome'] = df_pais.index.get_level_values('pais')
df_pais['dia'] = df_pais.index.get_level_values('dia')

df_pais = df_pais[['nome', 'casos', 'recuperados', 'mortes', 'dia']]

lista_paizes = []

for i in df_pais.values.tolist():
    if i[0] == "All":
        pass
    else:
        temp = []
        temp.append(i[0])
        temp.append("{:,.0f}".format(i[1]))
        temp.append("{:,.0f}".format(i[2]))
        temp.append("{:,.0f}".format(i[3]))
        temp.append(i[4])

        lista_paizes.append(temp)


df_pais_top = df_pais[['nome', 'casos']]
df_pais_top = df_pais_top.sort_values(by=['casos'], ascending=False)

lista_paizes_top = []

for i in df_pais_top.head(11).values.tolist():
    if i[0] == "All" or i[0] == "Asia" or i[0] == "North-America" or i[0] == "Europe" or i[0] == "South-America" or i[0] == "Africa":
        pass
    else:
        temp = []
        temp.append(i[0])
        temp.append(i[1])
        lista_paizes_top.append(temp)

lista_paizes_top = sorted(lista_paizes_top, key=lambda x: x[1])
