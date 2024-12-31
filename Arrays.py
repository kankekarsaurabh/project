# <<<<<<< HEAD
# # DSA practice
# =======
# #Arrays
# # 
# # 
# # 
# # #monthly expenses
# list=[2200,2350,2600,2130,2190]
# extra=list[1]-list[0]
# print(extra)

# #first quarter
# first_quarter= list[0]+list[1]+list[2]
# print(first_quarter)

# #exactly 2000
# for i in list:
#     if i==2200:
#         print("Match found")
#     else:
#         print("Searching")

# list.insert(5, 1980)
# print(list)

# list[3]=list[3]-200
# print(list[3])
# print(list)

# #2
# heros=['spider man','thor','hulk','iron man','captain america']

# heros.append("black panther")
# print(heros)

# heros.remove("black panther")
# print(heros)

# heros.insert(3,"black panther")
# print(heros)

# heros[1:3]=["Doctor Strange"]
# print(heros)

# heros.sort()
# print(heros)

# #3)Create a list of all odd numbers between 1 and a max number. 
# # Max number is something you need to take from a user using input() function

# n=int(input("Enter a number"))

# arr=[]
# print(arr)

# def odd():
#     for i in range(1,n+1):
#         if i%2!=0:
#             arr.append(i)  
# odd()
# print(arr)

#second largest number in an array

# Example:
# Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

# Output:  6

# n = [2, 10, 5, 6, 9]
# largest = n[0]
# for i in n:
#     if i > largest:  # Add a conditional check
#         largest = i

# print(largest)
# >>>>>>> origin/main

# new array

# n= [1,2,3,4,5]
# split =4
# if split in n:
#     split_index=n.index(split)
#     part1= n[:split_index]
#     part2= n[split_index:]
# else:
#     part1=n
#     part2=[]

# part3= part2+part1
# print(part3)

#Count the number of bits
# def countBits(a):
#     count=0
#     x=bin(a)
#     print(x)
#     for i in x:
#         if i=='1':
#             count=count+1
#     return count


      
# n = int(input())
# print(countBits(n))


#total prime

#Write your totalPrime function here.def isPrime(n):
# from os import *
# from sys import *
# from collections import *
# from math import *

# def isPrime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True

# def totalPrime(S,E):
#      count=0
#      for i in range(S,E):
#          if isPrime(i):
#             count=count+1
#      return count
         
    
# #Taking S and E space seperated input.
# S,E = map(int,input().split(' '))
# print(totalPrime(S,E))

#DSA 251 Arrays : Rotate by k elements
arr=[2, 4, 12, 4, 65, 43, 23, 44, 55, 23, 11, 87,23, 44, 2, 11, 42, 89, 76, 45, 32, 22, 56, 32, 41]
k=int(12)
def rotateArray(arr,k):
    # Check if the value `k` exists in the array

    position=k
    
    
    
    part1=arr[:position]
    
    part2=arr[position:]
    
    part3=part2+part1
    
    return part3



print(rotateArray(arr,k))

        