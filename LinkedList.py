#Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

n=int(input("Enter a number"))

arr=[]
print(arr)

def odd():
    for i in range(1,n+1):
        if i%2!=0:
            arr.append(i)
           
odd()
print(arr)
