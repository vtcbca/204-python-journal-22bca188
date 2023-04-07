def makedict(n):
    dic={}
    c=int(input("Enter minimum word length:"))
    for i in n:
        if len(i)>=c:
            dic[i]=len(i)

    print(dic)

def input1():
    str=input("Enter sentence:")
    a=str.split(" ")
    makedict(a)

input1()    