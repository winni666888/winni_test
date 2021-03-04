age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

requested_toppings = []
if requested_toppings:
    #在if 语句中将列表名用在条件表达式中时， Python将在列表至少包含一个元素时返回True ， 并在列表为空时返回False
    for requested_topping in requested_toppings:
     print("Adding " + requested_topping + ".")
     print("\nFinished making your pizza!")
else:
     print("Are you sure you want a plain pizza?")