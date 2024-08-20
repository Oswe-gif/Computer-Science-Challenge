import bisect
from itertools import combinations
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        left = nums[:n]
        right = nums[n:]
        leftDictionary ={0:[0]}
        rightDictionary ={0:[0]}
        minimumSum= 10**10*15
        if minimumSum == 0:
            return 0
        for i in range(1, n+1):
            rightDictionary[i]=[]
            leftDictionary[i]=[]
            for j in combinations(left, i):
                leftDictionary[i].append(sum(j))            
            for j in combinations(right, i):
                rightDictionary[i].append(sum(j))
            leftDictionary[i] = sorted(leftDictionary[i])
            rightDictionary[i] = sorted(rightDictionary[i])
        #print(leftDictionary)
        #print(rightDictionary)
        
        for key in range(len(rightDictionary)):
            for leftElement in leftDictionary[key]:
                index = min(bisect.bisect_left(rightDictionary[n-key], sum(nums)/2 - leftElement),len(rightDictionary[n-key])-1)
                rightElement= rightDictionary[n-key][index]
                if minimumSum > abs(rightElement+leftElement-sum(nums)/2):
                    minimumSum=abs(rightElement + leftElement - sum(nums)/2)
        return int(minimumSum*2)

solution = Solution()
print(solution.minimumDifference([2,-1,0,4,-2,-9]))
print(solution.minimumDifference([3,9,7,3]))
print(solution.minimumDifference([-36,36]))
