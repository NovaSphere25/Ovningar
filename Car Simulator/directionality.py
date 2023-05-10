class directionality:
    def __init__(self, name):
        self.name = name
        self._opposites = set()

    def __invert__(self):
        return self.opposite

    @property
    def opposite(self):
        return list(self._opposites)

    @opposite.setter
    def opposite(self, value):
        if not isinstance(value, list):
            value = [value]

        self._opposites |= set(value)
        for val in value:
            val._opposites.add(self)

    def __repr__(self):
        return self.name