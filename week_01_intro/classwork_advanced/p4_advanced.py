"""
Презентация 4 — повышенный уровень.
Задачи уровня 3 (3.1–3.3, работа со строками и форматирование)
и уровня 4 (decimal и fractions).

Решения писать здесь. Тесты — в конце файла.
"""

# ============================================================
# Задача 3.1. Безопасный ввод числа
# ============================================================
# Условие:
#   Запросите у пользователя число. Если введено не число,
#   выведите сообщение об ошибке.
#   Используйте методы строк и преобразование типов.
#
# Пример:
#   In: 42
#   Out: OK: 42
#
#   In: abc
#   Out: Not a number
#
# Подсказка:
#   s = input()
#   if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
#       n = int(s)
#       print(f"OK: {n}")
#   else:
#       print("Not a number")

def safe_input(s: str) -> str:

    s = input('Введите число: ')

    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        n = int(s)
        print(f"OK: {n}")
    else:
        print("Not a number")
  

# ============================================================
# Задача 3.2. Разбор строки
# ============================================================
# Условие:
#   Запросите строку вида "имя:возраст". Разделите её по символу :
#   и выведите приветствие с возрастом, увеличенным на 1.
#
# Пример:
#   In: Ivan:24
#   Out: Hello, Ivan! Next year you are 25.
#
# Подсказка:
#   Используйте split(":") и int().

def parse_name_age(s: str) -> str:

    s = input("Введите строку вида 'имя:возраст'").split(":")
    age = int(s[1])
    name = s[0]

    print(f"Hello, {name}! Next year you are {age}")


# ============================================================
# Задача 3.3. Форматирование счёта
# ============================================================
# Условие:
#   Запросите название товара, цену за единицу и количество.
#   Выведите чек с выравниванием по правому краю и итоговой суммой.
#
# Пример:
#   In: apple
#   In: 15.5
#   In: 3
#   Out:
#     Product: apple
#     Cost: 15.50
#     Amount: 3
#     - - - - - - - - - - - - - - - - - - - -
#     Overall: 46.50
#
# Подсказка: f"value:>10.2f"

def format_receipt(product: str, cost: float, amount: int) -> str:

    product = input('Введите название товара: ')
    cost = float(input('Введите цену за единицу товара: '))
    amount = int(input('Введите количество товара: '))
    
    print(f"Product: {product}")
    print(f"Cost: {cost:>10.2f}")
    print(f"Amount: {amount}")
    print("-" * 43)
    print(f"Overall: {cost * amount:>10.2f}")


# ============================================================
# Задача 4.1. Точный расчёт стоимости (Decimal)
# ============================================================
# Условие:
#   Запросите цену товара (строка, например "19.99"), количество
#   и налоговую ставку в процентах. Вычислите итоговую стоимость
#   с помощью Decimal, округлив до двух знаков по ROUND_HALF_UP.
#
# Пример:
#   In: 19.99
#   In: 3
#   In: 13
#   Out: Overall: 67.77
#
# Подсказка:
#   Decimal('19.99') * 3 * (1 + Decimal('0.13'))
#   .quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

from decimal import Decimal, ROUND_HALF_UP

def exact_total(price: str, quantity: int, tax_percent: str) -> str:
   
   price = Decimal(input("Введите цену товара:"))
   quantity = int(input("Введите количество товара:"))
   tax_percent = Decimal(input("Введите налоговую ставку:"))
   
   total = price * quantity * (1 + tax_percent / 100)
   print("Overall:", total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

# ============================================================
# Задача 4.2. Сравнение float и Decimal
# ============================================================
# Условие:
#   Сложите 0.1 + 0.2 двумя способами: через float и через Decimal.
#   Выведите оба результата и проверьте, равны ли они 0.3.
#
# Пример:
#   float: 0.30000000000000004 -> False
#   Decimal: 0.3 -> True

from decimal import Decimal

def compare_float_decimal() -> tuple:
    f_format = 0.1 + 0.2
    d_format = Decimal('0.1') + Decimal('0.2')

    print(f"float: {f_format} -> {f_format == 0.3}")
    print(f"Decimal: {d_format} -> {d_format == Decimal('0.3')}")

    


# ============================================================
# Задача 4.3. Сумма дробей (Fraction)
# ============================================================
# Условие:
#   Запросите две обыкновенные дроби в формате "числитель/знаменатель".
#   Сложите их с помощью Fraction и выведите результат в виде
#   несократимой дроби.
#
# Пример:
#   In: 1/3
#   In: 1/6
#   Out: 1/2

from fractions import Fraction

def sum_fractions(frac1: str, frac2: str) -> str:
    frac1 = Fraction(input('Введите первую дробь "числитель/знаменатель": '))
    frac2 = Fraction(input('Введите вторую дробь "числитель/знаменатель": ')) 
    
    result = frac1+frac2
    print(result)

# ============================================================
# Задача 4.4. Точное деление счёта
# ============================================================
# Условие:
#   Счёт в ресторане составил 1234.56 руб. Его нужно разделить
#   на 7 человек поровну. Вычислите долю каждого с помощью Decimal
#   и округлите до копеек. Проверьте, что сумма долей не превышает
#   исходный счёт.
#
# Пример:
#   Account: 1234.56
#   Guests: 7
#   Share: 176.37
#   Sum: 1234.59 (over 0.03)
#
# Вопрос: как распределить «лишние» копейки, чтобы сумма долей
#   точно совпала со счётом?

from decimal import Decimal, ROUND_HALF_UP

def split_bill(account: str, guests: int) -> dict:
    total = Decimal(account)
    share = Decimal (total / guests).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    overall = share * guests
    diff = overall - total
    print (f"Sum: {overall} (over {diff})")


# ============================================================
# Тесты (assert)
# ============================================================

if __name__ == "__main__":
    # 3.1
    assert safe_input("42") == "OK: 42"
    assert safe_input("-7") == "OK: -7"
    assert safe_input("abc") == "Not a number"
    assert safe_input("3.14") == "Not a number"

    # 3.2
    assert parse_name_age("Ivan:24") == "Hello, Ivan! Next year you are 25."
    assert parse_name_age("Anna:30") == "Hello, Anna! Next year you are 31."

    # 3.3
    receipt = format_receipt("apple", 15.5, 3)
    assert "apple" in receipt
    assert "15.50" in receipt
    assert "46.50" in receipt

    # 4.1
    assert exact_total("19.99", 3, "13") == "67.77"

    # 4.2
    fs, feq, ds, deq = compare_float_decimal()
    assert feq is False
    assert deq is True

    # 4.3
    assert sum_fractions("1/3", "1/6") == "1/2"
    assert sum_fractions("1/2", "1/2") == "1"

    # 4.4
    res = split_bill("1234.56", 7)
    assert res["share"] == res["share"].quantize(res["share"])
    assert res["total"] >= res["over"]

    print("p4_advanced: все тесты пройдены")
