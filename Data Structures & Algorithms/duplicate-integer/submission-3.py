class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_set = set(nums)

        return len(temp_set) != len(nums)