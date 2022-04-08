# Classes
A bit more details on classes

## Object instance vs class instance
Everything in pyton is object. 
So the class itself is also object of class 'type'.

Check it out
```python
class Test:
    pass
test_object = Test()
print(type(test_object))
print(type(Test))  # Passing class itself
```
And one more (pay attention to the order of prints)
```python
class Test:
    def __init__(self):
        print('Object created!')
    print('Class instance created!')

Test() # Just creating, no need to assign to anything
```
### Class attributes vs object attributes

```python
from typing import Optional

class User:
    name = 'Jesus'
    surname = 'Christ'
    age = 33
    def __init__(
            self,
            name: Optional[str] = None,
            surname: Optional[str] = None,
            age: Optional[int] = None,
    ): # Every param is optional
        # Assigning value to object only if it's not None
        if name is not None:
            self.name = name
        if surname is not None:
            self.surname = surname
        if age is not None:
            self.age = age
        # Launch method while instance is created
        self.say_hi()
    def say_hi(self):
        print(f'Hi I\'m {self.name} {self.surname} and I\'m {self.age}')

    def say_hi_alternative(self):
        print(
            f'Hi I\'m {self.__class__.name} {self.__class__.surname} and I\'m {self.__class__.age}'
        )
        
jesus = User()
pasha = User(name='Pasha')
stepan = User(name='Stepan', surname='Douchebag', age=21)

# As you can see class attributes are used when you call 
# self.attribute_name, and it wasn't set in __init__

# Look
jesus.say_hi_alternative()
pasha.say_hi_alternative()
stepan.say_hi_alternative()
# Result is the same for all objects because in this method we refer to class attribute
# And we can change class attribute
User.age = 0
jesus.say_hi_alternative()
pasha.say_hi_alternative()
stepan.say_hi_alternative()

```
It's just for example, usually class attributes are
for something every object should have access to.
E.G. (non-executable)
```python
class Password:
    # Some method for password hashing/verifying
    pass

class User:
    _password = Password

    def verify_password(self, password: str) -> bool:
        """Check if password is correct"""
        return self._password.verify(password, self.password)

    def set_password(self, password: str) -> None:
        self.password = self._password.create_hash(password)
```
Also common usage of class attributes is
creating dataclasses and pydantic models 

Dataclass E.G.

```python
from typing import Optional
from dataclasses import dataclass


@dataclass  # Ah, yeah we are decorating class (:
class User:
    # We are just declaring so called 'schema' for the data
    name: Optional[str]
    surname: Optional[str]
    age: Optional[int]


user = User(name='pasha', surname='mukovoz', age=50)
print(user)  # Fine printing
# The same as
class User:
    def __init__(
            self,
            name: Optional[str] = None,
            surname: Optional[str] = None,
            age: Optional[int] = None,
    ): 
        self.name = name
        self.surname = surname
        self.age = age
```

### Class methods
My you've started assuming that if we have class attributes,
that means we can have class methods?

And you are right!
Usually they are used for actions that are logically
connected with the class, but don't need any object info.

```python
from passlib.context import CryptContext


class Password:
    # Adding attribute to the class (object of CryptContext class from library)
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod  # Yeeee another decorator
    # Notice how we are using cls instead of self in the class method
    def verify(cls, plain_password: str, hashed_password: str) -> bool:
        # Using class attribute
        return cls.password_context.verify(plain_password, hashed_password)
        
    @classmethod
    def create_hash(cls, password: str) -> str:
        """Creates password hash"""
        # Using class attribute
        return cls.password_context.hash(password)
```
But can we create 2 different functions to replace this class?

Yes, absolutely, but this effect our object-oriented thinking
and as always classes gives us other OOP features if we need them.

So, it's the matter of how you decide to do this.

### Static methods
Static method are methods which don't have access 
to self or cls.

```python
class Example:
    @staticmethod # Yeah decorator
    def example_method(param1, *args, **kwargs) -> ReturnType:
        pass
```
Yeah, it's just a function as is, the difference is only
that you will call it via class, so it can be used for namespacing.

From the outside, calling classmethod is the same as static method
```python
class Example:
    @staticmethod
    def static_example():
        print('Hi Im static method')

    @classmethod
    def class_example(cls):
        print('Hi Im class method')

Example.static_example()
Example.class_example()  # Using is the same
```
But the difference is that we can call static method from the classmethod,
but we can't do the opposite
```python
class Example:
    @staticmethod
    def static_example():
        print('Hi Im static method')
        # Can't call class method ;(

    @classmethod
    def class_example(cls):
        print('Hi Im class method')
        cls.static_example()  # Can call static method ;)

Example.class_example() 
```

### Properties
What if we want to have attributes, that are calculated
depending on state of the object? 

N.B. 'state' is values of all attributes in the moment

E.g. (Don't forget to tell about the information expert class)
```python
from dataclasses import dataclass
from typing import List

@dataclass
class OrderItem:
    name: str
    price: int
    amount: int

    @property
    def sum(self):
        return self.price * self.amount


@dataclass
class Order:
    items: List[OrderItem]  # <- This is called composition

    # And may be some other attributes, like user, date, status etc
    @property
    def sum(self):
        sum = 0
        for item in self.items:
            sum += item.sum
        return sum
    
    def add_item(self, item: OrderItem):
        self.items.append(item)


apple_item = OrderItem(name='apple', price=10, amount=2)
tomato_item = OrderItem(name='tomate', price=20, amount=5)

order = Order(items=[])
order.add_item(apple_item)
print(order.sum)
order.add_item(tomato_item)
print(order.sum)
```
Of course, we can have .get_sum method, but for what? 
it shouldn't accept any arguments, so we can have simply property