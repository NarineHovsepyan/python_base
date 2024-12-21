# Exercise 110

# my_list = []
# while True:
#     n = int(input(' Enter number : '))
#     if n == 0:
#         break
#     else:
#         my_list.append(n)
# my_list.sort()
# print(my_list)

#_--------------------------
# Exercise 111
# my_list = []
# while True:
#     n = int(input(' Enter number : '))
#     if n == 0:
#         break
#     else:
#         my_list.append(n)
# my_list.sort(reverse=True)
# print(my_list)

#---------ete min u max mek hat chi-------------------------------------
# # Exercise 112
# my_list = []
# while True:
#     text = input(' Enter number')
#     if text == '':
#         break
#     else:
#         my_list.append(int(text))
# if len(my_list)<4:
#     print ('ERROR')
# else:
#     print(my_list)
#     my_list.remove(min(my_list))
#     my_list.remove(max(my_list))
#     print(my_list)

#----------------------------------------
# Exercise 113

# mylist = []
# while True:
#     word = input('Enter number')
#     if word == '':
#         break
#     if word not in mylist:
#         mylist.append(word)
# print (mylist)


#----------------------------------------
# Exercise 114
# list1=[]
# list2=[]
# list3=[]
# while True:
#     number = input(':')
#     if number == '':
#         break
#     number = int(number)
#     if number < 0:
#         list1.append(number)
#     elif number==0:
#         list2.append(number)
#     else:
#         list3.append(number)
# print(list1,list2,list3)


#----------------------------------------
# Exercise 116
# for n in range(1,10001):
#     summ = 0
#     for i in range(1, n//2 +1):
#         if n%i == 0:
#             summ +=i
#     if summ == n:
#         print(n)


#--------------------------bacasakannery chi dasavorum--------------
# mylist = [12,34,66]
# for i in range(0, len(mylist)):
#     for j in range(0, len(mylist)- 1):
#         if mylist[j]>mylist[j]+1:
#             mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
# print(mylist)
#--------------------------------------------------
# list = [1,2,3,4]
# newlist = []
# for i in range(0,len(list)):
#     for j in range(i+1, len(list)+1):
#         newlist.append(list[i:j])
# print(newlist)

#--------------------------------------------------
# list =[12,23,34,45,45,6,7,8,9,87,678,567,456,345,234,765,321,1234,5678,1234,5678,835,637,987,421,234,5,5,5,6,5,6,5,6,5,6,5,6,5,6,5,7,6,8,7,9,8,7,6,5,5,4,3,3,3,3,277,213,543,987,321]
# n = 277
# start = 0
# stop = len(list)
# while True:
#     mid = (start+stop) // 2
#     if list[mid] == n:
#         print(mid)
#         break
#     elif list[mid]<n:
#         start = mid +1
#     else:
#         stop = mid -1

#--------------------------------------------------
# text =input('Enter text: ')
# list = []
# for i in text:
#       if i not in list:
#         list.append(i)
# print(len(list))

#----------------------------------------------------------
# list = [0,1,2,3,4,5,6,7,8,9]
# newlist = []
# for i in range(len(list)):
#     if list[i] % 2 ==0:
#         newlist.append(1)
#     else:
#         newlist.append(list[i]%5)
# print(newlist)


#---------------------------------
# list = [0,1,2,3,4,5,6,7,8,9, 0,9,0,0,0]
# newlist = []
# for i in range(0, len(list)):
#     if list[i] !=0:
#         newlist.append(i)
# print(newlist)

#-------------------------------
# list = [[[1,2,3], [2,3,4],[4,5,6]]]
# print([i for i in list for i in i for i in i])

#-------------------------------------------------
# text = 'hello python team'
# text = text.split(' ')
# text.sort(key=len)
# print(text[-1])

