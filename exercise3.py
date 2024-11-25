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
#     print(count)

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
# if both numbers are even, but returns the greater if one or both numbers are odd

def lesser(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            return b
        else:
            return a
    elif a%2!=0 or b%2==0:
        if a>b:
            return a
        else:
            return b


x=int(input("Enter first number"))
y=int(input("Enter second number"))
result=lesser(x,y)
print(result)