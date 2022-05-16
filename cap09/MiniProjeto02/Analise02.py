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

# Veículos por Marca / Dados: brand
sns.catplot(y="brand", data=df, kind="count")
plt.title("Veículos por Marca")
plt.ylabel("Marca")
plt.xlabel("Número de Veículos")
plt.savefig("graficos/02/brand-vehicleCount.png")
plt.show()


# Preço médio dos veículos com base no tipo de veículo / Dados: price, vehicleType, gearbox
sns.barplot(x=df.vehicleType, y=df.price, hue=df.gearbox)
plt.title('Preço médio dos veículos com base no tipo de veículo')
plt.ylabel("Preço Médio")
plt.xlabel("Tipo de Veículo")
plt.savefig("graficos/02/vehicletype-gearbox-price.png")
plt.show()

