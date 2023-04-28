# Реализовать дескрипторы для любых двух классов

class NonString:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError('Должен быть строковый тип данных!')
        instance.__dict__[self.my_attr] = value


class Worker:
    name = NonString('name')  # дескрипторы
    surname = NonString('surname')  # дескрипторы
    position = NonString('position')  # дескрипторы

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}, Должность: {self.position}'


worker = Worker('Natallia', 'Khadakouskaya', 'student', 100000, 50000)

print(worker.get_full_name())

worker.name = 10000
worker.surname = 10
worker.position = 1

'''worker.name = '10000'
worker.surname = '10'
worker.position = '1'''''

# print(worker.__dict__)
print(worker.get_full_name())