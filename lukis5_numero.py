#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

from math import floor
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            sq_sum = 0
            while n > 0:
                sq_sum += (n%10)*(n%10)
                n = floor(n/10)
            if sq_sum == 1:
                return True
            n = sq_sum
        return False
sol = Solution()

print(sol.isHappy(19))
print(sol.isHappy(2))