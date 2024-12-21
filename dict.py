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
#         for i in range(len(day_list)):
#             mouth = x //day_list[i] +1
#             return mouth,  x - sum(day_list[:mouth - 1]) 
# print(calendar(2024, 59))




# import random
# def number():
#     letter = 'MNBVCXZLKJHGFDSAPOIUYTREWQ'
#     return f'{random.randint(0,9)}{random.randint(0,9)} {random.choice(letter)}{random.choice(letter)} {random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
# print(number())

