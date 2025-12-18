from main.mixin_print import MixinPrint
from main.product import Product
from main.baseproduct import BaseProduct

def test_mixin_print(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
