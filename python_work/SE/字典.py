a={"color":"green","point":5}
# 键和值之间用冒号分隔， 而键—值对之间用逗号分隔
#字典 是一系列键—值对 。 每个键 都与一个值相关联， 你可以使用键来访问与之相关联的值。 与键相关联的值可以是数字、 字符串、 列表乃至字典
print(a["color"])
print(a["point"])
b=a["point"]

a={"color":"green","point":5}
a["number"] = 0
a["time"]=8
print(a)
del a["point"]
print(a)
for b,c in a.items():
#for 语句的第二部分包含字典名和方法items() ， 它返回一个键—值对列表
    print("\n b:"+str(b))
    print("\n c:"+str(c))

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
#  .key()函数遍历字典里的所有键
    print(name.title())


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
# .values().这条for 语句提取字典中的每个值， 并将它们依次存储到变量language 中
    print(language.title())

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
#通过对包含重复元素的列表调用set() ， 可让Python找出列表中独一无二的元素， 并使用这些元素来创建一个集合
   print(language.title())

for alien_number in range(30):
    print(alien_number)

aliens = []
for alien_number in range(5):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 将字典嵌套到列表里
    print(aliens)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)


