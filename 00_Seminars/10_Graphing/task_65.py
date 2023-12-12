import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='sex', size='island', style='island')

"""
x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
y_vars = ["sex"]
pair = sns.PairGrid(penguins, x_vars=x_vars, y_vars=y_vars, hue='species')
pair.map(sns.scatterplot)
"""

"""
data = penguins.pivot_table(index='species', columns='island', values='body_mass_g')
sns.heatmap(data)
plt.xlabel('Остров', size=14)
plt.ylabel('Вид пингвина', size=14)
# plt.show()
"""


# penguins['bill_depth_mm'].hist(bins=10)

plt.show()

# 6,7,8 (введение в ООП)