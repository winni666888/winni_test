def display_message():
    print("hallo")
display_message()

def favorite_book(tittle):
    print("my favorite book is "+ tittle.title())
favorite_book("history")

def describe_pet(animal_type,pet_name):
    print("my "+animal_type +" is " + pet_name.title())
#位置实参
describe_pet("animal","cat")

def describe_pet(animal_type, pet_name):
#显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
a=get_formatted_name('jimi', 'hendrix')
print(a)

# def build_person(first_name, last_name):
#     """返回一个字典， 其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=''):
# #返回一个字典， 其中包含有关一个人的信息
#     person = {"first": first_name, "last": last_name}
#     if age:
#          person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

#
# def get_formatted_name(first_name, last_name):
# #返回整洁的姓名
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# # 这是一个无限循环!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# def get_formatted_name(first_name, last_name):
# #返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

def contriy(city,country):
    print(city + ',' + country)
contriy("beijing","zhongguo")


def greet_users(names):
#   向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah','ty', 'margot']
greet_users(usernames)


def print_models(unprinted_designs, completed_models):
#模拟打印每个设计， 直到没有未打印的设计为止
#打印每个设计后， 都将其移到列表completed_models中
    while unprinted_designs:
        current_design = unprinted_designs.pop()
# 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
#  显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def make_pizza(*toppings):
# 形参名*toppings 中的星号让Python创建一个名为toppings 的空元组， 并将收到的所有值都封装到这个元组中
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')




# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):


# def log(aa,*bb):
#     pirnt(aa+"/t".join(bb))
# log(aa="88",99,42,554,84)

# a = "jihhoihuggjie"
# print(a.sort(reverse=True))




# def add(a,b,c,d):
#     e=a+b+c+d
#     return e  #返回出执行结果
# result=add(23,56,89,36) #将方法执行后的结果赋给变量
# print("本次相加的结果为：",result)
# print("本次相加的结果为：",add(54,25,36,65))

# def zzj(f):
#     print("正在榨汁")
#     print("两分钟后...")
#     zhi = "一杯"+f+"汁"
#     return zhi
# guozhi=zzj("苹果")
# print(guozhi)


# def show(name,age,sex,hobby):
#     print("我叫：",name,"年龄:",age,"性别：",sex,"爱好：",hobby)
# show("winni",18,"男","拍照")

def add(*args):   #不定长参数
    sum=0
    for i in args:
        sum=sum+i
    return sum
d=add(3,45,7)
print(d)

#模块
import random
a=random.random()
print(a)

