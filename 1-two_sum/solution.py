class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hl = {}
        for idx, num in enumerate(nums):
            hl[num] = idx
        
        for idx, num in enumerate(nums):
            if (target - num) in hl and hl[target - num] != idx:
                return [idx, hl[target - num]]
        
        return None
            