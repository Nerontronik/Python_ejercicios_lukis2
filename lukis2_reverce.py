#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            hold = s[left]
            s[left] = s[right]
            s[right] = hold
            left +=1
            right -=1
            
        return s
            
        
s = ["h","e","l","l","o"]

sol = Solution()

sol.reverseString(s)