# Data structures
A module about a **really** important thing in programming and python

## Simple
### Int
```python
x = 3
y = int('2')
z = int(b'13')
```
### Float
```python
x = 3.12351345
y = float('3.1415926')
print(0.3 + 0.3 + 0.3 == 0.9)

from decimal import Decimal

x = Decimal('0.3')
y = Decimal('0.9')
print(x + x + x == y)
```
### String
```python
x = 'string'
y = "string"
z = str(12.3)
print(x, y, z)

print(x[0])
for char in 'any string':
    print(char)

x = "Python is the best"
y = x.replace('best', 'worst')
print(x)
print(y)
# E.g of common replace usage
url = "smth.com?param=Pasha Mukovoz"
new_url = url.replace(' ', '%20')

res = x.find('is')  # Returns index position of searched string
print(res)

words = x.split(' ')
print(words)
csv_example = '12,Pasha,chlen'
csv_data = csv_example.split(',')
print(csv_data)

x = ' '.join(words)
print(x)

x = x.upper()
print(x)
x = x.lower()
print(x)
x = x.capitalize()
print(x)

print('Python'.isalpha())
print("python3".isalnum())
print("3".isdigit())

name = 'Pasha'
age = 10
print('Hi, my name is ' + name)  # if name is int, we fail
print(f'Hi, my name is {name}, age: {age}')
print("Hi, my name is {}, age: {}".format(name, age))
print("Hi, my name is {1}, age: {0}".format(age, name))
print("Hi, my name is {name=}, age: {age=}".format(name=name, age=age))
```
### Boolean
```python
x = True
y = bool(1)
z = bool(' ')
q = bool([1, 2, 3])  # Non-empty collection
print(x, y, z, q)

x = False
y = bool(0)
z = bool('')
q = bool([])  # Empty collection
u = bool(None)
print(x, y, z, q, u)

some_list = [1]
if some_list:
    # tadada
else:
    # not tadada

print(True + True)

```
### Bytes
```python
x = b'asdgagag'
y = bytes('ahabafdb')
bytes()
```
### None
```python
from typing import Optional
x = None
def name(x: int, y: Optional[list] = None):
    if y:
        pass
    else:
        pass

```

## Complex (Collections)

### List
```python
x = [1, 2, 3]
y = list(1, 2, 3)
res = []
for num in range(1, 11):
    res.append(num)
print(res)
res = list(range(1, 11))
print(res)
res = [num for num in range(1, 11)]  # List comprehension
print(res)

# Append adds object to the end
x = [1]
x.append(2)
print(x)

x = [1]
y = [2]
x += y
print(x)

# Len
print(len(x))


# Pop
x = [1, 2, 3]
print(x.pop())

# Remove
x = [1, 2, 3]
x.remove(2)
print(x)

# Index
x = [1, 2, 3]
print(x.index(2))

# Sort
x = [1, 5, 8, 3, 9]
x = sorted(x)
print(x)


# slices
x = list(range(1, 11))
x = x[2:6]
print(x)

x = list(range(1, 11))
x = x[1::2]  # Even numbers
print(x)

x = list(range(1, 11))
x = x[::-1]  # Reverse
print(x)
```
### Tuple
```python
# Immutable
x = (1, 2, 3)
y = tuple([1, 2, 3])

print(x + x)
```
### Set
```python
# Unique elements only!
x = {1, 2, 3}
y = set([1, 2, 3])
print(x)

# Linear existence search
ex_list = [1, 2, 3]
searched_value = 2
for item in ex_list:
    if item == searched_value:
        break

# Constant existence search
ex_set = {1, 2, 3}
start_len = len(ex_set)
ex_set.add(searched_value)
len_after_add = len(ex_set)
print(start_len == len_after_add)

x = {1, 2, 3}
y = {3, 4, 5}
res = x.intersection(y)
print(res)

# Can contain only hashable (immutable) vales
x = {1, 2, 3, 'a', 'b', (1, 2)} # Valid
print(x)
y = {1, 2, 3, [1, 2, 3]} # Invalid
```

### Dictionary (DICKtionary)
```python
# Key: value pairs
# Keys are basically set
x = {'Pasha': 50, 'Misha': 23, 'Stepan': 21}
y = dict(Pasha=50, Misha=23, Stepan=21)
z = dict([('Pasha', 50), ('Misha', 23), ('Stepan', 21)])
print(x)
print(x.keys())
print(x.values())
print(x.items())

print(x['Pasha'])
print(x.get('Pasha'))

# LBYL
# Look
# Before
# You
# Leap
if 'Gay' in x:
    print(x['Gay'])
else:
    print('No gays here')

# EAFP
# Easier
# to
# Ask
# Forgiveness
# than
# Permission
try:
    print(x['Gay'])
except KeyError:
    print('No gays here')

gay = x.get('Gay', 'default')
```

## Task

Visit `main.py` to see the task,
you should always validate data
you receive in the function
and handle all possible problems,
think about it. Raise Exceptions.

Tests will help you to detect all edge cases.

To test it (assuming you are in the same directory as this file) run
```shell
python -m unittest test.py
```
