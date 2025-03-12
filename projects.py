
menu={
    "coffee":78,
    "burger":89,
    "sandwich":98,
    "salad":84
}

print("welcome to sweet restaurtant")
print("coffee: 78\nburger: 89\nsandwich: 98\nsalad :84")

order_total=0

item_1=input("enter your food order:")
if item_1 in menu:
   order_total += menu[item_1]
   print("your order has been listed:",item_1)
else:
      print("your order has not be listed:",item_1)


another_order=input("do you want another item? (y/n) ")

if another_order== "y":
   item_2 = input("enter your second order:")
   if item_2 in menu:
       order_total += menu[item_2]
   print("your second order has been added:",item_2)
elif another_order=="n":

      print("the total amount of food order is:", order_total)

else:
     print("your order is not placed:",item_2)



next_order=input("else continue for next order or not?(y/n)")

if next_order=="y":
    item_3=input("enter your next order:")
    if item_3 in menu:
        order_total += menu[item_3]

    print("for order has been listed:",item_3)
    print("the total amount is:", order_total)


elif next_order=="n":
    print("the total amount is:",order_total)

else:
    print("order is not given:",item_3)


