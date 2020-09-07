"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list_dics = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '7b', 'scores': [5, 4, 3, 5, 2]},
        {'school_class': '11z', 'scores': [4, 4, 4, 4, 4]},
        {'school_class': '1c', 'scores': [3, 4, 4, 5, 3]}
    ]

    list_scores = []
    for i in list_dics:
        list_scores.append(sum(i['scores']) / len(i['scores']))
    print('Средний балл по всей школе:', sum(list_scores) / len(list_scores))
    for i in list_dics:
        print(f'Средний балл по {i["school_class"]} классу:', sum(i['scores']) / len(i['scores']))


if __name__ == "__main__":
    main()
