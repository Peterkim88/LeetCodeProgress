class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        while numRows > 0:
            subRes = []
            
            if len(res) == 0:
                subRes.append(1)
            elif len(res) == 1:
                subRes = [1, 1]
            else:
                last = res[-1]
                for i in range(len(last)+1):
                    if i == 0 or i == len(last):
                        subRes.append(1)
                    else:
                        newNum = last[i-1] + last[i]
                        subRes.append(newNum)
                        
            res.append(subRes)
            numRows -= 1
            
        return res