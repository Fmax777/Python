import json


def load_purchases():
    try:
        with open('purchases.txt', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Файл не найден")
        return None
    except json.JSONDecodeError:
        print('Ошибка при разборе JSON данных')
        return None


purchases = load_purchases()


def total_revenue(purchases):
    total = 0
    if purchases:
        for purchase in purchases:
            total_price = purchase['price'] * purchase['quantity']
            total += total_price
    return total


if purchases:
    tr = total_revenue(purchases)
else:
    print('Загрузка данных не выполнена')


def items_by_category(purchases):
    categories = {}
    if purchases:
        for purchase in purchases:
            category = purchase['category']
            item = purchase['item']
            if category not in categories:
                categories[category] = [item]
            else:
                if item not in categories[category]:
                    categories[category].append(item)
    return categories

def expensive_purchases(purchases, min_price):
    expensive_items = []
    if purchases:
        for purchase in purchases:
            if purchase['price'] >= min_price:
                expensive_items.append(purchase)
    return expensive_items


def average_price_by_category(purchases):
    category_data = {}
    if purchases:
        for purchase in purchases:
            category = purchase['category']
            price = purchase['price']
            quantity = purchase['quantity']
            if category in category_data:
                category_data[category]["total_price"] += price * quantity
                category_data[category]["count"] += quantity
            else:
                category_data[category] = {"total_price": price * quantity, "count": quantity}
    average_price = {}
    for category, data in category_data.items():
        average_price[category] = round(data["total_price"] / data["count"], 2)
    return average_price

def most_frequent_category(purchases):
    category_counts = {}
    if purchases:
        for purchase in purchases:
            category = purchase['category']
            quantity = purchase['quantity']
            if category in category_counts:
                category_counts[category] += quantity
            else:
                category_counts[category] = quantity
    max_quantity = 0
    most_frequent = None
    for category, quantity in category_counts.items():
        if quantity > max_quantity:
            max_quantity = quantity
            most_frequent = category
    return most_frequent



if purchases:
    print(f'Общая выручка: {total_revenue(purchases)}')
    print(f'Товары по категориям: {items_by_category(purchases)}')
    min_price = 1.0 # определяем min_price
    print(f'Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}') # передаём min_price в функцию
    print(f'Средняя цена по категориям: {average_price_by_category(purchases)}')
    print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}')
else:
    print('Загрузка данных не выполнена')