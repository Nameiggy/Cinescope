
from warcraft_store import GoblinShop

shop = GoblinShop()
print(shop)

# Показываем товары
print(shop.show_items())

# Покупаем товар
print(shop.buy_item("Зелье маны"))
print(shop.buy_item("Артефакт магии"))
