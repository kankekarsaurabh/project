#2Sample input

#2
#hacker book
#we are finding vowels


# def vowel(letter):
#     return letter in ['a', 'e', 'i', 'o', 'u', 'y']
    

# word= input("Enter a string")
# count=0
# for letter in word:
#     found=vowel(letter)
#     count+=1
# #     print(count)

# q1) LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd

# def lesser(a,b):
#     if a%2==0 and b%2==0:
#         if a>b:
#             return b
#         else:
#             return a
#     elif a%2!=0 or b%2==0:
#         if a>b:
#             return a
#         else:
#             return b


# x=int(input("Enter first number"))
# y=int(input("Enter second number"))
# result=lesser(x,y)
# print(result)

#2) ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter2
# def animal(x,y):
#     if x[0]==y[0]:
#         return "Same letter"
#     else:
#         return "Different letter"


# a=input("Enter a string")
# x,y=a.split(" ")
# result=animal(x,y)
# print(result)

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# def firstfourth(b):
#     if len(b)>=4:
#         z= {b[0].upper()+b[1:3] + b[3].upper()+ b[4:]}
#         return z
#     elif len(b)<4:
#         z  = b[0].upper() + b[1:]
#     else:
#         return z


# x=input("Enter a string")
# result=firstfourth(x)
# print(result)

# 3)
# MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. 
# The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:


# def yoda(string):
#     z=""
#     for i in range(len(string) -1,-1,-1):
#         z=z +string[i]
#     return z
# x=input("Enter a string")
# result=yoda(x)
# print(result)


# 4)Given an integer n, return True if n is within 10 of either 100 or 200

# def within(a):
#     if 90<=a<=110 or 190<=a<=210:
#         return True
#     else:
#         return False

# n=int(input("Enter a number"))
# result=within(n)
# print(result)

#5)Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def three(a):
   
#     for i in range(len(a)):
#         if a[i] == 3:
#             i+=1
#             if a[i]==3:
#                 print(i)
#                 return True

# array=[1,3,4,5,6,3,4,33,44,33,3,3,44,44]
# result= three(array)
# print(result)

#6)  PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# def doll(string):
#     multiplier=""
#     add=""
#     for i in string:
#         add=i+i+i
#         multiplier=multiplier+add
#     return multiplier

# s=input("Enter any string")
# result=doll(s)
# print(result)

#7 BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, 
# reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19




# def validate(a,b,c):
#     sum=0

#     if 1<=a<=11 and 1<=b<=11 and 1<=c<=11:
#         sum=a+b+c
#         if sum<=21:
#             return sum
#         elif sum >21 and (a==11 or b==11 or c==11):
#             sum=sum-10
#             if sum > 21:
#                 return "BUST"
#             else:
#                 return sum
#         elif sum>21:
#             return "BUST"
#     else:
#          return "Invalid input"
# try:    
#     num1=int(input("first number\n"))
#     num2=int(input("Second Number\n"))
#     num3=int(input("third number\n"))
#     result=validate(num1,num2,num3)
#     print(result)
# except ValueError:
#         print ("Invalid input")


# 7) SUMMER OF '69: Return the sum of the numbers in the array,
#  except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


#Need to fix
# def six(a):
#     sum=0
#     for i in range(len(a)):
#         sum=i+sum
#         if a[i] == 6:
#             i+=1
#             if a[i]==9:
#                 print(i)
#                 return True

# array=[1,3,5]
# result= six(array)
# print(result)



# 8) CHALLENGING PROBLEMS
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False



# 9) COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

    


# 10) Just for fun:

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E