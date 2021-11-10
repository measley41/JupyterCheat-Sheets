# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Reshaping and Aggregation Functions
# from [Reshaping DataFrames in Pandas](https://towardsdatascience.com/reshaping-dataframes-in-pandas-f6bfbb2c5b0f) by [Anirudh Nanduri](https://medium.com/@nvpsani)  
# and [Meet the hardest functions of Pandas, Part II](https://towardsdatascience.com/meet-the-hardest-functions-of-pandas-part-ii-f8029a2b0c9b) by [Bex t.](https://ibexorigin.medium.com)

# %% [markdown]
# <a id='Contents'></a>
# ## Contents:
#
# ### Type 1: Reforming without aggregation
# > [Pivot](#Pivot) Converts rows of categorical values into separate columns  
# > [Melt](#Melt) Converts columns into rows  
# > [Stack](#Stack) Converts columns into index - for MultiIndex DataFrames  
# > [Unstack](#Unstack) Converts index into columns - for MultiIndex DataFrames  
#
# *Note* Need to add transpose
# > 
# ### Type 2: Reforming with aggregation
# > [Group by](#group_by)  
# > [Pivot Table](#pivot_table)  
# > [Crosstab](#Crosstab)  
# > [crosstab vs. pivot_table](#crosstab_vs_pivot_table)  
#

# %%
# Create a DataFrame to work with

import numpy as np
import pandas as pd
df = pd.DataFrame({'Date': pd.Index(pd.date_range(start='2/2/2019', periods=3)).repeat(3),
                   'Class':['1A','2B','3C','1A','2B','3C','1A','2B','3C'],
                   'Numbers':np.random.randn(9)})

df['Numbers2']= df['Numbers']*2

# %% [markdown]
# ## Type 1: Reshaping without aggregation
# [Return to top](#Contents)
# <a id='Pivot'></a>
# ### Pivot
# Pivot rearranges the table by converting categorical values into separate columns:

# %%
df

# %%
df.pivot(index='Date', columns='Class', values='Numbers')

# %% [markdown]
# If we don't specify the values parameter, pandas would create all the various possible views while taking all column names apart from what we specified as the index and columns.  

# %%
df.pivot(index='Date', columns='Class')

# %% [markdown]
# The format below gives the same results as the first example, but it's slower. This is because it first gets the results for all of the columns, then creates a subset of the results.  The first example of specifying the `values` parameter is preferred.

# %%
df.pivot(index='Date', columns='Class')['Numbers']

# %% [markdown]
# [Return to top](#Contents)
# <a id='Melt'></a>
# ### Melt
#
# Melt is the opposite of pivot.  
# It converts multiple columns into a single column of categorical names and a second column that contains their values.

# %%
df

# %%
df.melt(id_vars=['Date','Class'])

# %% [markdown]
# `value_vars` can be used when you only want to convert specific columns.

# %%
df.melt(id_vars=['Date','Class'], value_vars=['Numbers'])

# %% [markdown]
# `value_name` and `var_name` can be used to specify the resulting column names, rather than using the default names of `variable` and `value`.

# %%
df.melt(id_vars=['Date','Class'], value_vars=['Numbers'], value_name='Numbers_Value', var_name='Num_Var')

# %% [markdown]
# [Return to top](#Contents)
# <a id='Stack'></a>
# ### Stack and Unstack
#
# *stack* and *unstack* are similar to *melt* and *pivot*, except they work with MultiIndex objects.  
# - stack: columns to index  
# - unstack: index to columns
#
# ### Stack: columns to index

# %%
# see what df looks like with a multiIndex
df.set_index(['Date','Class'])

# %%
df.set_index(['Date','Class']).stack()

# %% [markdown]
# One possible use of `stack` is to create a nested lookup table.  Using the example above, you can look up values:

# %%
df.set_index(['Date','Class']).stack()['2019-02-03']['2B']['Numbers2']

# %% [markdown]
# [Return to top](#Contents)
# <a id='Unstack'></a>
# ### Unstack: Index to columns

# %%
df.set_index(['Date','Class'])

# %%
df.set_index(['Date', 'Class']).unstack()

# %% [markdown]
# [Return to top](#Contents)
# <a id='Type2'></a>
# ## Type 2: Reshaping with aggregation
#
# Create a new dataframe for examples:

# %%
df = pd.DataFrame({'Date': pd.Index(pd.date_range(start='2/2/2019', periods=2)).repeat(4),
                  'Class':['1A','2B','3C','1A','2B','3C','1A','2B'],
                  'Numbers': np.random.randn(8)})
df

# %% [markdown]
# [Return to top](#Contents)
# <a id='group_by'></a>
# ### Group by

# %%
grps = df.groupby('Date')
for date, group in grps:
    print(date)
    print(group)


# %%
df.groupby('Date')['Numbers'].mean()

# %% [markdown]
# #### Some methods to get the result as a DataFrame

# %%
df.groupby('Date')[['Numbers']].mean()
df.groupby('Date').agg('mean')

# %% [markdown]
# **Creating a separate index**  
# (instead of using 'Date' as an index by default)

# %%
df.groupby('Date', as_index=False)['Numbers'].mean()

# %% [markdown]
# #### Aggregating on multiple columns:

# %%
df.groupby(['Date','Class'],as_index=False)['Numbers'].mean()

# %%
df['Numbers2'] = df['Numbers']*2

# %% [markdown]
# #### Multiple aggregations on a column

# %%
df.groupby('Date').agg({'Numbers':'sum', 'Numbers2':['mean','max']})

# %% [markdown]
# #### Renaming aggregation columns

# %%
df.groupby(['Date'], as_index=False).agg(Numbers_Avg=('Numbers','mean'),Numbers_Sum=('Numbers','sum'))

# %% [markdown]
# #### Using Lambda Expressions

# %%
df.groupby('Date', as_index=False).agg(Num_As_Pct=('Numbers', lambda x: np.round(x.mean()*100,2)))


# %% [markdown]
# #### Using Custom Functions

# %%
def sign(number):
    if (number.mean()>=0): #.all():
        return 'positive'
    else:
        return 'negative'

df.groupby('Date').agg({'Numbers':['mean',sign]})

# %% [markdown]
# #### Including Missing Values

# %%
# insert some missing values
df.iloc[4:6,0]=np.nan
df

# %%
df.groupby('Date',dropna=False).mean()

# %% [markdown]
# Sorting options

# %% [markdown]
# [Return to top](#Contents)
# <a id='pivot_table'></a>
# ### Pivot_Table
#
# Works similar to a pivot (categorical values to separate columns) with the addition of aggregation.

# %%
df

# %% [markdown]
# #### If not specified, the default aggregation function is `mean`:

# %%
df.pivot_table(index='Date', columns='Class')

# %% [markdown]
# #### The agg function can be specified:

# %%
df.pivot_table(index='Date', columns='Class', aggfunc='sum')

# %% [markdown]
# [Return to top](#Contents)
# <a id='Crosstab'></a>
# ### Crosstab
#
# - Crosstab works with categorical data.
# - Crosstab always returns a DataFrame.  
# - **By default, it takes two or more columns and returns a frequency of each combination.**

# %%
df

# %%
pd.crosstab(df.Date, df.Class)
#or
pd.crosstab(index=df['Date'], columns=df['Class'])

# %% [markdown]
# #### Other aggregation parameters can be used:

# %%
pd.crosstab(df.Date, df.Class, values=df.Numbers, aggfunc='sum')
# or
pd.crosstab(index=df['Date'], columns=df['Class'], values=df['Numbers'], aggfunc='sum')

# %%
pd.crosstab(df.Date, df.Class, values=df.Numbers, aggfunc='mean')
# or
pd.crosstab(index=df['Date'],
           columns=df['Class'],
           values=df['Numbers'],
           aggfunc=np.mean)

# %% [markdown]
# #### Crosstab Subtotal Summaries
# Crosstab also provides subtotal summaries when `margins=True` is used.  
# By default, the subtotal is named "All", but the name can be specified, using `margins_name='Total Number'`, as an example.  

# %%
pd.crosstab(index=df['Date'], columns=df['Class'], margins=True, margins_name='Total_Number')

# %% [markdown]
# #### Normalizing values with Crosstab
# Crosstab also has the option of normalizing values.  `normalize` can be set to `all`, `index`, or `columns`.<br>
# This example shows the percentages of each that adds up to 1.0 for the whole group:

# %%
pd.crosstab(index=df['Date'], columns=df['Class'], normalize='all')

# %% [markdown]
# [Return to Top](#Contents)
# <a id='crosstab_vs_pivot_table'></a>
# ### crosstab vs pivot_table
# Crosstab and Pivot_Table produce similar results.  Both are slower than groubpy.  
# Some of the differences are:  
#
# - Crosstab can work with any data type (lists, numpy arrays, DataFrame columns, etc.)
# - Crosstab has optional parameter for `normalize`
# - Crosstab can change names using `rownames` and `colnames`
#  - (They both have options for `margins`, `margins_name`
#  
#  
# - Pivot_table can only work with DataFrames
# - Pivot_table has `fillvalue=xx` 
#     - (Crosstab can be followed with `.fillna(0)`)

# %% [markdown]
# [Return to Top](#Contents)

# %%
print(f"numpy: {np.__version__}")
print(f"pandas: {pd.__version__}")

# %%
