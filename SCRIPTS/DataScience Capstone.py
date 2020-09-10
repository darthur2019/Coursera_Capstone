# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
df = pd.read_csv('Data-Collisions.csv')


# %%
df.describe()


# %%
df.info()


# %%
df[['ROADCOND']].count()


# %%
194673-189661


# %%
df['SEVERITYCODE'].value_counts()


# %%
df.describe(include='all')


# %%



# %%



