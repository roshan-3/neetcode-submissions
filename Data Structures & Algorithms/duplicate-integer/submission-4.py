class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_set = set()
        for n in nums:
            if n in temp_set:
                return True
            else:
                temp_set.add(n)
        return False