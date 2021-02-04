#!/usr/bin/env python
# coding: utf-8

# A. VARIABLE
# 
# Variable is a placeholder for unknown numbers / expressions.
# 
# In python, the format in making a variable will be - 
# name_of_the_variable = value. For the example :

# In[1]:


x = 10


# 
# B. DATA TYPES & CONVERSION

# Data Types
# 
# Every quantity in the value can be distinguished into many types such as :

# 1. Boolean

# In[3]:


x = True
y = False


# states "True" value of 1 and "False" for value 0.

# 2. String

# In[4]:


z = "Good Morning"


# states a character / sentence which can be letters / numbers (use quotation mark "" or '').

# 3. Integer

# In[5]:


x = 35
y = 100


# states an integer itself (Z).

# 4. Float

# In[7]:


x = 3.14
y = 0.99


# states a decimal number.

# 5. Complex

# In[12]:


x = 1 + 5j


# states a real and imaginer number.

# 6. List

# In[13]:


x = ["xyz", "786", "2.23"]


# contains several values that can comes from various data types & it is changeable.

# 7. Tuple

# In[14]:


x = ("xyz", "786", "2.23")


# same like a list, tuple contains several values that can comes from various data types. But it is not changeable.

# 8. Dictionary

# In[16]:


x = {"nama":"adi", "id": 2}


# contains value of various data types in the form of pointers and values.

# Conversion
# 
# Python defines conversion functions to directly convert one data type to another which is useful in programming.
# 
# There are two types of conversion :

# 1. Implicit
# 
# In this type of conversion, python will automatically converts one data type to another without any user involvement.

# In[18]:


x = 15
print("x is of type :",type(x))

y = 12.4
print("y is of type :",type(y))

z = x + y
print("z is of type :",type(z))


# 2. Explicit
# 
# In this type, user will manually change data type as per their requirement.
# 
# For our example, we use :
# 1) int(a,base) : This function converts any data type to integer. 'Base' specifies the base in which string is if the data type is string.
# 
# 2) float() : this function is used to convert any data type to a floationg point number.

# In[19]:


#defined the string value
s = "10010"

#convert string to integer base 2 then print
c = int(s,2)
print("After converting to integer base 2: ", end="")
print(c)

#convert string to float then print
e = float(s)
print("After converting to float: ", end="")
print(e)


# For this conversion material, my source is from :
# https://www.geeksforgeeks.org/type-conversion-python/
# 
# You can check it there to see the complete explanation!

# In[ ]:




