massage="hello python crash course reader"
print(massage)
massage="hallo world"
print(massage)

first_name="ade"
last_name="hello python"
full_name=first_name+" "+last_name
print("hello,"+full_name.title()+"!")
#.title()单词首字母大写

print("lanauges:\n\tc\n\tjavascrip\n\tpython")
# \n换行符 \t制表符

name="tony"
print("hello,"+name+" "+"would you like learn some python today!")

name="tony"
print(name.title())
#首字母大写
print(name.upper())
#全部大写
print(name.lower())
#全部小写
print("Albert Einstein once said, “A person who never made a mistake never tried anything new.”")

name="Albert Einstein"
massage='"A person who never made a mistake never tried anything new'
'''合并/拼接字符串'''
print(name+"once said,"+" " +massage)

name = " tony "
print(name.rstrip())
#删除空格
print(name.lstrip())
print(name.strip())

age=23
massage = "Happy " +str(age)+"sd birthday"
#将非字符串值表示为字符串
print(massage)

bicycles=['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
#在Python中， 第一个列表元素的索引为0， 而不是1。 在大多数编程语言中都是如此， 这与列表操作的底层实现相关。 如果结果出乎意料， 请看看你是否犯了简单的差一错误。
print(bicycles[-1])
#Python为访问最后一个列表元素提供了一种特殊语法。 通过将索引指定为-1 ， 可让Python返回最后一个列表元素：

bicycles=['trck','cannondale','redline','specialized']
massage="my fist bicycle was a "+bicycles[1].title()
print(massage)

names = ['niuchaoping','huwenjie','muwanning']
names.append('songhaihai')
#.append()   为列表末添加元素
names.insert(1,'hushuoshuo')
# insert()   在列表任意位置添加元素，但需要制定索引。假如添加索引为1，即是在索引1前添加
del names[3]
print(names)
print(names[1])
print(names[0].title()+" is a da huai dan")
print(names)
faimly=names.pop(0)
#如果你要从列表中删除一个元素， 且不再以任何方式使用它， 就使用del 语句； 如果你要在删除元素后还能继续使用它， 就使用方法pop()
print(faimly)
print(names)

#根据值删除元素,有时候， 你不知道要从列表中删除的值所处的位置。 如果你只知道要删除的元素的值， 可使用方法remove()
bicycles = ['car','airplane','rocket']
too_expensive = 'rocket'
bicycles.remove(too_expensive)
#  .remove()
print(bicycles)
print(too_expensive)

list=['niu','hu','song','ma']
print(list)
print(list[3]+" is not in xian")
del list[3]
list.append('jiang')
print(list)
print("welcome "+ list[0]+" to my birthday party")
print("I am find a big desk")
list.insert(0,'liu')
list.append('zhang')
print(list)
print("because of dinner table is not arrive on time")
name=list.pop(2)
print("i am sorry for cannot invit "+name+" come my party")

#  使用方法sort() 对列表进行永久性排序
cars = ['bicycle','plane','rocket']
cars.sort()
#  ,sort(),将列表以字母顺序排列,永久排序
print(cars)
cars.sort(reverse=True)
#   与字母顺序相反的顺序排列列表元素， 为此， 只需向sort() 方法传递参数reverse=True
print(cars)
cars.reverse()
#reverse() 不是指按与字母顺序相反的顺序排列列表元素， 而只是反转列表元素的排列顺序：
print(cars)
len (cars)

cars=['bicycle','plane','rocket']
#   for循环把列表里的元素赋值给变量
for car in cars:
    print(car.title()+",That was a greak trick!")


def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,3,20,6,9,2,1]

print (bubbleSort(nums))

for value in range(1,5): #range() 让你能够轻松地生成一系列的数字,函数range() 让Python从你指定的第一个值开始数， 并在到达你指定的第二个值后停止， 因此输出不包含第二个值（这里为5）
    print(value)

squares = [value**2 for value in range(1,11)]
print(squares)

for value in range(1,21):
    print(value)



dimensions = (200, 50)
for dimension in dimensions:
        print(dimension)

digits  =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)

b = [1,8,9,7]
for a in b:
    print(a)
