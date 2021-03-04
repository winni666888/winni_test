#用户输入一个字符串, 逐个字符显示. 分别实现while版本和for版本.
astr = input('Enter a string: ')
for eachar in astr:
    print(eachar)

strlen = len(astr)
i = 0
while i < strlen:
    print(astr[i])
    i += 1

#使用input从用户输入得到一个字符串, 并显示这个用户输入的内容.
string = input("Please input a sring:")
print(string)

#使用input输入两个数字, 计算两个数字的并显示.
number1 = int(input("Please enter a number:"))
number2 = int(input("Please enter a number:"))
number = number1 + number2
print(number)

#使用while循环输出 0-10
number = 0
while number<=10:
    print(number)
    number+=1
#使用for循环输出 0-10
for i in range (0,11):
    print(i)

#用户输入一个数字, 判定这个数字是正数, 负数, 还是0.

a = int(input("Enter a number:"))
if a > 0:
    print("+")
elif a < 0:
    print("-")
else:
    print(0)
