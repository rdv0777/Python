"""реализовать метакласс. позволяющий создавать всегда один и тот же объект
класса"""

class Dog_Meta(type):
    def __init__(self, *args, **kwargs):
        self.__instance=None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance=super().__call__()
        return self.__instance
class My_Class(metaclass=Dog_Meta):
    pass

obj_1 = My_Class()
obj_2 = My_Class()
obj_3 = My_Class()
obj_4 = My_Class()
print(obj_1 is obj_4)


