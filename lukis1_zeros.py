#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev_idx = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                hold = nums[prev_idx]
                nums[prev_idx] = nums[i]
                nums[i] = hold
                prev_idx += 1
        return nums
nums1 = [0,1,0,3,12]   
nums2 = [8,1,0,0,21]
nums3 = [0,5,0,74,0]

sol = Solution()

print(sol.moveZeroes(nums1))
print(sol.moveZeroes(nums2))
print(sol.moveZeroes(nums3))