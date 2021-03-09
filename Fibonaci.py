
def fibo(size):
    a=0
    b=1
    i=1
    print(a.__str__()+" ")
    while i < size:
        print(str(b) +" ")
        c =a+b
        a=b
        b=c
        i=i+1
    print("\n")


fibo(int(7))