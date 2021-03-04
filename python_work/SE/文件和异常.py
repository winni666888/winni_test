with open('pei.txt') as file_object:
    contents = file_object.read()
    print(contents)

filename = 'pei.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

import json
#先导入模块json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
#指定了要将该数字列表存储到其中的文件的名称,通常使用文件扩展名.json来指出文件存储的数据为JSON格式
with open(filename, 'w') as f_obj:
#我们以写入模式打开这个文件， 让json 能够将数据写入其中
    json.dump(numbers, f_obj)
#我们使用函数json.dump() 将数字列表存储到文件numbers.json中

import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)