class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        z = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[z] = nums[i]
                z = z+1

        for i in range(z,len(nums)):
            nums[i] = 0
            z =  z+1

        return nums

        