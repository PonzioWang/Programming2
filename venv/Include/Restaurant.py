"""python类的第一个练习题
2019.5.14
"""

class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name)

wang_restaurant = Restaurant("wan",10)
wang_restaurant.describe_restaurant()
wang_restaurant.open_restaurant()




