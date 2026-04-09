class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,x in enumerate(nums):
            map[x] = i
        for i,x in enumerate(nums):
            goal = target - x
            if goal in map and map[goal] != i:
                if map[goal] < i:
                    return [map[goal], i]
                else:
                    return [i, map[goal]]