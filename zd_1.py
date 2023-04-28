# Реализовать дескрипторы для любых двух классов

class NonNegative:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным!")
        instance.__dict__[self.my_attr] = value


class Worker:
    wage = NonNegative('wage')  # дескрипторы
    bonus_percent = NonNegative('bonus_percent')  # дескрипторы

    def __init__(self, name, surname, position, wage, bonus_percent):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus_percent = bonus_percent

    def get_total_income(self):
        return self.wage * self.bonus_percent


worker = Worker('Natallia', 'Khadakouskaya', 'student', 10000, 5)

print(worker.get_total_income())

worker.wage = 10000
worker.bonus_percent = 10
# print(worker.__dict__)
print(worker.get_total_income())