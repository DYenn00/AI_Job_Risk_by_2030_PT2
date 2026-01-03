from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['Risk_Category'].value_counts()
    for x_label, grp in _df_16.groupby('Education_Level')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('Education_Level')
_ = plt.ylabel('Risk_Category')
