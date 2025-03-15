import pytest
from pytterns.patterns import load
from pytterns.core.decorators import strategy

@strategy("group_2")
class StrategyX:
    def check(self, value):
        return value == "X"
    def run(self):
        return "StrategyX"

def test_load_strategy():
    strategy_instance = load.strategy("group_2").check("X")
    assert strategy_instance.__class__.__name__ == "StrategyX"

def test_load_strategy_not_found():
    with pytest.raises(ValueError, match="No strategy in 'group_2' passed the 'check' filter"):
        load.strategy("group_2").check("Y").run()
