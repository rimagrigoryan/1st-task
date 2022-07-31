#%%
from optparse import Values
import pandas as pd

#%%
df = pd.read_csv("armenian_pubs - armenian_pub-1.csv")

# %%
df

#%%
pd.pivot_table(df,index=["Fav_Pub"])

# %%
df2 = df.pivot_table(index=['Fav_Pub'], values='Age',  aggfunc='count')

# %%
df2.sort_values('Age', ascending=False)

# %%
df3 = df.pivot_table(index=['Fav_Pub', "Gender"], values='Age',  aggfunc='count')

# %%
df3

# %%
df3.sort_values('Age', ascending=False)

# %%
df4 = df.pivot_table(index=['Gender',], values='Age',  aggfunc='mean')

# %%
df4

# %%
df5 = df.pivot_table(index=['Gender',], values='WTS',  aggfunc='mean')

# %%
df5

# %%
df6 = df.pivot_table(index=['Gender',], values=["Income", "WTS"], aggfunc='mean')

# %%
df6.to_csv("armenian_pubs_pivot_table.csv") 

# %%
hh