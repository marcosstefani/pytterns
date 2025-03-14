import pytest
from pytterns.core.decorators import strategy, STRATEGIES

def test_strategy_decorator():
    @strategy("test_group")
    class TestStrategy:
        def check(self, value):
            return value == "test"

    assert "test_group" in STRATEGIES
    assert len(STRATEGIES["test_group"]) == 1
    assert STRATEGIES["test_group"][0].check("test") is True
