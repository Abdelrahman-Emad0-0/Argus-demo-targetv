from shop.users import display_name, find_user


def test_find_user_returns_known_user():
    assert find_user(2).name == "omar said"


def test_display_name_is_title_cased():
    assert display_name(1) == "Amira Hassan"
