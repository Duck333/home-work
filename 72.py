list = ["математика","труд","физика","химия","физра","чзс"]
for item in list :
 print (item)
list.remove(input("Введите предмет который хотите удалить : "))
answer = input("Хочешь ли ты исключить ещё предмет из списка ? : ")
while answer == ("да") :
 list.remove(input("Введите предмет который хотите удалить : "))
 answer = input(" Хочешь ли ты исключить блюда из списка ? : ")
 if answer == ("нет") :
  break
for item in list :
 print (item)