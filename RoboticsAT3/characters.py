class Characters():
    def __init__(self):
        pass

    def __str__(self):
        return self.description


class Merchant(Characters):
    def __init__(self):
        self.description = "Merchant"
