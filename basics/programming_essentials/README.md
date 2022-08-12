# Essentials

Will try to answer question **_why_** we need things we have in python

## Variables
Variable is a link to the place in memory (value)
```python
x = 2
# Now variable x link us to value 2
b = x
# Now variable b links us to value x links to

# You can check it by running code below
a = 2
b = a
print('current a value', a)
print('current b value', b)
a = 3
print('variable a updated')
print('current a value', a)
print('current b value', b)
```
We need variables to verbally describe what value means
```python
x = 'pasha' # Wtf is 'pasha'?
name = 'pasha' # Oh, it's a name
```
We need variables to transfer data
```python
function_result = function()
other_result = other_function(function_result)
```

## Conditional statements
Well that's actually why programming exists ;).

We need to decide what to do, depending on what we have.

## Loops
We need loops to iterate through data and do smth for each element.
```python
# Let's imagine we want to know the sum of all numbers
# between 1 and 10
# Without loop
sum = 0
sum += 1
sum += 2
# ...
sum += 10
# Does this suck? A lot!
# With loop
sum = 0
for num in range(1, 11):  # from 1 to 10
    sum += num
# Does this need further explanation?
```
## Exceptions
We need them to handle exceptional (wow) situations.

We can't be sure that everything will run smoothly
(especially regarding user input), so python gives us a possibility
to properly handle this

## Functions
Functions allow us to seprate some code blocks, and parametrize them

e.g. calculating sum for numbers in range
```python
# What we've done before
sum = 0
for num in range(1, 11):  # from 1 to 10
    sum += num
# Okay, but what if we want to change it,
# so we calculate numbers from 1 to 100
sum = 0
for num in range(1, 101):  # from 1 to 100
    sum += num
# And now from 1 to 1000
sum = 0
for num in range(1, 1001):  # from 1 to 1000
    sum += num
# Hm, now we have 3 pieces of code
# which only have 1 different number each

# Time to deal with this
def range_sum(max_number: int) -> int:
    sum = 0
    for num in range(1, max_number):
        sum += num
    return sum

sum_to_10 = range_sum(11)
sum_to_100 = range_sum(101)
sum_to_1000 = range_sum(1001)
```
That's why function inputs are _parameters_,
because they _parametrise_ code.

Basically it's creating _variable_ :scream: parts of code,
which is good because it helps us to not repeat ourselves

N.B. In programming we have a DRY principle, [here](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/intro-to-clean-code/dry-modular-code/) is the link

## Classes
Classes are another programming tool which opens [OOP](https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP) for us

The idea of classes is to put together data
(class attributes) and functions (class methods).
That allows us to follow DRY principle,
and create some [abstractions](https://www.educative.io/edpresso/what-is-abstraction-in-programming),
which helps us to operate code
without knowing how something is actually implemented (encapsulation).

That's really handy when you are using someone else code,
so you can read smth like `users.get_by_name(username)`
and know that this will give you a user, without knowing _how it's actually made_.

#### Important !
You need to understand what is interface in OOP.

Interface is declaration of methods & attributes class/object should have, without necessarily implementing them.

So when I leave in exercises smth like

```python3
class SomeClass:
    def __init__(self, param1: int, param2: str):
        pass

    def method_a(self, param1: list[str]) -> int:
        '''Write method that makes ....'''
        pass
```
I'm basically declaring an interface you should implement
