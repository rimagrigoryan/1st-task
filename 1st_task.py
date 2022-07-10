#%%
from turtle import hideturtle
import pandas as pd

# %%
df = pd.read_csv("armenian_pubs - armenian_pubs.csv")

# %%
df

# %%
df.info()

# %%
df.to_csv("armenian_pubs_exported.csv") 
