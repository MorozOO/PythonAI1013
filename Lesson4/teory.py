# class Parent:
#     pass
#
# class Child(Parent):
#     pass

# class Human:
#     height = 170
#
# class Student(Human):
#     salary = 0
#
# class Worker(Human):
#     salary = 100
#
# nick = Student()
# ann = Worker()
# print(nick.height)
# print(ann.height)
#
# print(nick.salary)
# print(ann.salary)

# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
#
# class Parent(Grandparent):
#     age = 40
#
# class Child(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
# nick = Child()
#
#


# class Hello:
#     def __init__(self):
#         print("Hello")
# class HelloWorld(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World")
# one = HelloWorld()

class Grandparent:
    def about(self):
        print("I am GrandParent")

    def about_myself(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")

class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

kate = Child()
























