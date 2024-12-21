# Exercise1
# Create new list which have 6 different data types.
# For example: str, int

# my_list = (12, True, 'python', 3.18)
# print(my_list)

#----------------------------------------------------
#Exercise 2
# Create new list which have data notebooks and you want check if  
# the data have Mac?
# For example: my_list =[“Hp”,“Asus”,“Dell”,“Mac”,”Lenovo”] 
# output: True

# my_list = ['Hp', 'Asus', 'Dell', 'Mac', 'Lenovo']
# #print(True, [i for i in my_list if i == "Mac"])
# for i in my_list:
#     if i == 'Mac':
#         print(True)

#------------------------------------------
# Exercise 3  ------sxal------
# Create python program which will check if your password is strong 
# or no. if Len your password is great than 8 and if your password have  
# 2 numbers and 2 of the following special characters ('!', '@', '#', '$', '%', 
# '&', '*') Sample Input: Python@$World11

# number = 0
# char = 0
# password = ('Python@$World11')
# for i in password:
#     if i.isdigit():
#         number+=1
#     elif i.isalpha():
#         continue
#     else:
#         char +=1
# if char>0 and number>=2:
#     print(' Password is strong')
# else:
#     print('Try again')

#---------------------Chlucvac---------------------
# Exercise 4
# Create python program where you want to findid in link if link have 
# id print id.
# Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU 
# Sample Output: RWW2aUSwvU


#-------------------------------------------------------
# Exercise 5
# Create python program where you want to check if input word is 
# palindrome or no .if yes print Open otherwise Trash
# Sample Input: RACECAR  

# text = input(' Enter text: ')
# if text ==text[::-1]:
#     print('Open')
# else:
#     print('Trash')

#---------------------------------------
# Exercise 6
# Create python program to convert string to a list
# my_list = []
# text = input(' Enter string text: ')
# for i in text:
#     my_list+=i
# print(my_list)

#------------------------------------------

# Exercise 7 --------chstacvac----
# Create python program which will show all even numbers in your 
# string. Note: you have input where have 5 numbers:

# my_list = []
# y = 5
# for i in range(5):
#     x = int(input('Enter number'))
#     for j in range (x):
#         if j%2==0:
#             j == str(j)
#             my_list += j
#     print(my_list)

#-----------------------------------------------------
# Exercise 8
# Write a Python program to select the odd items of a list. And delete 
# even items

# my_list = [12, 44, 64, 90, 77, 67,24, 86]
# print([i for i in my_list if i %2==0])

#-----------------------------------------------------
# Exercise 9
# Your group have 5 people and each of them can  
# take one name and when take this name is delete 
# from this list.And he can not take his name:

# my_list = ['Davit', 'Gor', 'Anna', 'Mark', 'Eva']
# print(my_list)
# for i in my_list:
#     anun = input(' Enter name')
#     my_list == my_list.remove(anun)
#     print(my_list)

#---------------------------------------------------
# Exercise 10
# Create a python program which delete all  
# duplicate items in list.

# my_list = [12, 23,88,45,12,2,3,2,3,2,3,2,3,2]
# print(my_list)
# for i in my_list:
#     for j in my_list:
#         if i ==j:
#             my_list ==my_list.remove(j)
# print(my_list)

#----------------------------------------
# Exercise 11
# 3. Write a Python program to 
# get the largest text from a list.

# my_list = ['hahaha', 'laudegd', 'yt', 'tasdaka']
# my_list.sort(key=len)
# my_list=my_list[::-1]
# print(my_list[0])

#------------------------------------------
# Exercise 12
# Write a Python program that have two 
# lists and returns True if they have at least 
# one common member.
# my_list1 = [12,34,23,23]
# my_list2=[12,23,33,65,7]
# for i in my_list1:
#     for j in my_list2:
#         if i == j:
#             print(True)

#-----------------------

# number = int(input('Enter number: '))
# my_list = []
# for i in range(1,number):
#     if number%i == 0:
#         my_list.append(i)
# print(my_list)

#------------------
# import random
# anun = input('Enter name')
# master = ['♥', '♦', '♣', '♠']
# karter = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# kalod=[i+j for i in master for j in karter]
# nor_kalod = []
# while kalod != 0:
#     random_kart = random.choice(kalod)
#     nor_kalod.append(random_kart)
#     kalod.remove(random_kart)
# print(nor_kalod)

#--------------------------------------
# mylist = [1,2,3,4]
# list = []
# for i in range(len(mylist)):
#     for j in range(i, len(mylist)):
#         list.append(i) 
#         print(list)

#------------------------------------
# list = [7,4,5,8,1,3,6,9]
# for i in range(len(list)):
#     for j in list:
#         if list[i]<j:


