def Fibonacci():
    num = int(input("How Many Fibonacci Numbers Would You Like To Generate:"))
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        i = 1
        while i < (num - 1):
            fib.append(fib[i-1] + fib[i])
            i += 1
    return fib
         
print(Fibonacci())    
            
