class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        intList = [int(i) for i in str(x)]
        for idx in range(len(intList) // 2):
            if intList[idx] != intList[-(idx + 1)]:
                return False
        return True

if __name__ == "__main__":
    soln = Solution()
    print(soln.isPalindrome(121))