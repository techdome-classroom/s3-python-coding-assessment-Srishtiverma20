class Solution:
    def isValid(self, s: str) -> bool:
        arr = [''] * len(s)
        top = -1

        for ch in s:
            if ch =='(':
                top+=1
                arr[top] = ')'
            elif ch =='[':
                top+=1
                arr[top] = ']'
            elif ch =='{':
                top+=1
                arr[top] = '}'
            elif top == -1 or arr[top] != ch:
                return False
            else:
                top -= 1
            
        
        # All counts should be zero if balanced
        return top == -1




    



  

