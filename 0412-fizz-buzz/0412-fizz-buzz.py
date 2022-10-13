class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        
        for n in range(1, n+1):
            div3 = (n % 3 == 0)
            div5 = (n % 5 == 0)
            if div5 and div3:
                res.append("FizzBuzz")
            elif div3:
                res.append("Fizz")
            elif div5:
                res.append("Buzz")
            else:
                res.append(str(n))
                
        return res