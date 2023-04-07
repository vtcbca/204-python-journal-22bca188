def symmetric(n):
    half=(len(n)//2)
    first=n[:half]
    second=n[half:]
    if first==second:
        print(f"String {n} is symmetric!!!!")
    else:
        print(f"String {n} is not symmetric!!!")

def input1():
     a=input("Enter a string:")
     symmetric(a)
     
input1()     