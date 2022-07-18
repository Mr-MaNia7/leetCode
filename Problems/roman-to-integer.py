class Solution:
    def romanToInt(self, s: str) -> int:
        self.R2IDictionary = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        self.intList = [self.R2IDictionary[roman] for roman in s]
        self.intNum = 0

        index = 0
        while index < len(s):
            currentNum = self.intList[index]
            if index + 1 < len(s): nextNum = self.intList[index + 1]
            else: nextNum = 0

            # There are two cases to consider here
            # 1. when the number next to the current one is greater
            # 2. or otherwise
            if nextNum > currentNum:
                self.intNum += nextNum - currentNum
                index += 2
            else:
                self.intNum += currentNum
                index += 1
                while currentNum == nextNum:
                    self.intNum += nextNum
                    if index + 1 < len(s):
                        currentNum = self.intList[index + 1]
                        if index + 2 < len(s):
                            nextNum = self.intList[index + 2]
                        else:
                            index += 1
                            break
                    else:
                        index += 1
                        break
                    index += 1
        return self.intNum
            
if __name__ == "__main__":
    soln = Solution()
    print(soln.romanToInt("MMCMLXIV"))
