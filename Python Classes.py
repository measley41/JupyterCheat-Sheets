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
# # Python Classes
# from [A Comprehensive Guide for Classes in Python](https://towardsdatascience.com/a-comprehensive-guide-for-classes-in-python-e6bb72a25a5e) by [Soner Yildirim](https://sonery.medium.com)  
# and [How to Use Python Classes Effectively](https://towardsdatascience.com/how-to-use-python-classes-effectively-10b42db8d7bd) by [Rhea Moutafis](https://rheamoutafis.medium.com/)  
#
# <a id = 'Contents'></a>
# ## Contents
# - [What is a class in Python?](#What_Is)    
# - [Creating a class](#Creating)  
# - [Defining class methods](#Methods)  
# - [Class vs instance variables](#Class_vs_Instance)    
# - [Creating a child class](#child)  
#
#
# - [Python classes: the very basics](#basics)

# %% [markdown]
# <a id='What_Is'></a>
# ### What is a class in Python?
#
# Classes possess the following information:  
# - Data attributes: What is needed to create an instance of a class
# - Methods (i.e. procedural attributes): How we interact with instances of a class.  
#

# %% [markdown]
# [Return To Top](#Contents)
# <a id = 'Creating'></a>
# ### Creating a Class
#
# The following code creates a class called Book:

# %%
class Book():
    def __init__(self, name, writer, word_length):
        self.name = name
        self.writer = writer
        self.word_length = word_length


# %% [markdown]
# The `__init__` is a special function that is automatically executed when an instance of a class is created.  It is also called the *class constructor*.  
#
# The parameters of the init function represent the data attributes of a class.  
# Thus, if we need to specify the arguments for name, writer, and length parameters to create an instance of Book.  
# > **Note**: Self refers to the instance istself.  You can use any word instead of 'self' but it is a highly common practice to use 'self'.
#
# Let's create an instance:

# %%
b1 = Book('Pandas', 'John Doe', 100000)

print(type(b1))

# %% [markdown]
# b1 is an object that belongs to the Book class.  We can confirm it by using the type function which returns the type of an object.  
# We can access or modify the attributes of a class using the following way:

# %%
print(f"b1's name is {b1.name}.")
b1.name = 'NumPy'  #updates the name attribute

print(f"Now b1's name is {b1.name}.")


# %% [markdown]
# [Return To Top](#Contents)
# <a id='Methods'></a>
# ### Defining Class Methods
#
# The Book class only has data attributes.  Adding methods make it more useful and functional.  
# For instance, we can implement a method that returns the number of pages given the fontsize.  We specify the length of the book in number of words.  The method will calculate the number of pages based on the length and fontsize.

# %%
class Book():
    def __init__(self, name, writer, word_length):
        self.name = name
        self.writer = writer
        self.word_length = word_length
        
    def number_of_pages(self, fontsize=12):
        word_length = self.word_length
        if fontsize==12:
            words_in_page = 300
        else:
            words_in_page = 300 - (fontsize-12)*10
        return round(word_length / words_in_page)


# %% [markdown]
# If a function we declare inside a class definition needs to access data attributes of an instance, we need to tell the function how to access them.  This is what we did in the first line of the number_of_pages function.  
#
# We can access a method from the class or the instance.  Here is a simple example that demonstrates both ways.

# %%
b1 = Book("Pandas", "John Doe", 100000)

print(b1.number_of_pages())

print(Book.number_of_pages(b1))

# %% [markdown]
# The number_of_pages function has an additional fontsize parameter.  Since a default value (12) is specified, we do not have to explicity write it.  
# However, we can use a different value for the fontsize parameter.

# %%
print(b1.number_of_pages(14))

print(b1.number_of_pages(fontsize=16))

# %% [markdown]
# As the fontsize increases, the number of pages also increases which make sense.  
#
# There are certain methods that we need to define for our class in order to use some built-in functions of Python.  Consider the print function.

# %%
print(b1)


# %% [markdown]
# The print function returns the type and the memory location of the object by default.  However, we can customize its behavior by implementing the `__str__` method in our class.  
#
# We add the `__str__` method in our class definition above:

# %%
class Book():
    def __init__(self, name, writer, word_length):
        self.name = name
        self.writer = writer
        self.word_length = word_length
        
    def __str__(self):
        return "<" + self.name + ", by" + self.writer + ">"
        
    def number_of_pages(self, fontsize=12):
        word_length = self.word_length
        if fontsize==12:
            words_in_page = 300
        else:
            words_in_page = 300 - (fontsize-12)*10
        return round(word_length / words_in_page)


# %%
b1 = Book("Pandas", "John Doe", 100000)
print(b1)


# %% [markdown]
# [Return to Top](#Contents)
# <a id='Class_vs_Instance'></a>
# ### Class vs Instance Variables
#
# Class variables are declared inside a class but outside of any function.  
# Instance variables are declared inside the constructor which is the `__init__` method.  
#
# The class variables are more general and likely apply to all of the instances of a class.  On the other hand, instance variables are more specific and defined for each instance separately.  Having a distinction between class and instance variables is quite useful.  
#
# Consider the Book class we defined earlier.  We run a publishing company and have some standards for the books we publish such as page width and color for the cover.  If we define them as class variables, we do not have to explicity declare for each instance created.

# %%
class Book():
    page_width = 14
    cover_color = 'blue'
    
    def __init__(self, name, writer, word_length):
        self.name = name
        self.writer = writer
        self.word_length = word_length
        
    def __str__(self):
        return "<" + self.name + ", by" + self.writer + ">"
        
    def number_of_pages(self, fontsize=12):
        word_length = self.word_length
        if fontsize==12:
            words_in_page = 300
        else:
            words_in_page = 300 - (fontsize-12)*10
        return round(word_length / words_in_page)


# %% [markdown]
# We have implemented the page_width and cover_color as class variables because they are inside the class definition but outisde any function definition.  
#
# Let's create an instance of the Book class.

# %%
b2 = Book("Machine Learning", "Jane Doe", 120000)

# %% [markdown]
# We have not specified the class variables while creating this instance.  However, the b2 possesses these variables and we can access them.

# %%
print(b2.page_width)
print(b2.cover_color)

# %% [markdown]
# We have the option to change the class variables for a particular instance.

# %%
b2.cover_color = 'red'

b2.cover_color

# %% [markdown]
# The changes on a particular instance to not have any effect on the class variable.

# %%
Book.cover_color


# %% [markdown]
# However, this approach to changing attributes is not recommended.  Instead, we can implement methods to get and set the attribut values (aka getters and setters)

# %%
class Book():
    page_width = 14
    cover_color = 'blue'
    
    def __init__(self, name, writer, word_length):
        self.name = name
        self.writer = writer
        self.word_length = word_length
        
    def __str__(self):
        return "<" + self.name + ", by" + self.writer + ">"
        
    def number_of_pages(self, fontsize=12):
        word_length = self.word_length
        if fontsize==12:
            words_in_page = 300
        else:
            words_in_page = 300 - (fontsize-12)*10
        return round(word_length / words_in_page)
    
    def set_cover_color(self, cover_color):
        self.cover_color = cover_color
        
    def get_cover_color(self):
        return self.cover_color

b2 = Book("Machine Learning", "Jane Doe", 120000)

# %%
print(b2.get_cover_color())
b2.set_cover_color("purple")
print(b2.get_cover_color())


# %% [markdown]
# [Return to Top](#Contents)
# <a id='child'></a>
# ### Creating a Child Class
# We can create a child class based on a different class.  Let's create a class called "ColorBook" based on the "Book" class. 
#
# ```
# class ColorBook(Book):
# ```

# %% [markdown]
# The ColorBook is a child class of the Book class.  When we create a class in this way, the child class copies the attributes (both data and procedural) from the parent class.  This concept is called **inheritance** which makes the OOP more efficient and powerful.  
#
# It is similar to inheritance in real life.  Most of our genome come from our parents or ancestors.  We inherit from them.  Thus, we have similarities with our parents.  
#
# A child class can have new attributes in addition to the ones inherited from the parent class.  Furthermore, we have the option to modify or override the inherited attributes.  
#
# Let's define the `__init__` function of the ColorBook class.  It will have two additional parameters which are "color" indication of the color of pages and "has_image" indicating if there are images in the book.

# %%
class ColorBook(Book):
    
    def __init__(self, name, writer, word_length, color, has_image):
        Book.__init__(self, name, writer, word_length)
        self.color = color
        self.has_image = has_image


# %% [markdown]
# Since the name, writer, and word_length have already been defined in the Book class, we can just copy the `__init__` method from it.  We just need to define the additional attributes.  
#
# **Note:** We are free to define each data attribute manually for the child class.  
# Using the `__init__` of the parent is optional.  
#
# Let's create an instance of the ColorBook class.

# %%
c1 = ColorBook("Seaborn", "John Doe", 90000, "green", True)

print(c1.name)
print(c1.color)

# %% [markdown]
# The child class also inherits the class variables.

# %%
print(c1.cover_color)
print(c1.page_width)

# %% [markdown]
# The methods are also copied from the parent class.  For the Book class, we defined two methos that can also be used on the instances of the ColorBook class.

# %%
print(c1.number_of_pages())

print(c1)


# %% [markdown]
# We have the option to override the data and procedural attributes (i.e. methods) inherited from the parent class.  This makes the inheritance even more powerful because we are obligated to use everything in the parent class.  
#
# For instance, we can modify the `__str__` method for the ColorBook class.

# %%
class ColorBook(Book):
    
    def __init__(self, name, writer, word_length, color, has_image):
        Book.__init__(self, name, writer, word_length)
        self.color = color
        self.has_image = has_image
        
    def __str__(self):
        return "<" + self.name + ", in " + self.color + ">"


# %% [markdown]
# The print function will return the name of the book and its color.

# %%
c1 = ColorBook("Seaborn", "John Doe", 90000, "green", True)

print(c1)


# %% [markdown]
# [Return to Top](#Contents)
# <a id='basics'></a>
# ### Python classes: the very basics 
#
# Classes are objects that allow you to group data structures and procedures in one place.  For example, imagine you're writing a piece of code to organize the inventory of a clothes shop.  
#
# You could create a class that takes each item of clothing in the shop, and stores key quantities such as the type of clothing, and its color and size.  We'll add an option to add a price, too.  

# %%
class Clothing(object):
    def __init__(self, type, color, size, price=None):
        self.type = type
        self.color = color
        self.size = size
        self.price = price


# %% [markdown]
# Now, we can define various instances of the class and keep them organized:

# %%
bluejeans = Clothing("jeans", "blue", 12)
redtshirt = Clothing("t-shirt", "red", 10, 10)


# %% [markdown]
# We would add these two lines without indent, after the definition of the class.  The code will run, but it's not doing very much.    
#
# We can add a method to set the price directly underneath the `__init__` function, within the class definition.
#
# We could also add some routines to tell us the price, or to promote an item by reducing the price:

# %%
class Clothing(object):
    def __init__(self, type, color, size, price=None):
        self.type = type
        self.color = color
        self.size = size
        self.price = price
        
    def set_price(self, price):
        """Set the price of an item of clothing."""
        self.price = price
        print(f"Setting the price of the {self.color} {self.type} to ${price}.")
        
    def get_price(self):
        """Get the price of an item of clothing, if price is set."""
        try:
            print(f"The {self.color} {self.type} costs ${self.price}.")
        except:
            print(f"The price of the {self.color} {self.type} hasn't been set yet!")
            
    def promote(self, percentage):
        """Lower the price, if initial price is set."""
        try:
            self.price = self.price * (1-percentage/100)
            print(f"The price of the {self.color} {self.type} has been reduced by {percentage} percent!  It now only costs ${self.price:.0f}.")
        except:
            print(f"Oops.  Set an initial price first!")
            
bluejeans = Clothing("jeans", "blue", 12)
redtshirt = Clothing("t-shirt", "red", 10, 10)

# %% [markdown]
# Now we can add some calls of our methods after the lines where we've initialized the instances of the class:

# %%
print("blue jeans --------------------")
bluejeans.promote(20)
bluejeans.set_price(30)
bluejeans.get_price()

# %%
print("red t-shirt --------------------")
redtshirt.get_price()
redtshirt.promote(20)

# %% [markdown]
# If you need to add more routines, you can just put them in the class definition.  
#
# The nicest part of all of this is that you can add and delete as many objects as you like.  Deleting an attribute goes like so:

# %%
del redtshirt.price

# %% [markdown]
# And if you want to delete an entire object, you do like so:

# %%
del redtshirt

# %% [markdown]
# All of this is neat, simple, and expandable.  Try doing this implementation with standard functions, and you'll probably have a lot more trouble dealing with it.  
#
# From a theoretical point of view, there are more reasons why Python classes are a beautiful concept in many situations.

# %% [markdown]
#
