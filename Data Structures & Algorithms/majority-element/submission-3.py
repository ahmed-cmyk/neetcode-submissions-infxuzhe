class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        count = 0

        for num in nums:
            if count == 0:
                current = num
                count = 1
            elif num == current:
                count += 1
            else:
                count -= 1

        return current
