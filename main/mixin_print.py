class MixinPrint:
    """Класс-миксин для печати в консоль информации в читаемом виде"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})"
