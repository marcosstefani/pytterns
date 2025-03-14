from pytterns.core.decorators import STRATEGIES
class StrategyLoader:
    def __init__(self, name):
        self.name = name
        if name not in STRATEGIES:
            raise ValueError(f"No strategy found for strategy: {name}")

    def __getattr__(self, filter_method):
        """Allows you to call any method as a filter"""
        def filter_strategy(*args, **kwargs):
            for strategy in STRATEGIES[self.name]:
                method = getattr(strategy, filter_method, None)
                if callable(method) and method(*args, **kwargs):
                    return strategy
            raise ValueError(f"No strategy in '{self.name}' passed the '{filter_method}' filter")
        return filter_strategy
