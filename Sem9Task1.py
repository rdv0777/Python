


class NonNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    age = NonNegative()
    price = NonNegative()
    def __init__(self, name, age, price):
        self.name = name
        self.age = age
        self.price = price

    def total_profit(self):
        return self.age * self.price


OBJ = Worker("Апельсин", 20, 100)
print(OBJ.total_profit())
