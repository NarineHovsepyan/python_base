# dictt = {
#     1 : 'AEILNORSTU',
#     2 : 'DG',
#     3 : 'BCMP',
#     4 : 'FHVWY',
#     5 : 'K',
#     8 : 'JX',
#    10 : 'QZ'
# }
# text = input('Enter text: ').upper()
# count = 0
# for i in text:
#     for j in dictt:
#         if i in dictt[j]:
#             count += j
# print(count)

#----------------------------------

# rom = {
#     'I' : 1,
#     'V' : 5,
#     'X' : 10,
#     'L' : 50,
#     'C' : 100,
#     'D' : 500,
#     'M' : 1000
#       }
# text = input('Enter numbers = ')
# count=0
# s = 0

# mydict = {'a': 1, 'b':2, 'c': 12 }
# summ = 1
# for ll in mydict:
#     summ*=mydict[ll]
# print(summ)

# bar = {'D': 56,'E':12, 'F':69, 'C':45, 'B':23, 'A':67}
# keys = sorted(bar, key=bar.get, reverse=True) [:3]
# ll = {}
# for i in keys:
#     ll[i] = bar[i]
# print(ll)
# nuyny mi tuxov
# bar = {'D': 56,'E':12, 'F':69, 'C':45, 'B':23, 'A':67}
# print({i:bar[i] for i in sorted(bar, key=bar.get, reverse=True)[:3]})

# students  = {
#     'Armen':7,
#     'Davit':4,
#     'Anna':12,
#     'Vardan':5,
#     'Gor':12
#             }
# sum = 0
# for kk in students:
#     sum+=students[kk]
# men = round(sum/len(students), 2)
# lav = {}
# vat = {}
# for i in students:
#     if students[i] < men:
#         lav[i] = students[i]
#     else:
#         vat[i] = students[i]
# print(lav)
# print (vat)


# dict_ = {
#     1 :'AEILNORSTU',
#     2 :'DG',
#     3 :'BCMP',
#     4 :'FHVWY',
#     5 :'K',
#     8 :'JX',
#     10:'QZ',
#          }
# list = []
# text = input("Enter text :").upper()
# for i in text:
#     for l in dict_:
#         if i in dict_[l]:
#             print(l* (dict_[l].index(i)+1), end ='')

# dict_ = {
#     1 :'AEILNORSTU',
#     2 :'DG',
#     3 :'BCMP',
#     4 :'FHVWY',
#     5 :'K',
#     8 :'JX',
#     10:'QZ',
#          }

# sum = 0
# text = input(' Enter text: ').upper()
# for i in text:
#     for j in dict_:
#         if i in dict_[j]:
#             sum += j
# print(sum)

# name = {
#     'NARINE':32,
#     'Davit':32,
#     'NAIRA':28,
#     'Marine':54,
#     'EDVARD':66,
#     'GOR':31
#         }
# anun = input(' Enter your name:').upper()
# for j in name:
#     if anun in j:
#         print(name[j])
#     print(' Anuny cucakum chka :D')
#     break

# word = ' exercises'
# dd = {}
# for i in word:
#     dd

# dd = {'a':2, 'b':2, 'c':3}
# newdd = {}
# list = []
# for i in dd:
#     if dd[i] in dd:
#         list.append[i]
#         newdd[dd[i]]= list
# print(newdd)



# def summ(s):
#     return 10.95 + ((s-1)*2.95)
# print("$", summ(170))
    
# def tiv(k):
#     for i in range(2,k):
#         if k%i == 0:
#            return False
#     else:
#           return True        
# print

# def calendar(year, month, day):
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     return sum(day_list[:month - 1]) + day
# print(calendar(2024, 3, 15))

# def calendar(year, x):
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#      for i in range(len(day_list)):
#          mouth = x //day_list[i] +1
#          return mouth,  x - sum(day_list[:mouth - 1]) 
# print(calendar(2024, 59))




# import random
# def number():
#     letter = 'MNBVCXZLKJHGFDSAPOIUYTREWQ'
#     return f'{random.randint(0,9)}{random.randint(0,9)} {random.choice(letter)}{random.choice(letter)} {random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
# print(number())

# def calendar(year, mount, day):
#     month_list = {
#  1:'hunvar', 
#  2:'petrvar',
#  3:'mart',
#  4:'april',
#  5:'mayis',
#  6:'hunis',
#  7:'hulis',
#  8:'ogostos',
#  9:'september',
# 10:'hoktember',
# 11:'noyember',
# 12:'dektember'
# }
# mount == month_list.keys
# if month_list.keys[mount] + year%100 == day:
#     return True
# print(calendar(2024, 'hunvar', 28))


# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x-1)
# print(fact(5))



# def encoding(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + encoding(mylist[2:])
# print(encoding(['A', 12, 'B', 4,'A', 6, 'B', 1]))

# def encoding(mylist, count = 1):
#    if len(mylist) == mylist.count(mylist[0]):
#       return [mylist[0], len(mylist)]
#    if mylist[0] == mylist[1]:
#       return encoding(mylist[1:], count + 1)
#    else:
#       return [mylist[0], count] + encoding(mylist[1:], count= 1)
# print(encoding(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B']))



# def primelist(mylist):
#    pass
# print(primelist([1,[2,3], [4,[5,[6,7]]], [[[8], 9], [10]]]))


# def number():
#     x = input('Enter number')
#     if x =='':
#         return 0
#     else: 
#         return float(x) + number()
# print(number())

# def Evklid(a,b):
#     if  b == 0:
#         return a
#     elif a>b:
#         return Evklid(b, a%b )
#     else:
#         return Evklid(a, b%a)
# a = int(input(' Enter a = '))
# b = int(input(' Enter b = '))
# c = Evklid(a,b)
# print(f"Наибольший общий делитель чисел {a} и {b} равен {c}")

# nato_alphabet = {
#     'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
#     'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
#     'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
#     'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whisky', 'X': 'X-ray',
#     'Y': 'Yankee', 'Z': 'Zulu'
#                 }



# def factorial(x):
#     if x == 1:
#         return 1
#     else: 
#         return x * factorial(x-1)
# x = int(input())
# print(factorial(x))

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1 
#     else: 
#         return fib(n-1) + fib(n-2)
# print(fib(7))



# def even_elements(mylist):
#     if mylist == []:
#         return []
#     elif mylist[0]% 2 == 0:
#         return [mylist[0]] + even_elements(mylist[1:])
#     else:
#         return even_elements(mylist[1:])
    
# print(even_elements([3,4,5,34,23,45,67,54,33,12]))


# def oo_elements(mylist):
#     if mylist == []:
#         return []
#     elif mylist[0] % 2 != 0:
#         return [mylist[0]] + oo_elements(mylist[1:])
#     else: 
#         return oo_elements(mylist[1:])
# print(oo_elements([12,33,21,54,31,23,71,29]))


# def encoding(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + encoding(mylist[2:])
# print(encoding(["A", 12, "B", 4, "A", 6, "B", 1]))    


# def encoding(mylist, count=1):
#     if len(mylist) == mylist.count(mylist[0]):
#         return [mylist[0], len(mylist)]
#     if  mylist[0] == mylist[1]:
#         return encoding(mylist[1:], count +1)
#     else:
#         return [mylist[0], count] + encoding(mylist[1:], count = 1)
# print(encoding(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B']) )   


# def primelist(mylist):
#     if mylist == []:
#         return []
#     elif type(mylist[0]) == int:
#         return [mylist[0]]+ primelist(mylist[1:])
#     else:
#         return primelist(mylist[0]) + primelist(mylist[1:])

# print(primelist([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))    

# def dec_to_bin(number):
#     if number == 1:
#         return '1'
#     else:
#         return str(number%2) + dec_to_bin(number//2)
# number = int(input(' Enter number : '))
# print(dec_to_bin(number)[::-1])

