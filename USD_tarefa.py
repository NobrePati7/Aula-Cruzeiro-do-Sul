import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload manual do CSV
from google.colab import files
uploaded = files.upload()  # Vai abrir uma janela para você escolher o CSV

# Carregar e preparar o dataset
df = pd.read_csv("USD_BRL_hist.csv")
df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')
df = df.sort_values('Data')
df.set_index('Data', inplace=True)

# Plot 1: Série Temporal
plt.figure(figsize=(12, 5))
plt.plot(df.index, df['USD_BRL'], color='blue')
plt.title('Cotação Histórica USD/BRL')
plt.xlabel('Data')
plt.ylabel('Cotação em R$')
plt.grid(True)
plt.tight_layout()
plt.savefig("plot1_linha.png")
plt.show()

# Plot 2: Boxplot por Ano
df['Ano'] = df.index.year
plt.figure(figsize=(10, 5))
sns.boxplot(x='Ano', y='USD_BRL', data=df)
plt.title('Distribuição Anual da Cotação USD/BRL')
plt.xlabel('Ano')
plt.ylabel('Cotação em R$')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plot2_boxplot.png")
plt.show()

# Plot 3: Heatmap Ano x Mês
df['Mês'] = df.index.month
heatmap_data = df.pivot_table(values='USD_BRL', index='Ano', columns='Mês', aggfunc='mean')
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="YlGnBu")
plt.title('Heatmap da Cotação Média USD/BRL (Ano x Mês)')
plt.xlabel('Mês')
plt.ylabel('Ano')
plt.tight_layout()
plt.savefig("plot3_heatmap.png")
plt.show()
