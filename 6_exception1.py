"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
user_dict = {'How r u?': 'I\'m fine, thx', 'Whatcha doing?': 'Nothing'}


def ask_user():
    """
    Замените pass на ваш код
    """
    try:
        q = input("Your question:")
        while q in user_dict:
            print(user_dict[q])
            q = input("Another question:")
    except KeyboardInterrupt:
        print("\nПока!")


if __name__ == "__main__":
    ask_user()
