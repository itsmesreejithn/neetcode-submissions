class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        count: int = 1
        res: list = []
        print(nums)

        if (len(nums) == 0):
            return 0

        for i in range(len(nums)):
            if(i != 0):
                if((nums[i] - nums[i-1]) == 1):
                    count += 1
                elif ((nums[i] - nums[i-1]) == 0):
                    continue
                else:
                    res.append(count)
                    count = 1
            res.append(count)
        res.sort()
        print(res)
        return res[-1]