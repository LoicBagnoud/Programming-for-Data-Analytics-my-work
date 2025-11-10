# The purpose of this lab is to make some regression plots

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = sns.load_dataset("tips")

sns.set_style("whitegrid")
sns.lmplot(
    x="total_bill",
    y="tip",
    data=dataset,
    x_estimator=np.mean
)
plt.show()
