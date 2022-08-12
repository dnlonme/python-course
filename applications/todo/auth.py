from typing import Optional

from models import User

_current_user: Optional[User] = None


def get_current_user() -> Optional[User]:
    return _current_user


def authenticate_user(user: User):
    global _current_user
    _current_user = user


def logout():
    global _current_user
    _current_user = None
