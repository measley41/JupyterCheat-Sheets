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
# # 7 Levels of Using the Zip function in Python
# by Yang Zhou in [medium](https:/medium.com/techtofreedom/7-levels-of-using-the-zip-function-in-python-a4bd22ee8bcd)  
#
# ### Level 0: Basic Usage of the Zip Function  
#
# The zip function aggregates items from different <u>iterables</u>, such as lists, tuples or sets, and returns an <u>iterator</u>.

# %%
id = [1,2,3,4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates','Yang Zhou']
record = zip(id, leaders)

print(record)

print(list(record))

# %% [markdown]
# As shown above, the zip function returns an iterator of tuples, where the *i*-th tuple contains the *i*-th element from each of the lists.  
#
# ### Level 1: Zip Less or More Iterables at Once  
#
# Zip can deal with any number of iterables at once rather than just two.  
# One list:

# %%
id = [1,2,3,4]
record = zip(id)
print(list(record))

# %% [markdown]
# Three lists:

# %%
id = [1,2,3,4]
leaders = ['Elon Mask','Tim Cook','Bill Gates','Yang Zhou']
sex = ['male','male','male','male']
record = zip(id, leaders, sex)

print(list(record))

# %% [markdown]
# ### Level 2: Deal with Unequal Length Arguments
#
# By default, the result of the zip function is based on the shortest iterable:

# %%
id = [1,2]
leaders = ['Elon Mask','Tim Cook','Bill Gates','Yang Zhou']
record = zip(id, leaders)

print(list(record))

# %% [markdown]
# To use the longest iterable, use `zip_longest`, with the optional `fillvalue` argument:

# %%
from itertools import zip_longest
id=[1,2]
leaders = ['Elon Mask','Tim Cook','Bill Gates','Yang Zhou']

long_record = zip_longest(id, leaders)
print(list(long_record))

long_record2 = zip_longest(id, leaders, fillvalue='Top')
print(list(long_record2))

# %% [markdown]
# ### Level 3: Know the Unzip Operation
# Python doesn't have a separate unzip function, but asterisks allow us to unpack them.  
# In this example, the asterisk unpacks all four tuples from the record list:

# %%
record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4,'Yang Zhou')]
id, leaders = zip(*record)
print(id)

print(leaders)

# %% [markdown]
# The asterisk technique above is the same as this:

# %%
record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4,'Yang Zhou')]

print(*record)

id, leaders = zip((1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou'))
print(id)

print(leaders)

# %% [markdown]
# ### Level 4: Create and Update Dictionaries by the Zip Function
#
# There are two one-line solutions for creating or updating a `dict` based on lists:

# %%
id = [1,2,3,4]
leaders = ['Elon Mask','Tim Cook','Bill Gates','Yang Zhou']

# create dict by dict comprehension
leader_dict = {i: name for i, name in zip(id, leaders)}
print(leader_dict)

# create dict by dict function
leader_dict_2 = dict(zip(id, leaders))
print(leader_dict_2)

# update existing dict
other_id = [5,6]
other_leaders = ['Larry Page','Sergey Brin']
leader_dict.update(zip(other_id, other_leaders))
print(leader_dict)

# %% [markdown]
# ### Level 5: Use the Zip Function in For-Loops

# %%
products = ['cherry', 'strawberry','banana']
price = [2.5, 3, 5]
cost = [1, 1.5, 2]
for prod, p, c in zip(products, price, cost):
    print(f'The profit of a box of {prod} is ${p-c}!')

# %% [markdown]
# ### Level 6: Get the Transpose of a Matrix

# %%
matrix = [[1,2,3],[1,2,3]]
matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)

