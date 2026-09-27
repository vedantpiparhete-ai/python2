class OddError(Exception):
    pass
def evenOdd(n):
    if n % 2 != 0: # if we put == here so it wil give odd no. exception or if i give != it will even no. exception .
        raise OddError("Odd number encountered")
    else:
        print("number Exception")
n=int(input("Enter a number: "))
try:
    evenOdd(n)
except OddError as e:
    print(e)