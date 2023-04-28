# Реализовать метакласс, позволяющий создавать всегда один и тот же
# объект класса


class TypedMeta(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            return self.__instance
        return self.__instance


class MyClass(TypedMeta, metaclass=TypedMeta):
    pass


obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)