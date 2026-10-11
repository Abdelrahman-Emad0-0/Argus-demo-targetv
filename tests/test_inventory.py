import asyncio

from shop.inventory import check_stock


def test_check_stock_returns_stock_level():
    assert asyncio.run(check_stock("FAST-1")) == 12


def test_check_stock_reports_out_of_stock():
    assert asyncio.run(check_stock("FAST-2")) == 0


def test_check_stock_waits_for_slow_supplier_within_timeout():
    # BULK SKUs answer in 0.5 s, well inside the 2000 ms supplier timeout.
    assert asyncio.run(check_stock("BULK-1")) == 480
