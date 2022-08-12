from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union


@dataclass
class FormField(ABC):
    console_text: str
    field_name: str

    @abstractmethod
    def validate_input(self) -> Union[str, int, bool]:
        pass


@dataclass
class StringFormField(FormField):
    def validate_input(self) -> str:
        return input(self.console_text)


@dataclass
class IntegerFormField(FormField):
    def validate_input(self) -> int:
        try:
            user_input = int(input(self.console_text))
            return user_input
        except ValueError:
            print("Enter number")
            return self.validate_input()


@dataclass
class BooleanFormField(IntegerFormField):
    def validate_input(self) -> bool:
        user_input = super(BooleanFormField, self).validate_input()
        if user_input not in range(2):
            print("Enter 1 or 0")
            return self.validate_input()
        return bool(user_input)


@dataclass
class Form:
    fields: list[FormField]

    def get_data(self) -> dict:
        result = {}
        for field in self.fields:
            result[field.field_name] = field.validate_input()
        return result


todo_create_form = Form(
    fields=[
        StringFormField("Enter todo's name: ", "name"),
        StringFormField("Enter todo's description: ", "description"),
    ]
)

todo_update_form = Form(
    fields=[
        StringFormField("Enter new todo's description: ", "description"),
        BooleanFormField("Enter todo status, use 1 for finished, 0 for unfinished: ", "is_finished"),
    ]
)

user_create_form = Form(fields=[StringFormField("Enter username", "username")])
