import pytest
from pytterns import strategy, load

@strategy("integration_test")
class IntegrationStrategy:
    def check(self, value):
        return value == "ok"

def test_full_integration():
    strategy_instance = load.strategy("integration_test").check("ok")
    assert strategy_instance.__class__.__name__ == "IntegrationStrategy"
