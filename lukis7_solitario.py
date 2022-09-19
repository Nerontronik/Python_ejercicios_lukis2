#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc = 0
        for num in nums:
            acc ^= num
        return acc
        
nums = [5,1,2,1,2]

sol = Solution()

print(sol.singleNumber(nums))