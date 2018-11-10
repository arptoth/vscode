#!/anaconda/bin/python

#%% [markdown]
# # Title

#%%
import pandas as pd
data=pd.read_csv("diabetes.csv")

#%%
data=pd.DataFrame(data)


#%%
data.columns

#%%

# Load the H2O library and start up the H2O cluter locally on your machine
#%%
import h2o
from h2o.automl import H2OAutoML
h2o.init()

#%%
data_path = "https://github.com/h2oai/h2o-tutorials/raw/master/h2o-world-2017/automl/data/product_backorders.csv"

# Load data into H2O
df = h2o.import_file(data_path)

#%%
df.head()

#%%
df.describe()

#%%
y = "went_on_backorder"
x = df.columns
x.remove(y)
x.remove("sku")

#%%
aml = H2OAutoML(max_models = 5, seed = 1)
aml.train(x = x, y = y, training_frame = df)


#%
