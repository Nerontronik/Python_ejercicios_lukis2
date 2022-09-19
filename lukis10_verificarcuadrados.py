#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

from math import ceil
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = ceil(num / 2)
        while left <= right:
            mid = (left+right) // 2
            sqr = mid*mid
            if sqr == num:
                return True
            if sqr < num:
                left = mid+1
            else:
                right = mid - 1
        return False
         
num1 = 16
num2 = 14

sol = Solution()
print(sol.isPerfectSquare(num1))
print(sol.isPerfectSquare(num2))