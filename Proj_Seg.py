import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('patients.csv')

idade = df['age']
serv = df['service']
sats = df['satisfaction']
ardt = df['arrival_date']
dpdt = df['departure_date']

fig = plt.figure(figsize=(15, 10), layout='constrained')
axs = fig.subplot_mosaic([["Serv", "Sats"],
                          ["Idade", "Sats"]])

# Gráfico PIZZA
contSE = serv.value_counts()

labels_ordered = ['Emergencia', 'Cirurgia', 'Serviço Geral', 'UTI']
colors_ordered = ['firebrick', '#1e488f', '#2c6fbb', 'skyblue']

wedges, texts, autotexts = axs["Serv"].pie(contSE,
  autopct='%1.1f%%',
  labels=labels_ordered,
  wedgeprops={'width': 0.47},
  pctdistance=0.74,
  explode=(0.1, 0, 0, 0),
  colors=colors_ordered)

axs["Serv"].set_title('Serviços Prestados', weight='semibold', color='#01153e')
axs["Serv"].set_ylabel('')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('semibold')

for text in texts:
    text.set_color('#01153e')
    text.set_weight('semibold')

# Gráfico BARRAS HORIZONTAL
filtro_GS = df[df['service'] == 'general_medicine']
media_GS = filtro_GS['satisfaction'].mean()

filtro_EM = df[df['service'] == 'emergency']
media_EM = filtro_EM['satisfaction'].mean()

filtro_SUR = df[df['service'] == 'surgery']
media_SUR = filtro_SUR['satisfaction'].mean()

filtro_ICU = df[df['service'] == 'ICU']
media_ICU = filtro_ICU['satisfaction'].mean()

satisfacao_geral = (media_EM, media_SUR, media_GS, media_ICU)
categorias = ['Emergência', 'Cirurgia', 'Serviço Geral', 'UTI']
colors = ['firebrick', '#1e488f', '#2c6fbb', 'skyblue']

axs["Sats"].barh(categorias, satisfacao_geral, color=colors, edgecolor='white')
axs["Sats"].set_title('Satisfação por Serviço', weight='semibold', color='#01153e')
axs["Sats"].set_xlabel('Média de Satisfação')
axs["Sats"].tick_params(axis='y', rotation=0)
axs["Sats"].yaxis.tick_right()
axs["Sats"].invert_xaxis()

# Gráfico BARRAS
df['age_group'] = pd.cut(df['age'], bins=[0, 11, 20, 54, 100],
                        labels=['criança', 'adolescente', 'jovem-adulto', 'idoso'])

service_by_age = df.groupby(['service', 'age_group']).size().unstack()

service_name_map = {
    'general_medicine': 'Serviço Geral',
    'emergency': 'Emergência',
    'surgery': 'Cirurgia',
    'ICU': 'UTI'
}
service_by_age = service_by_age.rename(index=service_name_map)

service_by_age.plot(kind='bar', ax=axs["Idade"], color=['#98eff9', 'skyblue', '#2c6fbb', '#1e488f'])
axs["Idade"].set_title('Pacientes por Serviço e Faixa Etária', weight='semibold')
axs["Idade"].set_xlabel('Serviço')
axs["Idade"].legend(title='Idade', loc='right')
axs["Idade"].tick_params(axis='x', rotation=45)


plt.show()

# Gráfico 4 (Não existe, mas se caso mude de ideia e necesite inserir mais um o espaço não va estar ocupado)
