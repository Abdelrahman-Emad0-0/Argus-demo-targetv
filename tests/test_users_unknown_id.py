from shop.users import display_name


def test_display_name_of_an_unknown_id_does_not_raise():
    assert display_name(999) == "user 999"
