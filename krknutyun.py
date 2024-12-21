# # Exercise 10 
# k = 0
# n = int(input(' Enter n: '))
# for i in range(0,n):
#     for j in range(0,2*n):
#         if j == 0 or j == 2*n-1:
#             print(n, end='')
#         elif i>0 and j == 1  or i>0 and j == 2*n-1-1 :
#             print(n-1, end='')
#         elif i>1 and j == 2  or i>1 and j == 2*n-2-1 :
#             print(n-2, end='')
#         elif i>2 and j == 3  or i>2 and j == 2*n-3 -1:
#             print(n-3, end='')
#         elif i>3 and j == 4  or i>3 and j == 2*n-4 -1:
#             print(n-4, end='')
#         else:
#             print('.', end='')
#     print()

# for i in range(0,6):
#     for j in range(i, 11+i, 2):
#         print(f'{j:>3}', end='')
#     print() 


# n = int (input(' Enter n = '))
# for i in range(1,n+1):
#     for j in range (i):
#         print(i, end=' ')
#     print()

# count = 0
# n = int(input('enter n = '))
# for i in range(n):
#     tiv = int(input(' Enter number = '))
#     for j in range (2,tiv):
#         if tiv % j == 0:
#             break
#     else:
#         count+=1
# print(count)        


# Sum = 0
# n = int(input('Enter n = '))
# for i in range(1,n+1):
#     S=1
#     for j in range (1,i+1):
#         S *= j
#     Sum += S
# print(Sum)



# number = int((input(' Mutqagreq qaranish tiv: ')))
# n1=number%10
# n2=number//10%10
# n3=number//100%10
# n4 = number//1000
# print(n1+n2+n3+n4)

# import random
# user_= 0
# pc_ =0
# user=int(input('Enter number 0->5 : '))
# pc=random.randint(0,5)
# if pc>user:
#     pc_+=1
#     print('winner pc')
# elif pc == user:
#     print('^_^')
# else:
# #     print('Winner user')


# text = input(('text'))
# text_= 's'*len(text)
# while text_  not in text:
#     text_ =text_[:-1]
# print(text_)

# max = 0
# n = int(input('enter number'))
# for i in range(n):
#     k= int(input('k = '))
#     k = str(k)
#     sum = 0
#     for j in k:
#         sum += int(j)
#     if sum>max:
#         max = sum
# print(max)