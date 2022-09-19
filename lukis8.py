#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dig_len = len(digits)
        for i in reversed(range(dig_len)):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
        
        if digits[0] == 0:
            digits.insert(0,1)
        
        return digits
            
digits = [1,2,3]
sol = Solution()
sol.plusOne(digits)
#[1, 2, 4]