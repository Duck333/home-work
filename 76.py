names = ["Приглошонные :",]
names.append(input("Введите имя : "))
names.append(input("Введите имя : "))
names.append(input("Введите имя : "))
answer = input("Хочешь ли ты пригласить ещё друзей? ")

if answer == ("да") :
    names.append(input("Введите имя друга :"))
    answer = input("Хочешь ли ты пригласить ещё друзей? ")
while answer == ("да") :
 names.append(input("Введите имя друга :"))
 answer = input("Хочешь ли ты пригласить ещё друзей? ")
 if answer == ("нет") :
  break
for item in names :
 print (item)