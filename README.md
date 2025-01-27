# Python
# Итоговое задание №4
### Используя полученные в этом блоке знания вам необходимо написать программу.

Представьте, что Вы работаете Data Engineer и ваша задача — разработать скрипт на Python, который выполняет анализ данных по покупкам в магазине. У вас есть набор данных о покупках, и вам нужно провести различные аналитические операции, чтобы предоставить отчет.

> Есть вот такой вот список покупок.



    purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
    ]
item — название товара,\
category — категория товара,\
price — цена за единицу товара,\
quantity — количество единиц, купленных за один раз.\

Вам нужно реализовать несколько функций для анализа данных:


    total_revenue(purchases): Рассчитайте и верните общую выручку (цена * количество для всех записей).
    items_by_category(purchases): Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
	expensive_purchases(purchases, min_price): Выведите все покупки, где цена товара больше или равна min_price.
	average_price_by_category(purchases): Рассчитайте среднюю цену товаров по каждой категории.
	most_frequent_category(purchases): Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
    
Ваш скрипт должен выводить отчёт по каждому из следующих пунктов:

Общая выручка.\
Список товаров по категориям.\
Список покупок, где цена превышает заданное значение.\
Средняя цена товаров по категориям.\
Категория с наибольшим числом проданных товаров.\
Формат вывода должен соответствовать шаблону вида\

	Общая выручка: 21.0
	Товары по категориям: {'fruit': ['apple', 'banana'], 'dairy': ['milk'], 'bakery': ['bread']}
	Покупки дороже 1.0: [{'item': 'apple', 'category': 'fruit', 'price': 1.2, 'quantity': 10}, {'item': 'milk', 'category': 'dairy', 'price': 1.5, 	'quantity': 2}, {'item': 'bread', 'category': 'bakery', 'price': 2.0, 'quantity': 3}]
	Средняя цена по категориям: {'fruit': 0.85, 'dairy': 1.5, 'bakery': 2.0}
	Категория с наибольшим количеством проданных товаров: fruit