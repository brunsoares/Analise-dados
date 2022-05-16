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

# Cálculo preço médio por marca e por tipo veículo  / Dados: brand, vehicleType, price
dfMedia = pd.DataFrame()
for mc in list(df['brand'].unique()):   # Cálculo usando valores unicos e pegando média do preço
    for vt in list(df['vehicleType'].unique()):
        media = df[(df['brand'] == mc) & (df['vehicleType'] == vt)]['price'].mean()
        dfMedia = dfMedia.append(pd.DataFrame({"brand": mc, "vehicleType": vt, "meanPrice": media}, index=[0]))

# Tratamento novo DataFrame
dfMedia = dfMedia.reset_index()
del dfMedia['index']
dfMedia['meanPrice'].fillna(0, inplace=True)
dfMedia['meanPrice'] = dfMedia['meanPrice'].astype(int)
print(dfMedia.head(10))

# Preço médio de um veículo por marca e pelo tipo de veículo / Dados: meanPrice, brand, vehicleType / DataFrame = dfMedia
dadosHeatMap = dfMedia.pivot("brand", "vehicleType", "meanPrice")   # Transformando dados em 2d
sns.heatmap(dadosHeatMap, cmap="Purples", linewidths=1, annot=True, fmt="d")
plt.title('Preço médio de um veículo por marca e pelo tipo de veículo')
plt.ylabel("Marca")
plt.xlabel("Tipo de Veículo")
plt.savefig("graficos/04/heatmap-price-brand-vehicleType.png")
plt.show()

'''
    Lista Cores: 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 
    'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 
    'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 
    'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 
    'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 
    'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 
    'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 
    'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 
    'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'crest', 
    'crest_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'flare', 'flare_r', 'gist_earth', 'gist_earth_r', 
    'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 
    'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 
    'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 
    'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral',
    'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 
    'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 
    'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 
    'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 
    'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r'
'''