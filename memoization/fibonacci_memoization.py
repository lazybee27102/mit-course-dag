class Fibonacci:
    memo = {} 
    
    def fib(number):
        if(number in memo)
            return memo[number]
        if (number <= 2)
            return 1
        else 
            memo[number] = fib(number-1) + fib(number-2)
        return memo[number]



