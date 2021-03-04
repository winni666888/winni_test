# message = input("Tell me something, and I will repeat it back to you: ")
# #函数input() 接受一个参数： 即要向用户显示的提示 或说明， 让用户知道该如何做。程序等待用户输入， 并在用户按回车键后继续运行
# print(message)
#
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# #创建多行字符串的方式。 第1行将消息的前半部分存储在变量prompt 中；在第2行中，运算符+= 在存储在prompt 中的字符串末尾附加一个字符串。最终的提示横跨两行，并在问号后面包含一个空格， 这也是出于清晰考虑
# name = input(prompt)
# print("\nHello, " + name + "!")
#
# age=input("how old are you? ")
# age=int(age)
# print(age)
# age>=18

astr = input('Enter a string: ')
for eachar in astr:
    print(eachar)

strlen = len(astr)
i = 0
while i < strlen:
    print(astr[i])
    i += 1


