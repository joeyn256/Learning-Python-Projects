print("\nType: 'exit' to end\n")
def IsPrime():
    while True:
        num = input("Enter a Number or Type 'exit': ")
        if num == "exit":
            break
        list1 = [x for x in range(2, int(num)) if int(num) % x == 0]
        if len(list1) > 0:
            print('not prime')
            print("Divisors:", list1)
        else:
            print('prime')

IsPrime()
    
