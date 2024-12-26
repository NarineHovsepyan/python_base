
# def primelist(mylist):
#     if mylist == []:
#         return []
#     elif type(mylist[0]) == int:
#         return [mylist[0]] + primelist(mylist[1:])
#     else:
#         return primelist(mylist[0]) + primelist(mylist[1:])
# print(primelist([1,[2,3], [4,[5,[6,7]]], [[[8], 9], [10]]]))



# def encoding(mylist, count = 1):
#    if len(mylist)== mylist.count(mylist[0]):
#       return [mylist[0], len(mylist)]
#    if mylist[0] == mylist[1]:
#       return encoding(mylist[1:], count + 1)
#    else:
#       return [mylist[0], count] + encoding(mylist[1:], count=1)
# print(encoding(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B']))



# def encoding(mylist):
#    if mylist == []:
#       return []
#    else:
#       return [mylist[0]] * mylist[1] + encoding(mylist[2:])
# print(encoding(["A", 12, "B", 4, "A", 6, "B", 1]))  


# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x-1)
# x = int(input(' Enter x : '))
# print(factorial(x))

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# n = int(input("Enter fib.number : "))
# print(fib(n))

# def even_elements(mylist):
#     if mylist == []:
#         return []
#     elif mylist[0]%2 == 0:
#         return mylist[0] + even_elements(mylist[1:])
#     else:
#         return even_elements(mylist[1:])
    
# print(even_elements([3,4,5,34,23,45,67,54,33,12]))


# def count(text, ch):
#     if text == '':
#         return 0
#     if ch == text[0]:
#         return 1 + count(text[1: len(text)], ch)
#     else:
#         return count(text[1: len(text)], ch)
# text = input(' enter text : ')
# ch = input('Enter letter: ')
# print(count(text, ch))

# 173
# def summ():
#     n = input('Enter number: ')
#     if n =='':
#         return 0
#     else:
#         return float(n) + summ()  
# print(summ())

#174
# def Evclid(a,b):
#     if b == 0 or b == a or a == 0:
#         return a
#     elif a>b:
#         return Evclid(b, a%b)
#     else:
#         return Evclid(a, b%a)
# a = int(input('a = '))
# b = int(input(' b = '))
# print(f'k = {Evclid(a,b)}')

#176
# def NATO(text, nato_alphabet):
#     if text == []:
#         return []
#     elif text[0] in nato_alphabet:
#         return [nato_alphabet[text[0]]] + NATO(text[1:], nato_alphabet)
#     else: 
#         return [text[0]] + NATO(text[1:], nato_alphabet)
# nato_alphabet = {
#     'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
#     'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
#     'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
#     'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whisky', 'X': 'X-ray',
#     'Y': 'Yankee', 'Z': 'Zulu'
#                 }
# text = [ 'H', 'E', 'L', 'L', 'O']
# print(NATO(text, nato_alphabet))

#175
# def bin(n):
#     if n == 1:
#         return '1'
#     else:
#         return str(n%2) + bin(n//2)
# n = int(input('n = '))
# print(bin(n)[::-1])



