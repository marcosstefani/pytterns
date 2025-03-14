from pytterns.core.loaders import StrategyLoader

class load:
    @staticmethod
    def strategy(category):
        return StrategyLoader(category)
