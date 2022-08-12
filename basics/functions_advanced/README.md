# Functions advanced
A module about advanced usage of functions,
and some related python concepts

## Parameters
Till now, we've used only what called positional arguments.

Two types of parameters exists, positional and keyword arguments.

What's the difference?
```python
# What you already saw
def function_name(  # Indentation in function definition is ok
        param1: Param1Type, param2: Param2Type
) -> ReturnType:
    pass
# And we used it like this
res = function_name(value1, value2)
# But actually we can also use it like
res = function_name(param1=value1, param2=value2)
# OR
res = function_name(param2=value2, param1=value1)
```
As you can see for keyword arguments (kwargs),
the order in which we pass parameters
doesn't matter, because we are giving python enough info
to understand which value belongs to which parameter

N.B. You most likely won't use kwargs
for this simple functions, because you would have smth like
```python
res = send_email(email, text)
```
And this is descriptive enough

### Args, Kwargs!
Sometimes your function may have a lot of parameters

```python
# Imagine having filter function like this
def get_users(
        first_name: str, last_name: str, age: int,
        gender: str, address: str, occupation: str,
        balance: int
) -> list[User]:
# What we have here forces us to
# pass ALL these parameters to the function
users_with_name_james = get_users(
    'james', None, None,
    None, None, None,
    None
)  # Looks sad :(

# An upgraded version
from typing import Optional
def get_users(
        first_name: Optional[str] = None, last_name: Optional[str] = None,
        age: Optional[int] = None, gender: Optional[str] = None,
        address: Optional[str] = None, occupation: Optional[str] = None,
        balance: Optional[int] = None
) -> list[User]:
# Now every parameter is optional,
# and we have a lot to handle inside function
# BUT using it will be much more comfortable

users_with_name_james = get_users('james')


# Somewhat upgraded version
def get_users(*args) -> list[User]:
    pass

# Okay, what happened?
# Adding starred (parameter with "*") parameter
# allows us to accept ANY amount of POSITIONAL arguments
# N.B. name *args is not mandatory
# you can do smth like *shit, and it'll be alright
# But you shouldn't because this is conventional name

# Executable code
def example_function(*args):
    print(args)
    print(type(args))  # Look at the type of args

example_function(
    'I', ['can'], ('pass',), 'Any', set(('arguments',))
)
# Or even
parameters = ['I', ['can'], ('pass',), 'Any', set(('arguments',))]
example_function(*parameters)  # unpacking parameters list to the functions
# Notice that prints are the same
# End of executable code
```

And now time for a big boss

```python
def get_users(**kwargs) -> list[User]:
    pass
# Okay, what happened?
# Adding double starred parameter
# allows us to accept ANY amount of KEYWORD arguments
# N.B. name **kwargs is not mandatory
# you can do smth like **shit, and it'll be alright
# But you shouldn't because this is conventional name

# Executable code
def example_function(**kwargs):
    print(kwargs)
    print(type(kwargs))  # Look at the type of kwargs
# End of executable code
example_function(
    first_name='James', last_name='Cameron',
    occupation='Producer', balance=1_000_000_000,  # A way to write bit numbers
    gender='god'
)
# OR
# A usual use-case
query = {
    'first_name': 'James',
    'last_name': 'Cameron',
    'occupation': 'Producer',
    'balance': 1_000_000_000,
    'gender': 'god'
}
example_function(**query)
# Do you see where it's coming?
```

Using args and kwargs adds much more possibilities to our functions

## Decorator (This will be hard)
What if we want to do some actions before
and after a function call, EVERY time it's called?

Smth like
```python
def example_function():
    pass

if user.is_authenticated:
    example_function()
else:
    raise Exception('You don\'t have permission for this function')
```
And pyton have a thing!
First syntax
```python
@check_permission_decorator
def example_function():
    pass
```
And now we will write `check_permission_decorator`
Decorator is the function, that takes another function as an input

This code is executable
```python
from typing import Callable


def check_permission_decorator(func) -> Callable:  # Returns decorated function
    # declaring so called 'wrapper' function
    def wrapper(*args, **kwargs):  # Basically saying accept anything
        print(args),
        print(kwargs)
        print('Action before function call')
        # user = kwargs.get('user')
        # if user.is_authenticated:
        if True:  # Let's mock this for now, but you see where it's going
            res = func(*args, **kwargs)  # Calling decorated function
            print('Action after function call')
            return res
        else:
            raise Exception('You don\'t have permission for this function')
    print('Function decorated !')
    return wrapper


@check_permission_decorator
def example_function(*args, **kwargs):  # Accepting all parameters isn't mandatory, just for example
    print('Inside decorated function')


example_function(
    'shit', 'here', 'we', 'go', 3, 2, 1,
    some_random_data={'data': 'very_random'}
)
# And example of another way of using decorator
def another_example_function(*args, **kwargs):
    print('Inside another decorate function')

print('ANOTHER WAY')
check_permission_decorator(another_example_function)(
    'shit', 'here', 'we', 'go', 3, 2, 1,
    some_random_data={'data': 'very_random'}
)
# As you see we are passing function itself to the decorator
# And passing arguments to the result of decorator execution
```

N.B. Decorators can also accept arguments,
it should be obvious, because as you see
syntax for `check_permission_decorator` function
is usual,
you can simply add more over there
