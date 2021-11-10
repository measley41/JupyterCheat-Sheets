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
# ### Google style docstrings

# %%
def function(arg_1, arg_2=42):
    """Description of what the function does.
    
    Args:
      arg_1 (str): Description of arg_1 that can break onto the next line
        if needed.
      arg_2 (int, optional): Write optional when an argument has a default
        value.
        
    Returns:
      bool: Optional description of the return value
      Extra lines are not indented
      
    Raises:
      VAlueError: Include any error types that the function intentionally
        raises.
        
    Notes:
      See https://www.datacamp.com/community/tutorials/docstrings-python
      for more info.
    """


# %% [markdown]
# ### Numpydoc style docstrings

# %%
def function(arg_1, arg2=42):
    """
    Description of what the function does.
    
    Parameters
    ----------
    arg_1 : expected type of arg_1
      Description of arg_1.
    arg_2 : int, optional
      Write optional when an argument has a default value.
      Default=42.
      
    Returns
    -------
    The type of the return value
      Can include a description of the return value.
      Replace "Return" with "Yields" if this function is a genrator.
    """


# %% [markdown]
# ### Retrieving docstrings

# %%
def the_answer():
    """Return the answer to life,
    the universe, and everything.
    
    Returns:
      int
    """
    return 42


# %%
print(the_answer.__doc__)

# %% [markdown]
# To see a cleaner version without leading whitespaces:

# %%
import inspect
print(inspect.getdoc(the_answer))

# %% [markdown]
# ### Dry and Do One Thing
#
# DRY - Don't repeat yourself
#
# Before:

# %%
import pandas as pd

train = pd.read_csv('train.csv')
train_y = train['labels'].values
train_X = train[col for col in train.columns if col != 'labels'].values
train_pca = PCA(n_components=2).fit_transform(train_X)
plt.scatter(train_pca[:,0], train_pca[:,1])

val = pd.read_csv('val.csv')
val_y = val['labels'].values
val_X = val[col for col in val.columns if col != 'labels'].values
val_pca = PCA(n_components=2).fit_transform(val_X)
plt.scatter(val_pca[:,0], val_pca[:,1])

test = pd.read_csv('test.csv')
test_y = test['labels'].values
test_X = test[col for col in test.columns if col != 'labels'].values
test_pca = PCA(n_components=2).fit_transform(test_X)
plt.scatter(test_pca[:,0], test_pca[:,1])

# %%
import pandas as pd
train = pd.read_csv('train.csv')


# %% [markdown]
# First pass - create a function:

# %%
def load_and_plot(path):
    """Load a data set and plot the first two principal components.
    
    Args:
      path (str): The location of a CSV file.
      
    Returns:
      tuple of ndarray: (features, labels)
    """
    data = pd.read_csv(path)
    y = data['label'].values
    X = data[col for col in train.columns if col != 'label'].values
    pca = PCA(n_components=2).fit_transform(X)
    plt.scatter(pca[:,0], pca[:,1])
    return X, y

train_X, train_y = load_and_plot('train.csv')
val_X, val_y = loa_and_plot('validation.csv')
test_X, text_y = load_and_plot('test.csv')


# %% [markdown]
# Better, but the function does more than one thing.
#
# Do One Thing:

# %%
def load_data(path):
    """Load a data set.
    
    Args:
      path (str): The location of a CSV file.
      
    Returns:
      tuple of ndarray: (features, labels)
    """
    data = pd.read_csv(path)
    y = data['labels'].values
    X = data[col for col in data.columns]
      if col != 'labels'].values
    return X, y

def plot_data(X):
    """Plot the first two principal components of a matrix.
    
    Args:
      X (numpy.ndarray): The data to plot.
      """
    pca = PCA(n_components=2).fit_transform(X)
    plt.scatter(pca[:,0], pca[:,1])
    


# %% [markdown]
# Lists are mutable:

# %%
def foo(x):
    x[0] = 99
    
my_list = [1,2,3]
foo(my_list)
print(my_list)


# %% [markdown]
# Integers are immutable:

# %%
def bar(x):
    x = x + 90
    
my_var = 3
bar(my_var)
print(my_var)

# %% [markdown]
# ### Context Managers
#
# Five parts to defining a context manager:
# 1. Define a function
# 2. (optional) Add any set up code your context needs.
# 3. Use the "yield" keyword.
# 4. (optional) Add any teardown code your context needs.
# 5. Add the `@contextlib.contextmanager` decorator.

# %%
import contextlib

@contextlib.contextmanager
def my_context():
    print('hello')
    yield 42
    print('goodbye')


# %%
with my_context() as val:
    print(f"The value is: {val}")

# %% [markdown]
# Another example:

# %%
import time
import contextlib

@contextlib.contextmanager
def timer():
    """Time the execution of a context block
    
    Yields: None
    """
    start = time.time()
    #Send control back to the context block
    yield
    
    end = time.time()
    print(f"Elapsed: {end-start:.2f}s")


# %%
with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)


# %% [markdown]
# ### Handling errors that occur when using context managers
#
# If a user creates an error before you return to the context manager, it doesn't get a change to clean up.  
# In order to handle this, use `try` and `finally` so that the cleanup can be done:

# %%
def get_printer(ip):
    p = connect_to_printer(ip)
    
    try:
        yield
    finally:
        p.disconnect()
        print('disconnected from printer')


# %% [markdown]
# ### Functions as objects / variables

# %%
def my_function():
    print('Hello')

x = my_function
type(x)

# %%
x()

# %%
PrintyMcPrintface = print
PrintyMcPrintface('Python is awesome')

# %%
list_of_functions = [my_function, open, print]
list_of_functions[2]('I am printing with an element of a list')

# %%
dict_of_functions = {
    'func1': my_function,
    'func2': open,
    'func3': print
}

dict_of_functions['func3']('I am printing with a value of a dict')


# %%
def has_docstring(func):
    """Check to see if the function
    'func' has a docstring
    
    Args:
        func (callable): A function.
        
    Returns:
        bool
    """
    return func.__doc__ is not None


# %%
has_docstring(print)

# %%
has_docstring(my_function)


# %% [markdown]
# ### Nested Functions

# %%
def foo(x,y):
    if x>4 and x<10 and y>4 and y<10:
        print(x*y)


# %%
foo(5,5)


# %%
def foo(x,y):
    def in_range(v):
        return v>4 and v<10
    
    if in_range(x) and in_range(y):
        print(x*y)


# %%
foo(5,5)


# %% [markdown]
# ### Function can return a function

# %%
def get_function():
    def print_me(s):
        print(s)
        
    return print_me


# %%
new_func = get_function()
new_func('hello')

# %% [markdown]
# ### Variable Scopes

# %%
x = 7
y = 200
print(f"x outside foo is:{x}")

def foo():
    x = 42
    print(f"x in foo is: {x}")
    print(f"y in foo is: {y}")
    
foo()

# %% [markdown]
# - First, the interpreter looks in the local scope.
#     - When you're inside a function, the local scope includes the arguments and variable defined inside the function.
# - In the case of nested functions, the outer function is considered the 'non-local' scope
# - Next, it expands its search to the global scope
#     - Things defined outside the local scope
# - Finally, it checks the built-in scope
#
# **Note:** Python only gives you read access to variables defined outside of your current scope.  In order to access the variable from another scope, it must be declared using the **global** keyword:

# %%
x = 7

def foo():
    global x
    x = 42
    print(f"x in foo: {x}")
    
foo()
print(f"x outside foo: {x}")

# %% [markdown]
# You should avoid using the global variables whenever possible.  
# If you want to use the non-local variable in the local scope, you must use the **nonlocal** keyword:

# %%
x = 5
print(f"global x: {x}")
def foo():
    x = 10
    print(f"x in foo before bar: {x}")
    
    def bar():
        nonlocal x
        x = 200
        print(f"x in bar: {x}")
        
    bar()
    print(f"x in foo after bar: {x}")
    
foo()

print(f"global x: {x}")

# %%
x = 50

def one():
    x = 10
    
def two():
    global x
    x = 30
    
def three():
    x = 100
    print(x)
    
for func in [one, two, three]:
    func()
    print(x)
    
# guess: 50, 30, 100, 30

# %% [markdown]
# ### Closures
#
# A closure is PYthon's way of attaching nonlocal variables to a returned function so that the function can operate even when it is called outside of its parent's scope.

# %%
def foo():
    a = 5
    def bar():
        print(a)
    return bar

func = foo()

func()


# %% [markdown]
# When foo() returned the new bar() function, Python attached any nonlocal variable that bar() was going to need to the function object.  
# Those variables get stored in a tuple in the `__closure__` attribute of the function.

# %%
type(func.__closure__)

# %%
print(f"type: {type(func.__closure__)}")
print(f"length: {len(func.__closure__)}")
print(f"contents: {func.__closure__[0].cell_contents}")

# %% [markdown]
# ### Closures and Deletion
# In the following example, `x` is created in the global scope.  
# `foo()` creates a function `bar()` that prints whatever argument was passed to `foo()`.<br> 
# When we call `foo()` and assign the result to "my_func", we pass in "x".  
# So, as expected, calling `my_func()` prints the value of x.  
#

# %%
x = 25

def foo(value):
    def bar():
        print(value)
    return bar

my_func = foo(x)
my_func()

# %% [markdown]
# But, if we delete x and call my_func again, it still prints 25 because foo()'s "value" argument gets added to the closure attached to the new "my_func" function.  
# Even though "x" doesn't exist anymore, it's value persists in its closure.

# %%
del(x)
my_func()

# %% [markdown]
# ### Closures and overwriting
#
# Nothing changes if we overwrite x instead of deleting it.  The value still persists:

# %%
x = 25

def foo(value):
    def bar():
        print(value)
    return bar

x = foo(x)
x()
