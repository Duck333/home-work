list = ["Ваш список блюд : ",]
list.append(input("Введите название блюда : "))
list.append(input("Введите название блюда : "))
list.append(input("Введите название блюда : "))
list.append(input("Введите название блюда : "))
for item in list :
 print (item)
answer = input("Хочешь ли ты исключить блюда из списка ? : ")
if answer == ("да") :
 list.remove(input("Введите блюдо которое желаете удалить : :"))
while answer == ("да") :
 answer = input(" Хочешь ли ты исключить блюда из списка ? : ")
 list.remove(input("Введите блюдо которое желаете удалить : :"))
 if answer == ("нет") :
  break
for item in list :
 print (item)