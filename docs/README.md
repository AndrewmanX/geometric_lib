
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Документация проекта

## Общее описание решения

Этот проект предназначен для вычисления площади и периметра геометрических фигур: квадрата и круга. Он предоставляет простые функции, которые можно использовать для получения необходимых значений, используя переданные параметры.

## Функции

### Квадрат

#### Площадь квадрата ‘area(a)’

Вычисляет площадь квадрата.

##### Параметры:
- `a` (число): длина стороны квадрата.

##### Возвращает:
- Площадь квадрата.

##### Пример вызова:
*python*
area_p = area(4)
print(area_p)  # Вывод: 16

##### Периметр квадрата `perimeter(a)`

Вычисляет периметр квадрата.

##### Параметры:
- `а` (число): длина стороны квадрата.

##### Возвращает:
- Периметр квадрата.

##### Пример вызова:
*python*
perimeter_p= perimeter(5)
print(perimeter_p)  # Вывод: 20

### Круг

#### Площадь круга `area(r)`

Вычисляет площадь круга.

##### Параметры:
- `r` (число): радиус круга.

##### Возвращает:
- Площадь круга.

##### Пример вызова:
*python*
area_p = area(3)
print(area_p)  # Вывод: 28.27 (примерный результат при PI = 3.14)

#### Периметр круга `perimeter(r)`

Вычисляет периметр (длину окружности) круга.

##### Параметры:
- `r` (число): радиус круга.

##### Возвращает:
- Периметр круга.

##### Пример вызова:
*python*
perimeter_p = perimeter(3)
print(perimeter_p)  # Вывод: 18.84 (примерный результат при PI = 3.14)

## История изменений проекта

### Коммиты

- **d078c8d** - docs added
- **8ba9aeb** - Circle and square added
