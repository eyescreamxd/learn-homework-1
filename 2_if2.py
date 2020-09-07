"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def compare(str1, str2):
        if type(str1) == str == type(str2):
            if str1 == str2:
                print(1)
            elif str2 == 'learn':
                print(3)
            elif len(str1) > len(str2):
                print(2)
        else:
            print(0)

    compare('asd', 'learn')
    compare('asd', 1)
    compare('asd', 'asd')
    compare('asdasdasd', 'asd')
    compare('asd', 'asdasdasd')

if __name__ == "__main__":
    main()
