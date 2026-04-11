import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mLen = math.ceil(len(nums) / 2)
        fCounter = {}

        for num in nums:
            if num in fCounter:
                fCounter[num] += 1
            else:
                fCounter[num] = 1

            if fCounter[num] >= mLen:
                return num

        return nums[0]
