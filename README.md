# Задачи KTS Metaclass: Python

- [x] `flip_kv_vk`
- [x] `flip_kv_vk_safe`
- [x] `even_odd`
- [x] `find_shortest_longest_word`
- [x] `corresponding_pairs`
- [x] `is_prime`
- [x] `seconds_to_str`
- [x] `cartesian_product`
- [x] `dfs`
- [x] `bfs`


## 1. Переворачивание словаря

`flip_kv_vk`

Функция должна возвращать словарь, в котором в качестве ключей — значения
исходного словаря, а в качестве значений — ключи.

**Пример:**
```python
flip_kv_vk({
    'tokyo': 'Токио',
    'moscow': 'Москва',
}) == {
    'Токио': 'tokyo',
    'Москва': 'moscow',
}
```

## 2. Безопасное переворачивание словаря

`flip_kv_vk_safe`

Функция выше имеет недостаток, что если в изначальном массиве присутствовали одинаковые
значения, то сохранится лишь один ключ. В данном задании предлагается реализовать
функцию, возвращающую словарь, в котором в качестве ключей — значения
переданного словаря, а в качестве значений — массив ключей конфликтующих
значений.

**Пример:**
```python
flip_kv_vk({
    'Санкт-Петербург': '+3',
    'Москва': '+3',
}) == {
    '+3': ['Москва', 'Санкт-Петербург'],
}
```

## 3. Вычисление отношения сумм в массиве

`even_odd`

Функция на вход принимает массив чисел и должна вернуть отношение суммы
четных элементов массива к сумме нечетных.

**Пример:**
```python
even_odd([1, 2, 3, 4, 5]) == 0.8889
```

## 4. Поиск самого короткого и длинного слова в тексте

`find_shortest_longest_word`

Функция должна в переданном тексте найти и вернуть `tuple`, содержащий слово,
имеющее наименьшую длину и слово, имеющее наибольшую длину в данном тексте.
Если какого-то слова нет — вернуть None в соответствующей компоненте кортежа.

**Пример:**
```python
find_shortest_longest_word(
    'hello there, general kenobi'
) == ('hello', 'general')
```

## 5. Пары

`corresponding_pairs`

Задача заключается в написании функции, которая принимает 2 массива и возвращает
новый массив, содержащий соответствующие элементы исходных.

**Пример:**
```python
corresponding_pairs([1, 2], ['A', 'B']) == [(1, 'A'), (2, 'B')]
```


## 6. Простое число

`is_prime`

Необходимо реализовать функцию, возвращающую True, если переданное число
является простым, иначе - False.

**Пример:**
```python
is_prime(17) == True
```

## 7. Строковое представление времени

`seconds_to_str`

Функция должна вернуть текстовое представление времени.

**Пример:**
```python
seconds_to_str(20) == '20s'
seconds_to_str(60) == '01m00s'
seconds_to_str(65) == '01m05s'
seconds_to_str(3700) == '01h01m40s'
seconds_to_str(93600) == '01d02h00m00s'
```

## 8. Декартово произведение

`cartesian_product`

Необходимо реализовать функцию, возвращающую всевозможные пары значений двух
переданных массивов.

**Пример:**
```python
cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
```

## 9 и 10. Обход графа в глубину и в ширину

Дана сущность произвольного графа (`Graph`). Необходимо реализовать функцию
поиска элементов в глубину (`dfs`) и функцию поиска в ширину (`bfs`). Они должны
вернуть все узлы графа в порядке их просмотра ("посещения").
Подробнее про обходы в глубину и ширину:

* https://ru.wikipedia.org/wiki/Поиск_в_глубину
* https://ru.wikipedia.org/wiki/Поиск_в_ширину

**Пример:**

### `dfs`
```python
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(d)
a.point_to(c)
g = Graph(a)

assert g.dfs() == [a, b, d, c]
```

### `bfs`
```python
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(d)
a.point_to(c)
g = Graph(a)

assert g.bfs() == [a, b, c, d]
```
