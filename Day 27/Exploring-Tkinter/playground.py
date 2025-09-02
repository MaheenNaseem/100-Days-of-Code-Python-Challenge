def add(*args):
    result = 0
    for num in args:
        result += num
    return result

# print(add(5,6,8 ))

def calculate (n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(kwargs)
    # print(n)
    # print(type(kwargs))

calculate(2, add = 2, multiply = 2)

# Creating our own class and providing it kwargs (Many keyword arguments)

class Car:
    def __init__(self,**kw):
        self.model = kw.get("model")
        self.make = kw.get("make")

car = Car(model = "MK4")
print(car.model)
