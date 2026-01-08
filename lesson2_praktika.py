# import math
# def min_boxes(pr):
 #   return math.ceil(pr / 5)
# min = int(input("Количество предметов: "))

# print(f"Минимальное количество коробок: {min_boxes(min)}")


#n = int(input("Введите число: "))

#def check_divisibility(n):

   # for i in range(0, n + 1):
  
       # if(i % 2 == 0) and (i % 4 == 1):
           # print(f"Делится на 2, но не на 4")
      #  elif(i % 2 == 0) and (i % 4 == 0):
           # print(f"Делится и на 2, и на 4")
      #  else:
           # print(i)

#check_divisibility(n)

  # print(f"Делится на 2, но не на 4")

#n = int(input("Введите номер месяца: "))

#def quarter_of_year(n):

 #   if(1 <= n <= 3):
     #   print("1 квартал")
  #  elif(4 <= n <= 6):   
    #    print("2 квартал") 
   # elif(7 <= n <= 9):   
    #    print("3 квартал")
  #  elif(10 <= n <= 12):
  #      print("4 квартал")
   # else: 
     #   print("неверный номер месяца")
         
#quarter_of_year(n)


#lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

#for n in lst:
    #if(n > 15) and (n % 3 ==0):
      #  print(n)



#for i in range(25, 0, -5):
  #  print(i, end=' ')



var_1 = 50
var_2 = 5


temp = var_1
var_1 = var_2  
var_2 = temp
print("var_1:", var_1)  
print("var_2:", var_2)  