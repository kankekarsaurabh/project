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

n=[2,4,5,6,9]
largest=n[0]
for i in (n):
    