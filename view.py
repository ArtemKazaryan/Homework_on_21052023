def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '*'))
            result = func(*args, **kwargs)
            print('=' * 50)
            return result
        return wrapper
    return decorator

class View:
    @add_title('Ожидание пользовательского ввода')
    def wait_user_answer(self):
        print('*' * 50)
        print('Ожидание пользовательского ввода: '.center(50, '='))
        print('Доступные действия:\n'
              '1. Добавить новый рецепт\n'
              '2. Отобразить все рецепты\n'
              '3. Найти рецепт\n'
              '4. Удалить рецепт\n'
              'Выход. Завершить программу')
        print('*' * 50)
        query = input('Введите номер действия: ')
        return query

    def add_new_recept(self):
        dict_recept = {'Название рецепта': None,
                        'Автор рецепта': None,
                        'Тип рецепта (первое, второе блюдо и т.д.)': None,
                        'Текстовое описание рецепта': None,
                        'Ссылка на видео с рецептом': None,
                        'Список ингредиентов': None,
                        'Название кухни (итальянская, французская, украинская и т.д.)': None}
        for key in dict_recept.keys():
            dict_recept[key] = input(f'Введите {key.lower()}: ')
        return dict_recept

    @add_title('Неизвестная ошибка')
    def __throw_an_error__(self, error):
        print('Произошла какая-то ошибка:', error)

    @add_title('Список рецептов')
    def print_recepts(self, recepts):
        if recepts:
            [print(i + 1, recept) for i, recept in enumerate(recepts)]
        else:
            print('Ни одного рецепта нет!')

    @add_title('Поиск рецепта')
    def find_recepts(self):
        criteria = input('Введите список слов для поиска через пробел: ').split()
        return criteria

    @add_title('Дополнительная информация')
    def get_deletion_context(self):
        number = int(input('Введите номер рецепта для удаления: '))
        return number

    @add_title('Результат удаления')
    def return_delete_result(self, result):
        print(result)
        