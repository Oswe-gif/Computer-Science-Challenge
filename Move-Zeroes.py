from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nextPositionNonZeroPointer=0
        for i in range(0, len(nums)):
            if nums[i]!=0:
                currentValue=nums[i]
                nums[i] = nums[nextPositionNonZeroPointer]
                nums[nextPositionNonZeroPointer] = currentValue

                nextPositionNonZeroPointer += 1
        return nums
    
solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
