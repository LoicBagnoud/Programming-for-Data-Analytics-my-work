# This is to check if there is any correlation between the windspeed and the month in knock

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19)

corrtemp = df["month"].corr(df["meant"])

cleandf = df[["month", "wdsp"]].copy()

cleandf["wdsp"] = cleandf.loc[:, ("wdsp")].replace(" ", np.nan)
cleandf.dropna(inplace=True)

cleandf["wdsp"] = cleandf["wdsp"].astype(float)

corrwind = cleandf["month"].corr(cleandf["wdsp"])
print(f"Wind Correlation: {corrwind}")

sns.set_style("whitegrid")

sns.lmplot(x="month", y="wdsp", order = 3, data=cleandf)
plt.show()