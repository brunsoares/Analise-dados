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

# Preço médio dos veículos com base no tipo de combustível / Dados: price, fuelType, gearbox
sns.barplot(x=df.fuelType, y=df.price, hue=df.gearbox)
plt.title('Preço médio dos veículos com base no tipo de combustível')
plt.ylabel("Preço Médio")
plt.xlabel("Tipo de Combustível")
plt.savefig("graficos/03/fueltype-vehicleType-price.png")
plt.show()


# Potência média de um veículo por tipo de veículo / Dados: powerPS, vehicleType, gearbox
sns.barplot(x=df.vehicleType, y=df.powerPS, hue=df.gearbox)
plt.title('Potência média dos veículos com base no tipo de Veículo')
plt.ylabel("Potência Média")
plt.xlabel("Tipo de Veículo")
plt.savefig("graficos/03/vehicletype-fueltype-power.png")
plt.show()




