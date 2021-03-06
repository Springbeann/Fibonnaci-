class Fibonacci:
    def __init__(self):
        self.cache = [0,1]
    
    def __class__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')
        
        if n< len(self.cache):
            return self.cache[n]
        else:
            fib_number = self(n-1) + self(n-2)
            self.cache.append(fib_number)
        
            return self.cache[n]