import asyncio

from shop.inventory import check_stock


def test_check_stock_returns_stock_level():
    assert asyncio.run(check_stock("FAST-1")) == 12


def test_check_stock_reports_out_of_stock():
    assert asyncio.run(check_stock("FAST-2")) == 0
