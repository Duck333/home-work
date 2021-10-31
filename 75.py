numbers = ["415","615","666","696"]
numbersid = {"415" : "1" , "615" : "2","666" : "3" , "696" : "4"}
for item in numbers :
 print (item)
id = input("Введите число : ")
if  id != "415" or "615" or "666" or "696" :
 print("That is not in the")
if id == "415" or "615" or "666" or "696" :
 print(numbersid[id])
