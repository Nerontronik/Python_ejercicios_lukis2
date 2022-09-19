#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        check_j = set(jewels)
        total = 0
        for st in stones:
            if st in check_j:
                total += 1
        return total
        
jewels = "aA"
stones = "aAAbbbb"

sol = Solution()
sol.numJewelsInStones(jewels, stones)