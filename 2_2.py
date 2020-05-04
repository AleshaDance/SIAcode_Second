# (Задача) О неограниченном рюкзаке, каждый предмет может быть взят любое количество раз
wLimit = int(input("Max weight: "))     # максимальный вес в рюкзаке
n = int(input("Number of items: "))    # количество предметов
print('======<<==>>======')

items = dict()      # создаем словарь
for _ in range(n):
    w, v = input("Weight_Value: ").split('_')   # ключ - масса, значение - ценность
    items[int(w)] = int(v)      # добавление в словарь записи
# НАХОЖДЕНИЕ НАИБОЛЬШЕЙ ЦЕННОСТИ РЮКЗАКА
d = [0]*(wLimit + 1)
for x in items:
    for i in range(x, wLimit + 1):
        d[i] = max(d[i], d[i-x] + items[x])

print('======<<==>>======')
print("Max value - {}".format(d[wLimit]))
