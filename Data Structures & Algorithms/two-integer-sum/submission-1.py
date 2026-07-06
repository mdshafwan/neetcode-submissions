class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            differnce = target - nums[i]
            if differnce in hashmap:
                return [hashmap[differnce],i]
            hashmap[nums[i]] = i