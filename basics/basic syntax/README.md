# Syntax 
Quick overview of all basic syntax, more advanced things as we go

Highly recommend to complete [this course](https://www.youtube.com/watch?v=Z1Yd7upQsXY&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg) (11 lessons)
and use exercises here to verify your knowledge

### Variables
```python
var_name: VarType = value
```
Also you can create multiple variables in one line
```python
var_name1, var_name2 = value  # Both variables will have this value
# OR
var_name1, var_name2 = value1, value2 # Variables will have corresponding values
```

Pay attention to the difference between spelling var_name and VarType

To name variables we use snake_case style, it's a way of splitting words using underscore _

VarType is always a class, to name classes we use UpperCamelCase, where we start each word with capital letter

#### N.B. 
To name variables that aren't supposed to change (constants) we change all letters to capital e.g. `SPEED_OF_LIGHT`

To mark "private" (will talk about this later) variables we add _ before the variable e.g. `_some_private_variable` 

### Conditional statement
```python
if condition:
    # Do smth
elif second_condition:
    # Do smth 
else:
    # If none of the above statements are true, do this
```
The only required element here is "if" statement, others are optional


### For loop
```python
for item in collection:
    # do something for item
```
More details [here](https://www.w3schools.com/python/python_for_loops.asp)

### While loop
Encourage you to not use it,
but sometimes it's logically easier to write for while
and then replace it with for loop

[Docs](https://www.w3schools.com/python/python_while_loops.asp)

### Try/except block
```python
try:
    # trying to make some action
except ExceptionType as e:  # <- Catching exception of type ExceptionType,
                            # assigning it to a variable e (most common name for excepiton variable)
    # If exception happened do this
else:
    # If no exception do this
finally:
    # Regardless if exception happened or not, do this
```
Detailed docs & examples [here](https://www.w3schools.com/python/python_try_except.asp)

### Functions
```python
# This is called function signature
def function_name(param_name1: ParamType, param_name2: ParamType = default_value) -> ReturnType:
    # do something

function_name(value1, value2) # <- this is called function call
```
More info [here](https://www.w3schools.com/python/python_functions.asp)

### Classes
```python
# A class definition
class ClasName(ParentClassName1, ParentClassName2):
    pass
class_name_instance = ClasName() # Creating an instance of a class
```
[Docs](https://www.w3schools.com/python/python_classes.asp)


### Scopes
Another important concept in python are **_scopes_**

Each construction has its scope and in python that's indicated by indent

The most common beginner's mistakes

```python3
if statement:
    x = 0

print(x)
# if statement is False we will have no variable x declared
# and the following error
# NameError: name 'x' is not defined
```
```python3
for item in collection:
    some_var = item
print(some_var) 
# If collection was empty you will have NameError,
# otherwise you will have the last item of the collection
# in some_var, encourage to never acquire last item of the collection like this

```
```python3
def some_func(param_a: str):
    # Some code 
    pass

print(param_a)
# param_a exists only inside function, you will get NameError here
```

```python3
some_var = 1
def some_func(param_1: int):
    some_var = param_1

some_func(2)
# Guess what program will print
print(some_var)
```
The value of `some_var` won't change, it's up to you to google why and how to deal with this

The same applies to classes and theirs methods

## Conclusion
So it was a **_very_** basic syntax introduction which you need to start doing something




