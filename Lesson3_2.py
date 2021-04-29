
def my_func(**kwargs):
    """создаем словарь именованных аргументов конвертируем их в список по значениям"""
    my_data = kwargs
    return list(my_data.values())


print(my_func(name="Sergey", second_name="Litvinenko", year_of_birth=1983, city="Moscow",
              email="litvinenko12345@yandex.ru", phone_number=89651000000))
