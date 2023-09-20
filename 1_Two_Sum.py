class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            target = target - nums[i]
            for (i) in range(len(nums)):
                if(nums[c] == target):
                    return(i,c)




sol = Solution()
nums1 = [2, 9, 11, 15, 7]; target1 = 9
nums2 = [3, 3]; target2 = 6
nums3 = [1, 2, 3, 4, 5]; target3 = 0
nums4 = [1, 3, 4, 10]; target4 = 9

print(sol.twoSum(nums1, target1))
print(sol.twoSum(nums2, target2))
print(sol.twoSum(nums3, target3))
print(sol.twoSum(nums4, target4))