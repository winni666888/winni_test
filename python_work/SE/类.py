# class Dog():
# #一次模拟小狗的简单尝试
#     def __init__(self, name, age):
# #初始化属性name和age
#         self.name = name
#         self.age = age
#     def sit(self):
# #模拟小狗被命令时蹲下
#         print(self.name.title() + " is now sitting.")
#     def roll_over(self):
# #模拟小狗被命令时打滚
#         print(self.name.title() + " rolled over!")
#
# class Dog():
#      my_dog = Dog('willie', 6)
#      print("My dog's name is " + my_dog.name.title() + ".")
#      print("My dog is " + str(my_dog.age) + " years old.")
#
#
# class Dog():
#      my_dog = Dog('willie', 6)
#      your_dog = Dog('lucy', 3)
#      print("My dog's name is " + my_dog.name.title() + ".")
#      print("My dog is " + str(my_dog.age) + " years old.")
#      my_dog.sit()
#      print("\nYour dog's name is " + your_dog.name.title() + ".")
#      print("Your dog is " + str(your_dog.age) + " years old.")
#      your_dog.sit()

# class Dog(object):
# #object： dog类继承object类
#     def __init__(self,name,age,color):
# #给dog类定义了name.color,age三个属性
#         self.name = name
#         self.age = age
#         self.color = color
#     def eat(self):
#         print(self.name,"啃骨头")
#     def run(self):
#         print(self.name,"飞快跑")
# #实例化对象
# dog = Dog("小黑",3,"白色")
# #隐式传递了self，实际上将dog传递给了self
# print(dog.name)

# class Card(object):
#     def __init__(self,num,pwd,ban):
#         self.num = num
#         self.pwd = pwd
#         self.ban = ban
#     def cun(self):
#         print("存款")
# card = Card("1000","123456",1000)
# print(card.ban)

