class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arrLen = len(nums) - 1
        
        i = 0
        j = i + 1

        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]

            j += 1

            if (arrLen + 1) == j:
                i += 1
                j = i + 1

        return [0,1]