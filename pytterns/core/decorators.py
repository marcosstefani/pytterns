STRATEGIES = {}

def strategy(grouper):
    def decorator(cls):
        if grouper not in STRATEGIES:
            STRATEGIES[grouper] = []
        STRATEGIES[grouper].append(cls())
        return cls
    return decorator
