def factorial(num:int)->int:
    '''
    calculate n! using recursion
    Args:
        num(int):user input the int number
    return:
        num(int):return the factorial
    '''
    if num ==0:
        return 1
    return num*factorial(num-1)

factorial(5)


def is_prime(num:int)->bool:
    '''
    check for the number is prime or not
    
    Args:
        num(int):number for check
    
    return:
        bool : true if that prime or false if not prime
        
    '''
    
    for i in range(2,num):
        if num % i ==0:
            return False
        
    return True

is_prime(3)


def common_dividor(num1:int,num2:int)->list[int]:
    '''
    this func help to calc the common division
    
    '''
    limit=min(num1,num2)
    divisors=[]
    for divisor in range(1,limit+1):
        if num1 % divisor == 0 and num2 % divisor ==0:
            divisors.append(divisor)
    return divisors

common_dividor(10,20)
         