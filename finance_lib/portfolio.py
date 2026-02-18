class Portfolio:
    def __init__(self):
        self.actions = []

    def add_asset(self, action):
        self.actions.append(action)

    def get_total_value(self):
        total = sum(action.total_value for action in self.actions)
        return round(total, 2)

    def __add__(self, action):
        self.actions.append(action)
        return self

    def __len__(self):
        return len(self.actions)

    def __iter__(self):
        return iter(self.actions)
