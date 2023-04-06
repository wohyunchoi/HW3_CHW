def factorial(n):
    num = 1
    
    if n == 1:
        return 1
    elif n == 0 :
        return 1 
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    
    for i in range(0,15,2):
        print("{0:d}! = {1:d}".format(i,factorial(i)))
