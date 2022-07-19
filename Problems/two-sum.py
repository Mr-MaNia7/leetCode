from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3,3], 6))