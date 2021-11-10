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
#
# [8 Python Pandas Value_counts() tricks that make your work more efficient](https://re-thought.com/pandas-value_counts) by [Anna Zverkova](https://re-thought.com/author/anna/)
#
# [Introduction](#intro)  
#
#

# %% [markdown]
# [Return to Top](#Contents)
# <a id="intro"></a>
# ### Introduction
# #### Syntax
# `df['your_column'].value_counts()` will return the count of unique occurences in the specified column.
#
# #### Parameters
#
# - **normalize (bool, default False)** - If True, then the object returned will contain the relative frequencies of the unique values.  
# - **sort (bool, default True)** - Sort by frequencies  
# - **ascending (bool, default False)** - Sort in ascending order.
# - **bins (int, optional)** - Rather than count values, group them into half-open bins, a convenience for `pd.cut`, only works with numeric data.  
# - **dropna (bool, default True)** - Don't include counts of NaN.

# %%
#import packages
import pandas as pd

df = pd.read_csv('coursea_data.csv')
df.head(10)

# %%
# check how many records are in the dataset 
# and if we have any NA
df.info()

# %% [markdown]
# This tells us that we have 891 records in our dataset and that we don't have any NA values.

# %% [markdown]
# [Return to Top](#Contents)
# <a id='defaults'></a>
# ### 1.) value_counts() with default parameters
#
# **Syntax** - `df['your_column'].value_counts()`

# %%
df['course_difficulty'].value_counts()

# %% [markdown]
# The `value_counts` function returns the count of all unique values in the given index in descending order without any null values.
#
# ### 2.) value_counts() in ascending order
# The series returned by `value_counts()` is in descending order by default.  We can reverse the case by setting the `ascending` parameter to `True`.
#
# **Syntax** - `df['your_column'].value_counts(ascending=True)`

# %%
# count of all unique values for the column course_difficulty 
# in ascending order
df['course_difficulty'].value_counts(ascending=True)

# %% [markdown]
# ### 3.) value_counts() sorted alphabetically
# In some cases it is necessary to display your value_counts in alphabetical order.  
# This can be done easily by adding sort index `sort_index(ascending=True)` after your value_counts().
#
# Default value_counts() for column "course_difficulty" sorts values by counts:

# %%
df['course_difficulty'].value_counts()

# %% [markdown]
# Value_counts() with sort_index(ascending=True) sorts by index (column that you are running value_counts() on:

# %%
df['course_difficulty'].value_counts().sort_index(ascending=True)

# %% [markdown]
# If you want to list value_counts() in reverse alphabetical order you will need to change ascending to False `sort_index(ascending=False)`

# %%
df['course_difficulty'].value_counts().sort_index(ascending=False)

# %% [markdown]
# ### 4.) Pandas value_counts(): sort by value, then alphabetically
# Lets use for this example a slightly different dataframe.

# %%
df_fruit = pd.DataFrame({
    'fruit':
    ['sharon fruit']*5 + ['apples']*5 + ['bananas']*3 +
    ['nectarines']*3 + ['carrots']*3 + ['apricots'] + ['mango']*2
})

# %% [markdown]
# Here we wnat to get output sorted first by the value counts, then alphabetically by the name of the fruit.  This can be done by combining value_counts() with `sort_index(ascending=False)` and `sort_values(ascending=False)`.

# %%
df_fruit['fruit'].value_counts().sort_index(ascending=False).sort_values(ascending=False)

# %% [markdown]
# ### 5.) value_counts() percentage counts or relative frequencies of the unique values
# Sometimes, getting a percentage count is better than the normal count.  By setting `normalize=True`, the object returned will contain the relative frequencies of the unique values.  The `normalize` parameter is set to `False` by default.
#
# **Syntax** - `df['your_column'].value_counts(normalize=True)`

# %%
df['course_difficulty'].value_counts(normalize=True)

# %% [markdown]
# ### 6.) value_counts() to bin continuous data into discrete intervals.
# This is one great hack that is commonly under-utilised.  The `value_counts()` can be used to bin continuous data into discrete intervals with the help of the `bin` parameter.  This option works only with numerical data.  It is similar to the `pd.cut` function.  Let's see how it works using the *course_rating* column.  Let's group the counts for the column into 4 bins.
#
# **Syntax** - `df['your_column'].value_counts(bin=number of bins)`

# %%
df['course_rating'].value_counts()

# %%
df['course_rating'].value_counts(bins=4)

# %% [markdown]
# Binning makes it easy to understand the idea being conveyed.  We can easily see that most of the people out of the total population rated coursed above 4.5.  With just a few outliers where the rating is below 4.15 (only 7 rated courses lower than 4.15).

# %%
df['course_rating'].value_counts(bins=4, ascending=True)

# %% [markdown]
# ### 7.) value_counts() displaying the NaN values
# By default, the count of null values is excluded from the result.  But, the same can be displayed easily by setting the `dropna` parameter to `False`.  Since our dataset does not have nay null values setting dropna parameter would not make a difference.  But this can be of use on another dataset that has null values, so keep this in mind.
#
# **Syntax** - `df['your_column'].value_counts(dropna=False)`

# %% [markdown]
# ### 8.) value_counts() as dataframe
# As mentioned at the beginning of the article, value_counts returns series, not a dataframe.  If you want to have your counts as a dataframe you can do it using function `.to_frame()` after the `.value_counts()`.
#
# We can convert the series to a dataframe as follows:
#
# **Syntax** - `df['your_column'].value_counts().to_frame()`

# %%
df['course_difficulty'].value_counts()

# %%
df['course_difficulty'].value_counts().to_frame()

# %% [markdown]
# If you need to name index column and rename a column, with counts in the dataframe you can convert to dataframe in a slightly different way.

# %%
value_counts = df['course_difficulty'].value_counts()
df_value_counts = pd.DataFrame(value_counts)
df_value_counts = df_value_counts.reset_index()
df_value_counts.columns = ['unique_values','counts for course_difficulty']
df_value_counts

# %% [markdown]
# ### 9.) Group by and value_counts
# This is one of my favourite uses of the value_counts(0 function and an underutilized one too.  `Groupby` is a very powerful pandas method.  You can group by one column and count the values of another column per this column value using `value_counts`.
#
# **Syntax** - `df.groupby('your_column_1')['your_column_2'].value_counts()`  
#
# Using `groupby` and `value_counts` we can count the number of certificate types for each type of course difficulty.

# %%
df.groupby('course_difficulty')['course_Certificate_type'].value_counts()

# %% [markdown]
# This is a multi-index, a valuable trick in pandas dataframe which allows us to have a few levels of index hierarchy in our dataframe.  In this case, the course difficulty is the level 0 of the index and the certificate type is on level 1.

# %% [markdown]
# ### 10. Pandas value counts with a constraint
# When working with a dataset, you may need to return the number of occurences by your index column using `value_counts()` that are also limited by a constraint.  
#
# **Syntax** - `df['your_column'].value_counts().loc[lambda x: x>]`  
#
# The above quick one-liner will filter out counts for unique data and see only data where the value in the specified column is greater than 1.  
#
# Let's demonstrate this by limiting course rating to be greater than 4.

# %%
df['course_rating'].value_counts()

# %%
df['course_rating'].value_counts().loc[lambda x: x>4]

# %%
