from typing import Generator

import pytest
from _pytest.nodes import Item


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item: Item) -> Generator[None, None, None]:
    print(f"\n[RUN] {item.name}")
    yield
    print(f"[DONE] {item.name}")
