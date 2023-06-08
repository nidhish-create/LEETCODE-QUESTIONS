class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeats: dict[int, int] = {}
        pairs = 0
        for num in nums:
            if num in repeats:
                pairs += repeats[num]
                repeats[num] += 1
            else:
                repeats[num] = 1
        return pairs
