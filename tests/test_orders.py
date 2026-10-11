from shop.orders import connect, list_orders


def test_list_orders_returns_all_orders():
    orders = list_orders(connect())
    assert [row[0] for row in orders] == [1001, 1002, 1003]


def test_list_orders_filters_by_status():
    orders = list_orders(connect(), status="paid")
    assert [row[0] for row in orders] == [1001, 1002]
    assert all(row[3] == "paid" for row in orders)
