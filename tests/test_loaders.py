import pytest
from pytterns.core.loaders import StrategyLoader
from pytterns.core.decorators import strategy, STRATEGIES

@strategy("group_1")
class StrategyA:
    def check(self, value):
        return value == "A"

@strategy("group_1")
class StrategyB:
    def check(self, value):
        return value == "B"

def test_strategy_loader_found():
    loader = StrategyLoader("group_1")
    assert loader.check("A").__class__.__name__ == "StrategyA"
    assert loader.check("B").__class__.__name__ == "StrategyB"

def test_strategy_loader_not_found():
    loader = StrategyLoader("group_1")
    with pytest.raises(ValueError, match="No strategy in 'group_1' passed the 'check' filter"):
        loader.check("C")
