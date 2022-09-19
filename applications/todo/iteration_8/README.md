# Task

None :)

# Summary


So you managed to pretty nice app, but let's make some analysis.

I'll take code from my example of an app to show some concepts.

### Models

So what models actually are.

Models are core data of an application, in our case it's `Todo` and `User` model.

Usually models directly interacts with database, we haven't done that, but will do this in next application (blog)

`Action` class is not a model because we don't store data it represents, it just helps us to organize code.

Usually when you prototype you do modeling (incredible). Basically describing models,
their data and relations (see more bellow)

### Relations

It's how data is related to each other.

In our case one `User` have many `Todo`s. That relation called one to many (unexpected).

But from `Todo` perspective it's many to one. Many todos can have the same user


### Views
A view is a visual representation of data.
In our case it's when we print something, for web it's html/css you see on the page.

Examples of a views
```python

def _select_todo(user_id: int) -> Todo:
    # We have prints inside select_item if you remember
    # So everytime we use this function it's a view
    return select_item(list(filter(lambda todo: todo.user_id == user_id, DATA['todo'])), "Select todo:\n")

def _create_todo(user_id: int):
    name = input("Enter name:\n")
    description = input("Description:\n")
    todo = Todo(id=calculate_id('todo'), name=name, description=description, is_completed=False, created_at=datetime.now(), user_id=user_id)
    DATA['todo'].append(todo)
    # A view
    print(f"Todo {todo.name} created!")


def _update_todo(user_id: int):
    todo = _select_todo(user_id)
    todo.is_completed = not todo.is_completed
    # A view
    print(f"Todo {todo.name} is_completed is now {todo.is_completed}")


def _delete_todo(user_id: int):
    todo = _select_todo(user_id)
    DATA['todo'].remove(todo)
    # A view
    print(f"Todo with id {todo.id} was deleted")


def _get_todo(user_id: int):
    todo = _select_todo(user_id)
    # A view
    print(
        f"Name: {todo.name}\nDescription: {todo.description}\nCompleted:{todo.is_completed}\nCreated at: {todo.created_at}"
    )


def _list_todos(user_id: int):
    # A view
    for todo in filter(lambda todo: todo.user_id == user_id, DATA['todo']):
        print(str(todo))
```
### Controller

Controller controls (wow) what models and views do, basically sending data between view and model.

In our case actions are controllers

### MVC

Haha, you didn't notice but you already now the most common backend architecture.

[Here](https://towardsdatascience.com/everything-you-need-to-know-about-mvc-architecture-3c827930b4c1) you can read more

But don't dive to deep it will be more relevant once we start building web apps.

### Serialization/Deserialization

It's process of loading data to/from source.

Serialization is reading data from source and returning its representation (model).

Deserialization is deconstructing representation to them format source can accept (making dict from model)

In our case it's this code in `BaseModel` class (usually you'll have separate classes called 'serializers' to handle this).
```python
    # Deserialization
    def to_dict(self):
        data = asdict(self)
        data["created_at"] = self.created_at.strftime(DATE_FORMAT)
        return data
    # Serialization
    @classmethod
    def from_json(cls, data: dict) -> "BaseModel":
        data["created_at"] = datetime.strptime(data["created_at"], DATE_FORMAT)
        return cls(**data)
```
