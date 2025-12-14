def test_smartphone_product_init(Smartphone):
    """Тестируем правильность инициализации объекта"""
    assert Smartphone.name == "Iphone 15"
    assert Smartphone.description == "512GB, Gray space"
    assert Smartphone.price == 210000.0
    assert Smartphone.memory == 512
    assert Smartphone.model == "15"
    assert Smartphone.color == "Gray space"


def test_lamngrass_init(LawnGrass):
    """Тестируем правильность инициализации объекта"""
    assert LawnGrass.name == "Газонная трава"
    assert LawnGrass.description == "Элитная трава для газона"
    assert LawnGrass.price == 500
    assert LawnGrass.germination_period == "7 дней"
    assert LawnGrass.country == "Россия"


def test_smartphone_product_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 241000


def test_lamngrass__add(grass1, grass2):
    assert grass1 + grass2 == 241000
