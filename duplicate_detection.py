class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


sol = Solution()
num_array_1 = [1, 2, 3, 1]
num_array_2 = [1, 2, 3, 4]
num_array_5 = [1, 2, 3, 4, 5]
num_array_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
num_array_4 = [2, 14, 18, 22, 22]
print(sol.containsDuplicate(num_array_1))
print(sol.containsDuplicate(num_array_2))
print(sol.containsDuplicate(num_array_5))
print(sol.containsDuplicate(num_array_3))
print(sol.containsDuplicate(num_array_4))