# tiv = int(input('Enter number'))
# count_200 = tiv // 200
# tiv = tiv % 200
# count_100 = tiv // 100
# tiv = tiv% 100
# count_25 = tiv // 25
# tiv = tiv % 25
# count_10 = tiv // 10
# tiv = tiv % 10
# count_5 = tiv // 5
# tiv = tiv % 5
# count_1 = tiv // 1
# print(count_200\n count_100\n count_25\n count_10\n count_5\n count_1\n)


# a = float (input(" a = "))
# b = float (input(" b = "))
# print ( 'S =', a * b )
# print (type(a), type(b))

# a = int(input('Enter number'))
# for i in range(a + 1):
#     for j in range(a + 1):
#         if i == j or a == i + j:
#             print ('^' , end = '')
#         else:
#             print("  ", end ="") 
#     print() 

# n = int(input(' Enter number: = '))
# for i in range(2,n):
#     if n % i == 0:
#         print(False)
#         break
# else:
#     print(True)

#_____________________________________
# text = 'python 3.18'
# count_let = 0
# count_number = 0
# count_char = 0
# for i in text:
#     if i.isdigit():
#         count_number += 1
#     elif i.isalpha():
#         count_let += 1
#     else:
#         count_char += 1
# print(f'Let ={count_let}\nNumber ={count_number}\nChar ={count_char}')
    
#-----------------------------------------

# x = int(input("Enter x = "))
# y = int(input(' Enter y = '))
# if x > y:
#     for i in range(x, x*y +1, x):
#         if i % x == 0 and i % y == 0:
#             print(i)
#             break
# elif x<y:
#     for i in range(y, x*y +1, y):
#         if i % x == 0 and i % y == 0:
#             print(i)
#             break
# else:
#     print(x)  

#--------------------------------
# x = input(" input number")
# summ = 0
# for i in str(x):
#     summ += int(i)
# print(summ)
# text = input()
# tt = text[::-1]
# for i in tt:
#     print(i)
#--------------------------------
# text = input('  ')
# summ = 0
# for i in text:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

# number = int(input('Enter number'))
# sum = 1
# for i in range(1, number+1):
#     sum *= i
# print(sum)
#--------------------------------------------
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('fizz bazz')
#     elif i % 3 == 0:
#         print('fizz')
#     elif i% 5 == 0:
#         print('bazz')
#     else:
#         print(i)
#-------------------------------------------
# text = input('text  :   ').lower()
# count = 0
# for i in text:
#     if i == 'a':
#         count += 1
# print(count)
#----------------------------------------------
# Fibonacci
# n1, n2 = 0, 1
# for i in range (40):
#      print(n1)
#      n1, n2 = n2, n1 + n2
#-----------------------------
# text = input('Enter text: ')
# count_let = 0
# count_num = 0
# count_char = 0
# for i in text:
#     if i.isdigit():
#         count_num += 1
#     elif i.isalpha():
#         count_let += 1
#     else:
#         count_char += 1
# print(f'Let --->{count_let}\nNumber -->{count_num}\nChar --->{count_num}')

#-----------------------------------

# sum = 0
# count = 0
# while True:
#     number = (input(' Enter number:'))
#     if number == '':
#         break
#     else:
#         count += 1
#         sum += int(number)
# print(sum/count)

#------------------------------------------------
# Sum = 0
# while True:
#     age = (input(' age = '))
#     if age == '':
#         break
#     else:
#         age = int(age)
#         if 2 >= age > 0:
#              continue
#         elif  12 >= age >= 3:
#             Sum += 14
#         elif  65 >= age > 12:
#             Sum += 23
#         else:
#             Sum += 18
# print (Sum)
#--------------------------------------------
#Kesar
# text = input(' Enter tex:')
# for i in text:
#     print(chr((ord(i)+3)), end='^')
#------------------------------------------------
#pi

# pi = 3
# a= 2
# b= 3
# c = 4
# for i in range(15):
#     pi += (4/(a*b*c))*((-1)**i)
#     a, b, c = a+2, b+2, c+2
# print(pi)
#------------------------------------------------

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# import random
# count_O = 0
# count_P = 0
# result = ''
# while True:
#     if count_P == 3 or count_O == 3:
#         break
#     text = random.choice("OP")
#     if text == 'O':
#             result += 'O'
#             count_O += 1
#             count_P == 0
            
#     else:
#             result += 'P'
#             count_P += 1
#             count_O == 0    
# print (result)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# sum = 0
# count = int(input('Enter count'))
# for i in range(count):
#     number = int(input('Enter number'))
#     for j in range(2,number):
#         if number % j == 0:
#             break
#     else:
#         sum += 1
# print(sum)



# S = 0        
# number = int(input('Enter number'))
# for i in range(1,number+1):
#     sum = 1
#     for j in range(i):
#     sum *=i
#     S += sum
#     print (S)

#---------------------
# sum = 0
# count = int(input('jjj'))
# for i in range(0,count + 1, 5):
#     price = int(input(f'{i} --> '))
#     sum += price
# print (sum)


# a = int(input("Enter a = "))
# b = int(input("Enter b = "))
# c = int(input("Enter c = "))
# for i in range(a,b):
#     if i % c == 0:
#         print (i)

# x = 0
# n = int(input("Enter n = "))
# while n>12:
#     n/=2
#     x +=2
# print(x)

#--------------------------------------

# text = input('Enter text')
# for i in text:
#     if i.isdigit():
#         continue
#     elif i.isalpha():
#         continue
#     else:
#         text == text.replace(i, '')
# print(text == text[::-1])

# bin_cod = input('Enter cone = ')
# bin_cod = bin_cod[::-1]
# number = 0
# for i in range(0,len(bin_cod)):
#     number += int(bin_cod[i])*2**i
# print (number)
#-----------------------------
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i*j:>4}', end='')
#     print()


# n = int(input("Enter number"))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if j == 0 or j == n:
#             print('|', end='')
#         elif i == 0 or i == n:
#             print('--', end='')
#         else: 
#             print('  ', end='')
#     print()

# n = int(input("Enter number"))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if i + j == n or i == j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()        

# for i in  range(1,11):
#     for j in range(1,11):
#         print(f'{i * j:>4}', end=' ')
#     print()

# n = int (input( ' Enter number'))
# text = ''
# while n > 1:
#     text += str(n%2)
#     n //= 2
# print ('1' + text[::1])

# for i in range(0,6):
#     for j in range(i, 11 + i, 2):
#         print(f'{j:>3}', end='' )
#     print()


# n = int(input(' Enter n: '))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i , end='  ')
#     print()    

# n = int(input(' Enter n: '))
# for i in range(0,n+1):
#     for j in range(0,n+1):
#         if j == 0 or j == n:
#             print('|', end='')
#         elif i == 0 or i == n:
#             print('--', end='')
#         else:
#             print('  ', end='')
#     print()

# n = int(input(' Enter n: '))
# for i in range(n+1):
#     for j in range(n+1):
#         if j == i or j + i == n:
#             print('^', end='')
#         else:
#             print('  ', end='')
#     print()

# count = 0
# n = int(input(' Enter n: '))
# for i in range(1, n+1):
#     tiv = int(input('number'))
#     for j in range(2,tiv):
#         if tiv % j == 0:
#             break
#     else:
#         count +=1
# print(count)


# n = int(input(' Enter n : '))
# for i in range(n):
#     for j in  range(2*n - 1):
#         if j < (2 * n - 1)//2 - i or j > (2 * n - 1)//2 + i:
#             print(' ', end='')
#         else:
#             print('#', end='')    
#     print()

