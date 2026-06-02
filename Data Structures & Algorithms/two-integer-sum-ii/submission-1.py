class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right: int = len(numbers) - 1
        left: int = 0

        while left < right:
            sum = numbers[left] + numbers[right]
            if (sum > target):
                right -= 1
            elif (sum < target):
                left += 1
            elif (sum == target):
                return [left + 1, right + 1]