"""User directory."""

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    name: str
    tier: str


_USERS = {
    1: User(1, "amira hassan", "gold"),
    2: User(2, "omar said", "standard"),
    3: User(3, "laila farouk", "standard"),
}


def find_user(user_id):
    """Return the user, or None when the id is unknown."""
    return _USERS.get(user_id)


def display_name(user_id):
    """Name shown in the order header."""
    user = find_user(user_id)
    if user is None:
        return f"user {user_id}"
    return user.name.title()
