# def add(*nums):
#     a = 0
#     for n in nums:
#         a += n
#
#     return a
#
# print(add(1,2,3,4,5,6,7,8,9))


class Car:
    def __init__(self, **kw):
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.color = kw.get("color")




my_truck = Car(make="GMC", model="Sierra Denali")
print(my_truck.make, my_truck.model)
