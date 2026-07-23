class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:

            sumis = numbers[l] + numbers[r]
            print(sumis)
            if sumis == target:
                return [l+1 , r+1]
            if sumis > target:
                r -= 1
                continue
            else:
                l += 1
                continue
