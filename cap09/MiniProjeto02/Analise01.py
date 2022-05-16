import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white")

# Dataset
'''
Campos do arquivo CSV:
dateCrawled, name, seller, offerType, price, abtest, vehicleType, yearOfRegistration,
gearbox, powerPS, model, kilometer, monthOfRegistration, fuelType, brand, notRepairedDamage,
dateCreated, postalCode, lastSeen, yearOfCreation, yearCrawled, monthOfCreation, monthCrawled,
NoOfDaysOnline, NoOfHrsOnline, yearsOld, monthsOld
'''
clean_data_path = "dataset/autos.csv"
df = pd.read_csv(clean_data_path, encoding="latin-1")

# Distribuição de veiculos com base no ano de registro /    Dados: yearOfRegistration
fig, axies = plt.subplots(figsize=(8, 6))
sns.histplot(df['yearOfRegistration'], color="#4287f5", kde=True, ax=axies)
axies.set_title("Distribuição de Veículos com base no ano de Registro")
plt.ylabel("Densidade (KDE)")
plt.xlabel("Ano de Registro")
fig.savefig("graficos/01/vehicle-distribution.png")
plt.show()


# Análise de Outliers / Dados: price, vehicleType
fig, ax = plt.subplots()
sns.boxplot(x=df.vehicleType, y=df.price)
ax.set_title('Análise de Outliers')
plt.ylabel("Range de Preço")
plt.xlabel("Tipo de Veículo")
fig.savefig("graficos/01/price-vehicleType-boxplot.png")
plt.show()

# Contagem Total de Veículos à venda Conforme o tipo do Veículo / Dados: vehicleType
fig, ax = plt.subplots()
sns.countplot(x="vehicleType", data=df)
ax.set_title('Contagem Total de Veículos à venda Conforme o tipo do Veículo')
plt.ylabel("Total de Veículos para venda")
plt.xlabel("Tipo de Veículo")
fig.savefig("graficos/01/count-vehicleType.png")
plt.show()
