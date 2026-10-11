"""Stock lookups against the (simulated) supplier API."""

import asyncio

SUPPLIER_TIMEOUT_MS = 2000

# Simulated supplier latency per SKU family, in seconds.
_LATENCY_S = {"FAST": 0.01, "BULK": 0.5}
_STOCK = {"FAST-1": 12, "FAST-2": 0, "BULK-1": 480}


async def _supplier_stock(sku):
    await asyncio.sleep(_LATENCY_S[sku.split("-")[0]])
    return _STOCK[sku]


async def check_stock(sku):
    """Stock level for a SKU. The supplier gets SUPPLIER_TIMEOUT_MS to answer."""
    return await asyncio.wait_for(_supplier_stock(sku), timeout=SUPPLIER_TIMEOUT_MS / 1000)
