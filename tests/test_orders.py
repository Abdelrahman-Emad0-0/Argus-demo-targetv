from shop.orders import connect, list_orders


def test_list_orders_returns_all_orders():
    orders = list_orders(connect())
    assert [row[0] for row in orders] == [1001, 1002, 1003]
