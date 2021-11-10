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
# ## 5 Uses of Asterisks in Python
# From [medium.com](https://medium.com/techtofreedom/5-uses-of-asterisks-in-python-3007911c198f) by Yang Zhou
#
# ### Use 1: Multiplication or Exponentiation Operator
# - Single `*` for multiplication  
# ```
# >>> 2*3  
# >>> 6
# ```
# - Double `**` for exponentiation
# ```
# >>> 2**3
# >>> 8
# ```
#
# ### Use 2: To Receive an Unlimited Number of Arguments

# %%
def print_genius(*names):
    print(type(names))
    for n in names:
        print(n)
        
print_genius('Elon Mask', 'Mark Zuckerberg ', 'Yang Zhou')
print()

def top_genius(**names):
    print(type(names))
    for k, v in names.items():
        print(k,v)
        
top_genius(Top1='Elon Mask',Top2='Mark Zuckerberg', Top3='Yang Zhou')


# %% [markdown]
# - A parameter prefixed by one `*` can capture any number of positional agruments into a `tuple`.
# - A parameter prefixed by two `**` can capture any number of keyword arguments into a `dict`.  
#
# By convention, we define a function like the following if the number of its arguments cannot be determined:  
#
# ```
# def func(*args, **kwargs):
#   pass
# ```
#
# ### Use 3: Restrict to Keyword-Only Arguments

# %%
def genius(*, first_name, last_name):
    print(first_name, last_name)
    
genius('Yang','Zhou')


# %%
def genius(*, first_name, last_name):
    print(first_name, last_name)
    
genius(first_name='Yang',last_name='Zhou')


# %% [markdown]
# As shown in the example, arguments following one `*` must be passed as keyword arguments.  
# We can also mix types to have a few positional arguments and restrict a few to keyword-only.

# %%
def genius(age, *, first_name, last_name):
    print(first_name, last_name, 'is', age)
    
genius(28, first_name='Yang',last_name='Zhou')


# %% [markdown]
# ### Use 4: Iterables Unpacking
# We can use asterisks to unpack <u>iterables</u>.<br>
# For example, to combine different iterables, such as one list, one tuple, and one set into a new list, we can use `for` loops:

# %%
A=[1,2,3]
B = (4,5,6)
C = {7, 8, 9}
L = []

for a in A:
    L.append(a)
    
for b in B:
    L.append(b)
    
for c in C:
    L.append(c)
    
print(L)

# %% [markdown]
# We could also use list comprehensions:

# %%
A=[1,2,3]
B = (4,5,6)
C = {7, 8, 9}

L = [a for a in A] + [b for b in B] + [c for c in C]
print(L)

# %% [markdown]
# But asterisks are the cleanest and simplest:

# %%
A=[1,2,3]
B = (4,5,6)
C = {7, 8, 9}

L = [*A, *B, *C]
print(L)

# %% [markdown]
# If we use one single `*` as a prefix of a `dict`, its keys will be unpacked.  If we use double asterisks `**` as a prefix, its values will be unpacked.  However, we must use their keys to receive the unpacked values.  Because of this inconvenience, it's not common to extract items of a `dict` by asterisks.

# %%
D = {'first':1, 'second':2, 'third':3}

print(*D)

# %%
print(**D)

# %%
print('{first},{second},{third}'.format(**D))

# %% [markdown]
# ### Use 5: Extended Iterable Unpacking

# %%
L = [1,2,3,4,5,6,7,8]

a, *b = L

print(a)

print(b)
